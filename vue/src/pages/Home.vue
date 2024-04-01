<template>
    <div id="home">
        <div id="back"></div>
        <div id="left">
            <div id="logo"></div>
            <div id="rank-container">
                <div id="rank">生存排行榜</div>
                <div id="user-container">
                    <userCard2 v-for="(user,index) in users" v-bind:key="index" :name="user.name" :survival_day="user.survival_day" :role="user.role" :survival=user.live ping="1" :number="index" ></userCard2>
                </div>
            </div>
        </div>
        <div id="mid">
            <div id="mid-top">
                <div id="cluster">
                    <div id="cluster-top">
                        <div class="cluster-message">【房间名】:{{ cluster.cluster_name }}</div>
                        <div class="cluster-message">【直连代码】:{{ cluster.ip }}</div>
                    </div>
                    <div id="cluster-bottom">
                        <div class="cluster-message">【模式】:{{ computed_gameMode }}</div>
                        <div class="cluster-message">【密码】:{{ computed_password }}</div>
                        <div class="cluster-message">【描述】:{{ cluster.cluster_description }}</div>
                    </div>
                </div>
            </div>
            <div id="mid-bottom">
                <div id="navigation">
                    <div id="navigation-back"></div>
                    <div class="navigation-border">
                        <div class="navigation selected" @click="changeComponents('user')" id="user-button">在线玩家</div>
                    </div>
                    <div class="navigation-border">
                        <div class="navigation" @click="changeComponents('active')" id="active-button">活跃信息</div>
                    </div>
                    <div class="navigation-border">
                        <div class="navigation" @click="changeComponents('mod')" id="mod-button">模组信息</div>
                    </div>
                    <div class="navigation-border">
                        <div class="navigation" @click="changeComponents('world')" id="world-button">世界信息</div>
                    </div>
                    <div class="navigation-border">
                        <div class="navigation" @click="changeComponents('system')" id="system-button">系统信息</div>
                    </div>
                </div>
                <div id="components-container">
                    <keep-alive class="componets">
                        <component :is="component" :key="component" :max_players="cluster.max_players"></component>
                    </keep-alive>
                </div>
            </div>
        </div>
        <div id="right">
            <chat></chat>
        </div>
    </div>
</template>
<script>
import active from '../components/active.vue';
import world from '../components/world.vue';
import system from '../components/system.vue';
import user from '../components/user.vue';
import mod from '../components/mod.vue';
import { io } from 'socket.io-client';
import { getCluster } from '../api/server';
import userCard2 from '../components/userCard.vue';
import chat from '../components/chat.vue';
export default{
    components:{
        system,
        user,
        mod,
        world,
        userCard2,
        chat,
        active,
    },
    data(){
        return{
            component:"user",
            users:[],
            socketio:null,
            cluster:{
                cluster_name:null,
                cluster_description:null,
                cluster_password:null,
                max_players:null,
                game_mode:null,
                ip:'c_connect("117.41.187.65",10999)',
            }
        }
    },
    computed:{
        computed_gameMode(){
            if(this.cluster.game_mode=='survival'){
                return '生存';
            }
        },
        computed_password(){
            if(this.cluster.cluster_password==''||this.cluster.cluster_password==' '){
                return '无'
            }
            return this.cluster.cluster_password;
        }
    },
    methods:{
        changeComponents(name){
            this.component = name;
            document.querySelectorAll('.navigation').forEach(element=>{
                element.classList.remove('selected');
            })
            document.getElementById(name+'-button').classList.add('selected');
        },
        initSocketio(){
            if(!window.socketio){
                window.socketio = io(`${import.meta.env.VITE_BASE_API}`);
            }
            this.socketio = window.socketio;
        },
        reciveMessage(){
            this.socketio.on('users',(data)=>{
                this.handleResponse(data);
            })
        },
        handleResponse(data){
            this.users = [];
            for(let i=0;i<data.length;i++){
                this.users.push({
                    name:data[i].name,
                    survival_day:data[i].survival_day,
                    online:data[i].online,
                    live:data[i].live,
                    role:data[i].role,
                })
            }
            this.users.sort((a, b) => b.survival_day - a.survival_day);
        },
        handleGetCluster(){
            getCluster().then(response=>{
                this.cluster.cluster_name = response.data.cluster_name;
                this.cluster.cluster_description = response.data.cluster_description;
                this.cluster.cluster_password = response.data.cluster_password;
                this.cluster.max_players = response.data.max_players;
                this.cluster.game_mode = response.data.game_mode;
            })
        }
    },
    mounted(){
        this.initSocketio();
        this.reciveMessage();
        this.handleGetCluster();
    }
}
</script>
<style scoped>
#home{
    height: 100%;
    width: 100%;
    display: flex;
    position: relative;
}
#back{
    height: 100%;
    width: 100%;
    content: "";
    left: 0;
    top: 0;
    z-index: -2;
    position: absolute;
    background-image: url(../../image/tab/mod背景.png);
    background-size: cover;
    background-repeat: no-repeat;
    background-position: bottom;
}
#left{
    width: calc(15% - 2vw);
    margin: auto 1vw;
    margin-top: 3vh;
    margin-bottom: 3vh;
    height: calc(100% - 6vh);
}
#logo{
    height: 10vh;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(68,54,39,0.7);
    background-image: url('../../image/logo/logo2.png');
    background-size: 90% auto;
    background-position: center;
    color: gold;
    background-repeat: no-repeat;
}
#rank-container{
    margin-top: 1.5vh;
    width: 100%;
    height: calc(100% - 11.5vh);
    background-color: rgba(68,54,39,0.7);
}
#rank{
    width: 100%;
    height: 5vh;
    margin-top: 1vh;
    line-height: 5vh;
    font-size: 3.5vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: rgb(244,225,178);
}
#user-container{
    height: calc(100% - 5vh);
    width: 100%;
    overflow-y:auto;
}
#user-container::-webkit-scrollbar {
  width: 0.5vw;
}
#user-container::-webkit-scrollbar-track {
    background-image: url('../../image/scroll/scrollbar_bar.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: top;
}
#user-container::-webkit-scrollbar-thumb {
    background-image: url('../../image/scroll/scrollbar_handle.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: top;
}
#mid{
    margin: auto 0px;
    margin-top: 3vh;
    margin-bottom: 3vh;
    height: calc(100% - 6vh);
    width: 60%;
}
#mid-top{
    width: 100%;
    height: 10vh;
    background-color: rgba(68,54,39,0.7);
    color: rgb(244,225,178);
}
#cluster{
    margin: 0px 1vw;
    height: 100%;
    font-size: 20px;
    width: calc(100% - 2vw);
}
.cluster-message{
    height: 100%;
    display: flex;
    align-items: center;
    margin-right: 20px;
    font-size: 2vh;
    line-height: 2vh;
}
#cluster-top{
    display: flex;
    width: 100%;
    height: 50%;
}
#cluster-bottom{
    display: flex;
    width: 100%;
    height: 50%;
}
#mid-bottom{
    width: 100%;
    height: calc(100% - 11.5vh);
    margin-top: 1.5vh;
    /* background-color:blue; */
}
#navigation{
    width: 100%;
    height: 5vh;
    background-color: rgba(58,44,29,0.9);
    display: flex;
    position: relative;
    justify-content: center;
}
#navigation-back{
    height: 100%;
    width: 100%;
    left: 0;
    bottom: 0;
    z-index: 10;
    position: absolute;
    background-image: url(../../image/tab/分割线上.png);
    background-size: 100% 100%;
    background-position: top;
    filter: matrix(1.457, 0, 0, 0, 1.151, 0, 0, 0, 0.652, 0, 0, 0, 0, 0, 1, 0);
    background-repeat: no-repeat;
}
.navigation{
    height: calc(60%);
    width: 100%;
    display: flex;
    align-items: center;
    background-image: url('../../image/navigation/导航背景1.png'); /* 背景图片路径 */
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: bottom;
    position: absolute;
    left: 0px;
    bottom: 30%;
    z-index: 0;
    justify-content: center;
    color: rgb(200,200,150);
    cursor: pointer;
}
.navigation.selected{
    background-image: url('../../image/navigation/导航背景2.png'); /* 背景图片路径 */
    color: black;
}
.navigation.selected:hover {
    color: initial;
}
.navigation:hover{
    color: orange;
}
.navigation-border{
    height: 100%;
    width: 8vw;
    z-index: 100;
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
    margin-right: 10px;
    margin-left: 10px;
    font-size: 2vh;

    position: relative;
}
.navigation-border:hover{
    background-image: url('../../image/navigation/导航背景装饰.png'); /* 背景图片路径 */
}
.components{
    width: 100%;
    height: 100%;
}
#components-container{
    width: 100%;
    background-color: rgba(68,54,39,0.7);
    height: calc(100% - 5vh);
    /* background-color: blueviolet; */
}
#right{
    width: calc(25% - 2vw);
    margin: auto 1vw;
    margin-top: 3vh;
    margin-bottom: 3vh;
    height: calc(100% - 6vh);
    background-color: rgba(68,54,39,0.7);
    position: relative;;
}
</style>