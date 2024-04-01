<template>
    <div id="activeChart" class="chart"></div>
    <div id="activeChart-button">
        <div id="last" @click="lastDay">上一天</div>
        <div id="date">{{ ftime }}</div>
        <div id="next" @click="nextDay">下一天</div>
    </div>
</template>
<script>
import * as echarts from 'echarts';
import { io } from 'socket.io-client';
import { getActiveMessage,getCluster } from '../api/server';
export default{
    name:'activeChart',
    props:{
        name:String,
        // lineColor:String,
        // itemColor:String,
        // borderColor:String,
    },
    data(){
        return{
            
            chart:null,
            init:false,
            active:[],
            playerNum:0,
            max:null,
            
            time:new Date(),
            ftime:'',
            minTime:new Date().setHours(0,0,0,0),
            maxTime:new Date().setHours(23,59,59,999), 
        }
    },
    methods:{
        formttedTime(){
            const year = this.time.getFullYear().toString();
            const month = (this.time.getMonth() + 1).toString().padStart(2, '0');
            const day = this.time.getDate().toString().padStart(2, '0');
            this.ftime= `${year}-${month}-${day}`
        },
        nextDay(){
            this.time.setDate(this.time.getDate()+1)
            this.formttedTime();
            this.minTime=this.time.setHours(0,0,0,0)
            this.maxTime=this.time.setHours(23,59,59,999)
            this.draw();
        },
        lastDay(){
            this.time.setDate(this.time.getDate()-1)
            this.formttedTime();
            this.minTime=this.time.setHours(0,0,0,0)
            this.maxTime=this.time.setHours(23,59,59,999)
            this.draw();
        },
        initChart(){
            var chartContainer = document.getElementById('activeChart');
            this.chart = echarts.init(chartContainer);
            // chartContainer.style.borderColor = this.borderColor;
        },
        initSocketio(){
            if(!window.socketio){
                window.socketio = io(`${import.meta.env.VITE_BASE_API}`);
            }
            this.socketio = window.socketio;
        },
        reciveMessage(){
            this.socketio.on('chat',(data)=>{
                if(data.type=='join')
                    this.playerNum++;

                    console.log(data)
                    this.active.push([parseInt(new Date().getTime()),this.playerNum]);
                if(data.type=='leave')
                    this.playerNum--;
                    this.active.push([parseInt(new Date().getTime()),this.playerNum]);
                this.draw();
            })
        },
        handleGetActiveMessage(){
            getActiveMessage().then(response=>{
                for(let i=0;i<response.data.messages.length;i++){
                    if(response.data.messages[i].type=='join')
                        this.playerNum++;
                    else
                        this.playerNum--;
                    this.active.push([parseInt(response.data.messages[i].time),this.playerNum])
                }
                this.draw();
            })
        },
        handleGetCluster() {
            return new Promise((resolve) => {
                getCluster().then(response => {
                    this.max = response.data.max_players;
                    this.draw();
                    resolve(response); // 解析异步响应
                })
            });
        },
        draw() {
            if(this.chart!=null){
                var option = {
                    grid:{
                        top:"10vh",
                        left:"60vw",
                        right:"30vw",
                        bottom:"30vh",
                    },
                    xAxis: {
                        type: 'time', // 使用时间轴类型的坐标轴
                        min: this.minTime,
                        max: this.maxTime,
                        axisLabel: {
                            formatter: function (value) {
                                var date = new Date(value);
                                var hours = date.getHours();
                                var minutes = date.getMinutes();
                                var seconds = date.getSeconds();
                                return hours.toString().padStart(2, '0') + ':' + minutes.toString().padStart(2, '0') + ':' + seconds.toString().padStart(2,'0');
                            },
                        },
                        splitLine:{
                            show:false,
                        }
                    },
                    yAxis: {
                        min:0,
                        max:this.max,
                        type: 'value',
                        axisLabel: {
                            formatter: '{value} 玩家'  // 在值后面添加 "玩家" 文本
                        },
                    },
                    series: [
                        {
                            data: this.active,
                            smooth: 'true',
                            type: 'line',
                        }
                    ],
                    tooltip:{
                        trigger: 'item',
                        formatter: function(params) {
                            var date = new Date(params.data[0]);
                            var hours = date.getHours();
                            var minutes = date.getMinutes();
                            var seconds = date.getSeconds();
                            var time = hours.toString().padStart(2, '0') + ':' + minutes.toString().padStart(2, '0') + ':' + seconds.toString().padStart(2,'0');
                            return params.data[1] + '名玩家 ' + time;
                        },
                    },
                }
            };
            this.chart.setOption(option);
        }
    },
    mounted(){
        this.initSocketio();
        this.initChart();
        this.formttedTime();
        this.handleGetCluster().then(response=>{
            this.reciveMessage();
            this.handleGetActiveMessage();
        })
    },
}
</script>
<style scoped>
#activeChart-button{
    display: flex;
    height: 4vh;
    width: 100%;
    justify-content: center;
    align-items: center;
    color: rgb(200, 200, 150);
    font-size: 2vh;
}
#last{
    height: 80%;
    width: 6vw;
    background-color: rgb(0,0,0);

    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 1vh;
    cursor: pointer;
}
#last:hover{
    background-color: rgb(100,100,100);
}
#date{
    height: 80%;
    width: 10vw;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 0.5vw;
    border-radius: 1vh;
    background-color: rgb(0,0,0);
}
#next{
    height: 80%;
    width: 6vw;
    border-radius: 1vh;
    background-color: rgb(0,0,0);
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
#next:hover{
    background-color: rgb(100,100,100);
}
.chart{
    height: calc(100% - 4vh);
    width: 100%;
    box-sizing: border-box;
    /* border: 1px solid rgb(17,125,187); */
    /* background-color: rgb(200,200,200); */
}
</style>