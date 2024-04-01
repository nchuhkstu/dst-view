<template>
    <div id="system">
        <div id="system-left">
            <div id="total-cpu" class="system-navigation selected" @click="clickNavigation('cpu')">
                <div class="system-navigation-left">
                    <chart ref="chartRef" :name="'cpu'" :lineColor="'rgb(76,157,203)'" :itemColor="'rgb(160,160,160)'"></chart>
                </div>
                <div class="system-navigation-right">
                    <div class="system-navigation-right-font1">CPU</div>
                    <div class="system-navigation-right-font2">{{ cpuUsage }}</div>
                </div>
            </div>
            <div id="total-memory" class="system-navigation" @click="clickNavigation('memory')">
                <div class="system-navigation-left">
                    <chart ref="totalMemoryRef" :name="'memory'" :lineColor="'rgb(149,49,180)'" :itemColor="'rgb(160,160,160)'" :borderColor="'rgb(149,49,180)'"></chart>
                </div>
                <div class="system-navigation-right">
                    <div class="system-navigation-right-font1">内存</div>
                    <div class="system-navigation-right-font2">{{ memoryUsage }}</div>
                </div>
            </div>
            <div id="total-network" class="system-navigation" @click="clickNavigation('network')">
                <div class="system-navigation-left">
                    <chart ref="totalNetworkRef" :name="'network'" :lineColor="'rgb(77,166,12)'" :itemColor="'rgb(160,160,160)'" :borderColor="'rgb(77,166,12)'"></chart>
                </div>
                <div class="system-navigation-right">
                    <div class="system-navigation-right-font1">网络</div>
                    <div class="system-navigation-right-font2">{{ '↑ '+formatBytes(total_sent_per_bytes)+'/s ↓ '+formatBytes(total_recv_per_bytes)+'/s' }}</div>
                </div>
            </div>
        </div>
        <div id="system-right">
            <div id="system-cpu" v-show="show=='cpu'">
                <div class="system-right-top">
                    <div class="system-right-top1">
                        <div class="system-right-top2">CPU</div>
                        <div class="system-right-top3">{{ cpuName }}</div>
                    </div>
                    <div style="font-size: 1vh;height: 2vh;line-height: 2vh; color: rgb(140,140,140); margin-top: 1vh;display: flex;">
                        <div>60秒内的利用率%</div>
                        <div style="margin-left: auto;">100%</div>
                    </div>
                </div>
                <div id="system-right-mid" v-if="cpuCount!=null">
                    <chart style="width: 20%; height: 8vh; flex-basis: calc(25% - 0.5vw);margin: 0.5vh 0;" v-for="(cpu,index) in cpuCount" v-bind:key="index" ref="cpuRefs" :name="index+''" :lineColor="'rgb(76,157,203)'" :itemColor="'rgb(160,160,160)'" :xline="true" :yline="true"></chart>
                </div>
                <div id="system-right-bottom">
                    <div class="system-right-bottom">
                        <div style="display: flex;">
                            <div>
                                <div class="system-right-bottom-1">利用率</div>
                                <div class="system-right-bottom-2">{{ cpuUsage }}</div>
                            </div>
                        </div>
                        <div style="display: flex;">
                            <div class="system-right-bottom-4">
                                <div class="system-right-bottom-1">进程</div>
                                <div class="system-right-bottom-2">{{ processCount }}</div>
                            </div>
                            <div class="system-right-bottom-4">
                                <div class="system-right-bottom-1">线程</div>
                                <div class="system-right-bottom-2">{{ threadCount }}</div>
                            </div>
                            <div class="system-right-bottom-4">
                                <div class="system-right-bottom-1">句柄</div>
                                <div class="system-right-bottom-2">{{ handleCount }}</div>
                            </div>
                        </div>
                        <div>
                            <div class="system-right-bottom-4">
                                <div class="system-right-bottom-1">正常运行时间</div>
                                <div class="system-right-bottom-2">{{ runTime }}</div>
                            </div>
                        </div>
                        
                    </div>
                    <div class="system-right-bottom" style="margin-left: 1vw;">
                        <div class="system-right-bottom-5">基准速度:</div>
                        <div class="system-right-bottom-5">逻辑处理器:</div>
                        <div class="system-right-bottom-5">虚拟化:</div>
                        <div class="system-right-bottom-5">L2缓存:</div>
                        <div class="system-right-bottom-5">L3缓存:</div>
                    </div>
                    <div class="system-right-bottom" style="margin-left: 0.5vw;">
                        <div class="system-right-bottom-3">{{ cpuBaseSpeed }}</div>
                        <div class="system-right-bottom-3">{{ cpuCount }}</div>
                        <div class="system-right-bottom-3">{{ cpuVM }}</div>
                        <div class="system-right-bottom-3">{{ cpuL2 }}</div>
                        <div class="system-right-bottom-3">{{ cpuL3 }}</div>
                    </div>
                </div>
            </div>
            <div id="system-memory" v-show="show=='memory'">
                <div class="system-right-top">
                    <div class="system-right-top1">
                        <div class="system-right-top2">内存</div>
                        <div class="system-right-top3">{{ swap_memory }}</div>
                    </div>
                    <div style="font-size: 11px; color: rgb(112,112,112); margin-top: 10px;display: flex;">
                        <div>内存使用量</div>
                        <div style="margin-left: auto;">{{ total_memory }}</div>
                    </div>
                </div>
                <div id="system-right-mid-memory">
                    <chart ref="detailMemoryRef" :name="'memoryDetail'" :lineColor="'rgb(149,49,180)'" :itemColor="'rgb(160,160,160)'" :borderColor="'rgb(149,49,180)'" :xline="true" :yline="true"></chart>
                </div>
                <div id="system-right-bottom">
                    <div>
                        <div style="display: flex;">
                            <div>
                                <div class="system-right-bottom-1">使用中（已压缩）</div>
                                <div class="system-right-bottom-2">{{ memoryUsed + ' GB ' }}</div>
                            </div>
                        </div>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
            <div id="system-network" v-show="show=='network'">
                <div class="system-right-top">
                    <div class="system-right-top1">
                        <div class="system-right-top2">网络</div>
                        <div class="system-right-top3">游戏服务器所占带宽</div>
                    </div>
                    <div style="font-size: 1vh;height: 2vh;line-height: 2vh; color: rgb(140,140,140); margin-top: 1vh;display: flex;">
                        <div>吞吐量</div>
                        <div style="margin-left: auto;">B</div>
                    </div>
                </div>
                <div id="system-right-mid">
                    <networkChart ref="networkChartRef" :name="'networkDetail'" :lineColor="'rgb(77,166,12)'" :itemColor="'rgb(160,160,160)'" :borderColor="'rgb(77,166,12)'" :xline="true" :yline="true"></networkChart>
                </div>
                <div id="system-network-formHead">
                    <div class="system-network-formHead">世界名</div>
                    <div class="system-network-formHead">协议</div>
                    <div class="system-network-formHead">端口</div>
                    <div class="system-network-formHead">上行速率</div>
                    <div class="system-network-formHead">上行流量</div>
                    <div class="system-network-formHead">下行速率</div>
                    <div class="system-network-formHead">下行流量</div>
                </div>
                <networkCard v-for="(world,index) in worldNetworkInformation" :key="index" :name="world.name" :protocol="world.protocol" :port="world.port" :sent_per_bytes="world.sent_per_bytes" :sent_total_bytes="world.sent_total_bytes" :recv_per_bytes="world.recv_per_bytes" :recv_total_bytes="world.recv_total_bytes"></networkCard>
            </div>
        </div>
    </div>

</template>
<script>
import { io } from 'socket.io-client';
import chart from './chart.vue'
import networkCard from './networkCard.vue';
import networkChart from './networkChart.vue';
import { getCpuInfo } from '../api/server';
export default{
    name:'system',
    components:{
        chart,
        networkCard,
        networkChart,
    },
    data(){
        return{
            socketio:null,
            cpuUsage:null,
            memoryUsage:null,
            processCount:null,
            threadCount:null,
            handleCount:null,
            cpuName:null,
            cpuCount:null,
            cpuVM:null,
            cpuBaseSpeed:null,
            cpuL2:null,
            cpuL3:null,
            runTime:null,
            
            show:'cpu',
            swap_memory:null,
            total_memory:null,
            memoryUsed:null,
            reserved_memory:null,
            memory_speed:null,
            memory_FormFactor:null,
            worldNetworkInformation:[],
            total_sent_per_bytes:0,
            total_recv_per_bytes:0,
        }
    },
    methods:{
        initSocketio(){
            if(!window.socketio){
                window.socketio = io(`${import.meta.env.VITE_BASE_API}`);
            }
            this.socketio = window.socketio;
        },
        reciveCpuMessage(){
            this.socketio.on('cpu',(data)=>{
                this.handleCpuResponse(data);
            })
        },
        handleCpuResponse(data){
            this.cpuUsage = Math.floor(data.total)+'%';
            this.processCount = data.processes;
            this.threadCount = data.threads;
            this.handleCount = data.handles;
            let runtime = data.runtime; // 假设 runtime 是以秒为单位的运行时间
            let days = Math.floor(runtime / (24 * 3600));
            runtime %= 24 * 3600;
            let hours = Math.floor(runtime / 3600);
            runtime %= 3600;
            let minutes = Math.floor(runtime / 60);
            let seconds = Math.floor(runtime % 60);
            let timeStr = days + ":" + hours.toString().padStart(2, "0") + ":" + minutes.toString().padStart(2, "0") + ":" + seconds.toString().padStart(2, "0");
            this.runTime = timeStr;
            this.$refs.chartRef.totalCpu.push(data.total);
            this.$refs.chartRef.totalCpu.shift();
            this.$refs.chartRef.draw();
            for(let i=0;i<this.cpuCount;i++){
                this.$refs.cpuRefs[i].totalCpu.push(data[i]);
                this.$refs.cpuRefs[i].totalCpu.shift();
                this.$refs.cpuRefs[i].draw();
            }
        },
        reciveMemoryMessage(){
            this.socketio.on('memory',(data)=>{
                this.handleMemoryResponse(data);
            })
        },
        handleMemoryResponse(data){
            this.memoryUsed = data.used_memory.toFixed(1);
            this.memoryUsage = data.used_memory.toFixed(1) + '/' + data.total_memory + ' GB (' + Math.floor(data.memory * 100)+'%)';
            this.$refs.totalMemoryRef.totalCpu.push(data.memory * 100);
            this.$refs.totalMemoryRef.totalCpu.shift();
            this.$refs.totalMemoryRef.draw();
            this.$refs.detailMemoryRef.totalCpu.push(data.memory * 100);
            this.$refs.detailMemoryRef.totalCpu.shift();
            this.$refs.detailMemoryRef.draw();
        },
        reciveNetworkMessage(){
            this.socketio.on('network',(data)=>{
                this.handleNetworkResponse(data);
            })
        },
        handleNetworkResponse(data){
            let flag=0;
            for(let i=0;i<this.worldNetworkInformation.length;i++){
                if(this.worldNetworkInformation[i].name==data.name){
                    this.worldNetworkInformation[i].sent_per_bytes=data.sent_per_bytes;
                    this.worldNetworkInformation[i].sent_total_bytes=data.sent_total_bytes;
                    this.worldNetworkInformation[i].recv_per_bytes=data.recv_per_bytes;
                    this.worldNetworkInformation[i].recv_total_bytes=data.recv_total_bytes;
                    flag=1;
                }
            }
            if(flag==0){
                this.worldNetworkInformation.push({
                    name:data.name,
                    protocol:data.protocol,
                    port:data.port,
                    sent_per_bytes:data.sent_per_bytes,
                    sent_total_bytes:data.sent_total_bytes,
                    recv_per_bytes:data.recv_per_bytes,
                    recv_total_bytes:data.recv_total_bytes,
                })
            }
            this.total_sent_per_bytes = 0;
            this.total_recv_per_bytes = 0;
            for(let i=0;i<this.worldNetworkInformation.length;i++){
                this.total_sent_per_bytes += this.worldNetworkInformation[i].sent_per_bytes;
                this.total_recv_per_bytes += this.worldNetworkInformation[i].recv_per_bytes;
            }
            this.$refs.networkChartRef.totalCpu.push(this.total_sent_per_bytes+this.total_recv_per_bytes);
            this.$refs.networkChartRef.totalCpu.shift();
            this.$refs.networkChartRef.draw();
            this.$refs.totalNetworkRef.totalCpu.push(this.total_sent_per_bytes+this.total_recv_per_bytes);
            this.$refs.totalNetworkRef.totalCpu.shift();
            this.$refs.totalNetworkRef.draw();
        },
        formatBytes(size) {
            const units = ['B', 'KB', 'MB', 'GB', 'TB'];
            const base = 1024;
            let unitIndex = 0;
            while (size >= base && unitIndex < units.length - 1) {
                size /= base;
                unitIndex++;
            }
            return size.toFixed(1) + ' ' + units[unitIndex];
        },
        clickNavigation(name){
            const buttons = document.querySelectorAll('.system-navigation');
            buttons.forEach(button => {
                button.classList.remove('selected');
            });
            document.getElementById('total-'+name).classList.add('selected');
            this.show=name;
            this.$nextTick(()=>{
                if(name=='cpu')
                    for(let i=0;i<this.cpuCount;i++)
                        this.$refs.cpuRefs[i].chart.resize();
                else if(name=='memory')
                    this.$refs.detailMemoryRef.chart.resize();
                else    
                    this.$refs.networkChartRef.chart.resize();
            })
        },
        handleGetCpuInfo(){
            getCpuInfo().then(response=>{
                this.cpuCount = response.data.cpuCount;
                this.cpuBaseSpeed = response.data.cpuBaseSpeed + ' GHz';
                this.cpuName = response.data.cpuName;
                this.cpuVM = response.data.cpuVM;
                this.cpuL2 = response.data.cpuL2 + 'MB';
                this.cpuL3 = response.data.cpuL3 + 'MB';
                this.swap_memory = response.data.swap_memory.toFixed(1) + 'GB';
                this.total_memory = response.data.total_memory + 'GB';
                this.reserved_memory = response.data.reserved_memory + 'GB';
                this.memory_speed = response.data.memory_speed + 'MHz';
                this.memory_FormFactor = response.data.memory_FormFactor;
            })
        },
    },
    mounted(){
        this.initSocketio();
        this.handleGetCpuInfo();
        this.reciveCpuMessage();
        this.reciveMemoryMessage();
        this.reciveNetworkMessage();
    }
}
</script>
<style scoped>
#system{
    width: 100%;
    height: 100%;
    display: flex;
}
#system-left{
    height: 100%;
    width: calc(25% - 1vw);
    padding: 0 0.5vw;
    color: white;
}
.system-navigation{
    width: 100%;
    height: 8vh;
    display: flex;
    border-radius: 1vh;
    cursor: pointer;
    margin-top: 1vh;
}
.system-navigation:hover{
    background-color: rgb(20,15,10);
}
.system-navigation.selected{
    background-color: rgb(40,30,20);
}
.system-navigation-left{
    margin: 1vh 0.5vw;
    height: calc(100% - 2vh);
    width: calc(40% - 1vw);
}
.system-navigation-right{
    margin: 1vh 0;
    height: calc(100% - 2vh);
    width: 60%;
}
#system-right{
    height: calc(100% - 4vh);
    width: calc(75% - 1vw);
    margin: 2vh 1vw;
    border-left: 1px solid rgb(217,217,217);
    color: white;
    margin-left: 0vw;
}
.system-right-top1{
    display: flex;
    height: 4vh;
}
.system-right-top2{
    font-size: 4vh;
    line-height: 4vh;
}
.system-right-top3{
    font-size: 2vh;
    line-height: 2vh;
    margin-left: auto;
    display: flex;
    align-items: flex-end;
}
#system-cpu{
    margin-left: 1vw;
    width: calc(100% - 1vw);
    height: 100%;
}
#system-memory{
    margin-left: 1vw;
    width: calc(100% - 1vw);
    height: 100%;
}
#system-right-mid{
    width: 100%;
    height: 36vh;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    align-content: space-between;
}
#system-right-mid-memory{
    width: 100%;
    height: 250px;
    margin: 5px 0;
}
#system-right-bottom{
    margin-top: 1vh;
    width: 100%;
    height: 29.5vh;
    display: flex;
}
.system-right-bottom{
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.system-right-bottom-1{
    font-size: 3vh;
    color: rgb(140,140,140);
}
.system-right-bottom-2{
    font-size: 2.5vh;
}
.system-right-bottom-3{
    font-size: 2.5vh;
    margin-bottom: 1vh;
    color: white;
}
.system-right-bottom-4{
    margin-top: 10px;
    margin-right: 10px;
}
.system-right-bottom-5{
    font-size: 3vh;
    margin-bottom: 1vh;
    color: rgb(140,140,140);
}
.system-navigation-right-font1{
    font-size: 3vh;
    line-height: 3vh;
}
.system-navigation-right-font2{
    font-size: 1.5vh;
    margin-top: 1vh;
    line-height: 1.5vh;
}
#system-network{
    margin-left: 1vw;
    width: calc(100% - 1vw);
    height: 100%;
}
#system-network-formHead{
    margin-top: 1vh;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 5vh;
    width: 100%;
}
#system-right-mid{
    height: 50%;
    width: 100%;
}
.system-network-formHead{
    height: 100%;
    width: 14%;
    font-size: 2vh;
    line-height: 2vh;
}
</style>