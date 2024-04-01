<template>
    <div id="user">
        <div id="container">
            <div id="back"></div>
            <div id="userContainer">
                <div id="world-information">{{ users.length }}/{{ max_players }}</div>
                <serverCard ping="1"></serverCard>
                <div id="container2">
                    <userCard v-for="(user,index) in users" v-bind:key="index" :name="user.name" :survival_day="user.survival_day" :role="user.role" :survival=user.live ping="1" :number="index" :connecting="user.connecting" ></userCard>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import { io } from 'socket.io-client';
import userCard from './userCard.vue';
import serverCard from './serverCard.vue';
export default{
    name:'user',
    components:{
        userCard,
        serverCard,
    },
    props:{
        max_players:String,
    },
    data(){
        return{
            users:[],
            socketio:null,
        }
    },
    methods:{
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
                if(data[i].online==true){
                    this.users.push({
                        name:data[i].name,
                        survival_day:data[i].survival_day,
                        online:data[i].online,
                        live:data[i].live,
                        role:data[i].role,
                        connecting:data[i].connecting,
                    })
                }
            }
        }
    },
    mounted(){
        this.initSocketio();
        this.reciveMessage();
    }
}
</script>
<style scoped>
#user{
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
}
#container{
    height: 95%;
    width: 100%;
    position: relative;
    display: flex;
    justify-content: center;
}
#back{
    height: 100%;
    width: 100%;
    top: 0;
    left: 0;
    background-image: url(../../image/tab/容器.png);
    filter: brightness(0.7);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    z-index: 0;
    position: absolute;
}
#userContainer{
    margin: 9vh 0;
    height: calc(100% - 18vh);
    /* overflow: hidden; */
    width: 85%;
    z-index: 1;
}
#world-information{
    line-height: 2vh;
    text-align: end;
    margin-right: 3vw;
    color: white;
    height: 2vh;
}
#container2{
    width: 100%;
    height: calc(100% - 10vh);
    overflow-y: auto;
    z-index: 1;
}
#container2::-webkit-scrollbar {
  width: 3vw; /* 滚动条宽度 */
}
/* 滚动条轨道上按钮样式 */
#container2::-webkit-scrollbar-button:start {
    background-image: url('../../image/tab/tab上.png'); /* 背景图片路径 */
    background-size: 100% 50%;
    background-repeat: no-repeat;
    background-position: center;
    height: 6vh; /* 上按钮高度 */
}

/* 滚动条轨道下按钮样式 */
#container2::-webkit-scrollbar-button:end {
    background-image: url('../../image/tab/tab下.png'); /* 背景图片路径 */
    background-size: 100% 50%;
    background-repeat: no-repeat;
    background-position: bottom;
    height: 6vh;
}

/* 设置滚动条轨道的背景颜色 */
#container2::-webkit-scrollbar-track {
    background-image: url('../../image/tab/tab界面滑轨.png'); /* 背景图片路径 */
    background-size: 40% 100%;
    background-repeat: no-repeat;
    background-position: center;
}

/* 设置滚动条滑块的背景颜色 */
#container2::-webkit-scrollbar-thumb {
    background-image: url('../../image/tab/tab滑钮.png');
    background-size: 100% auto;
    background-repeat: no-repeat;
    height: 50px;
    /* background-position: center; */
}
#container2::-webkit-scrollbar-thumb:vertical {
  height: 10px; /* 竖直滚动条中滑块的高度 */
}
</style>