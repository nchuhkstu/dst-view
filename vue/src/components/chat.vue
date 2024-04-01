<template>
    <div id="fixed-button" @click="clickFixed"></div>
    <div v-show="this.newmessageNum!=0" id="bottom-button" @click="goBottom">{{ newmessageNum + '↓' }}</div>
    <div id="chat">
        <div id="message-container">
            <chatCard v-for="(message, index) in messages" :key="index" :last_message_time="getLastMessageTime(index)" :message="message.message" :type="message.type" :time="message.time"></chatCard>
        </div>
    </div>
</template>
<script>
import { io } from 'socket.io-client';
import chatCard from './chatCard.vue'
import {getMessage} from '../api/server.js'
export default{
    name:'chat',
    components:{
        chatCard,
    },
    data(){
        return{
            socketio:null,
            messages:[],
            page_size:25,
            currentPage:1,
            total_page:null,
            time:new Date().getTime(),
            loadingNextPage:false,
            reviewHistory:false,
            newmessageNum:0,
            fixed:true,
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
            this.socketio.on('chat',(data)=>{
                this.handleResponse(data);
                if(this.reviewHistory==true)
                    this.newmessageNum++;
                if(this.fixed==true)
                    document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight;
            })
        },
        clickFixed(){
            this.fixed=!this.fixed;
            if(this.fixed==true)
                document.getElementById("fixed-button").style.backgroundImage = "url('../../image/ui/Fixed.png')";
            else
                document.getElementById("fixed-button").style.backgroundImage = "url('../../image/ui/notFixed.png')";
        },
        goBottom(){
            this.newmessageNum=0;
            document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight;
            this.reviewHistory=false;
        },
        handleResponse(data){
            this.messages.push({
                message:data.value,
                type:data.type,
                time:new Date().getTime(),
            })
        },
        getLastMessageTime(index) {
            if (index > 0) {
                return this.messages[index - 1].time;
            } else {
                return null; // 或者设置默认值
            }
        },
        findMessageByPage(){
            const height1 = document.getElementById("message-container").clientHeight;
            return new Promise((resolve,reject)=>{
                getMessage(this.page_size,this.currentPage,this.time).then(response=>{
                    this.total_page = Math.floor(response.data.total/this.page_size)+1;
                    for(let i=0;i<response.data.messages.length;i++){
                        this.messages.unshift({
                            message:response.data.messages[i].value,
                            type:response.data.messages[i].type,
                            time:parseInt(response.data.messages[i].time),
                        })
                    }
                    resolve();
                })
                .catch((error)=>{
                    reject();
                })
                .finally(()=>{
                    const height2 = document.getElementById("message-container").clientHeight;
                    document.getElementById("chat").scrollTop = (height2-height1)/height2 *document.getElementById("chat").scrollHeight;
                })
            })
        },
        checkScroll() {
            const element = document.getElementById("chat");
            const scrollThreshold = 0; // 滚动到顶部的阈值
            const position = (element.clientHeight + element.scrollTop)/element.scrollHeight;
            if(position<0.95)
                this.reviewHistory=true;
            if (element.scrollTop <= element.clientHeight * scrollThreshold && this.loadingNextPage === false) {
                this.nextPage();
            }
        },
        nextPage(){
            if(this.currentPage<this.total_page&&!this.loadingNextPage){
                this.loadingNextPage = true;
                this.currentPage++;
                this.findMessageByPage().then(()=>{
                    this.loadingNextPage = false;
                });
            }
        },
    },
    mounted(){

        this.initSocketio();
        this.reciveMessage();
        this.findMessageByPage().then(() => {
            document.getElementById("chat").scrollTop = document.getElementById("chat").scrollHeight;
        });
        document.getElementById("chat").addEventListener("scroll", this.checkScroll);
    }
}
</script>
<style scoped>
#chat{
    width: 100%;
    height: 100%;
    overflow-y: auto;
}
#chat::-webkit-scrollbar {
  width: 1vw;
}
#chat::-webkit-scrollbar-track {
    background-image: url('../../image/scroll/scrollbar_bar.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: top;
}
#chat::-webkit-scrollbar-thumb {
    background-image: url('../../image/scroll/scrollbar_handle.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: top;
}
#message-container{
    width: calc(100% - 30px);
    margin: 0 10px;
    min-height: 100%;
}
#bottom-button{
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 2vh;
    bottom: 8vh;
    right: 1.5vw;
    height: 4vh;
    width: 5vw;
    border-radius: 3vh;
    background-color: rgb(140,140,140);
    color: rgb(30,30,30);
    cursor: pointer;
}
#fixed-button{
    position: absolute;
    bottom: 8vh;
    right: 7vw;
    height: 4vh;
    width: 4vh;
    color: rgb(30,30,30);
    background-color: rgb(140,140,140);
    border-radius: 50%;
    background-image: url('../../image/ui/Fixed.png');
    background-position: center;
    background-size: 80% auto;
    background-repeat: no-repeat;
    cursor: pointer;
}
</style>