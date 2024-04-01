<template>
    <div :id="'userCard'+userid" class="userCard">
        <div class="number">
            {{ number+1 }}
        </div>
        <div class="iconContainer">
            <div class="icon-back"></div>
            <div class="icon"></div>
        </div>
        <div class="avatar-back">
            <div class="avatar-border">
                <div class="avatar" :style="avatar"></div>
                <div class="connecting" v-show="connecting"></div>
            </div>
        </div>
        <div class="user-back">
            <div class="back" :style="back"></div>
            <div class="name">{{ name }}</div>
            <div class="survivalDay">
                <div style="font-size: 3vh;line-height: 8vh;  font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;">{{ survival_day }}</div>
                <div style="font-size: 2vh;line-height: 8vh;">天</div>
            </div>
            <div class="button">
                <div class="button1"></div>
                <div class="button2"></div>
            </div>
            <div class="ping" :style="pingImage"></div>
        </div>
    </div>
</template>
<script>
export default{
    name:'userCard',
    props:{
        userid:String,
        name:String,
        survival_day:Number,
        role:String,
        survival:Boolean,
        ping:String,
        number:Number,
        connecting:Boolean,
    },
    computed:{
        avatar(){
            return{
                backgroundImage : "url('/image/avatar/"+this.role+"_"+this.survival+".png')"
            }
        },
        pingImage(){
            return{
                backgroundImage : "url('/image/tab/ping"+this.ping+".png')"
            }
        },
        back(){
            if(this.number % 2!=0){
                return{
                    filter: "invert(10%)"
                }
            }
        }
    }
}
</script>
<style scoped>
.userCard{
    display: flex;
    width: 100%;
    height: 8vh;
    position: relative;
    margin-bottom: 1vh;
}
.number{
    width: calc(6vw - 6vh);
    margin-left: 1vw;
    height: 8vh;
    line-height: 8vh;
    text-align: center;
    font-size: 2.5vh;
    color: white;
    display: flex;
    justify-content: center;
}
.iconContainer{
    height: 8vh;
    width: 8vh;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1;
}
.icon-back{
    height: 5vh;
    width: 5vh;
    position: absolute;
    z-index: 1;
    background-image: url(../../image/tab/头像边框.png);
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
}
.icon{
    height: 4.5vh;
    width: 4.5vh;
    background-image: url(../../image/tab/默认头像.png);
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 1;
}
.avatar-back{
    height: 8vh;
    width: 8vh;
    border-radius: 50%;
    background-image: url(../../image/tab/背景.png);
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
    display: flex;
    justify-content: center;
    align-items: center;
}
.avatar-border{
    height: 8vh;
    width: 8vh;
    border-radius: 50%;
    background-image: url(../../image/tab/框.png);
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
    position: relative;
}
.avatar{
    height: 8vh;
    width: 8vh;
    border-radius: 50%;
    background-image: url(../../image/tab/服务器.png);
    background-size: 50% auto;
    background-repeat: no-repeat;
    background-position: center;
}
.connecting{
    position: absolute;
    top: 0;
    left: 0;
    height: 8vh;
    width: 8vh;
    border-radius: 50%;
    background-size: 50% auto;
    background-repeat: no-repeat;
    background-position: center;
    background-image: url('../../image/avatar/connecting.png');
    animation: spin 2.5s linear infinite;
}
@keyframes spin {
    0% {
        transform: rotate(0deg);
    }
    25%{
        transform: rotate(-360deg);
    }
    50% {
        transform: rotate(-360deg);
    }
    75%{
        transform: rotate(-720deg);
    }
    100% {
        transform: rotate(-720deg);
    }
}
.name{
    height: 100%;
    /* display: flex; */
    line-height: 8vh;
    align-items: center;
    font-size: 3vh;
    padding-left: 0.5vw;
    color: white;
    margin-left: 0.5vw;
    width: 12vw; /* 容器的宽度，根据你的需要进行调整 */
    overflow: hidden;
    white-space: nowrap; /* 禁止文本换行 */
    text-overflow: ellipsis; /* 使用省略号表示被截断的文本 */
    z-index: 1;
}
.survivalDay{
    color: white;
    margin-left: 2vw;
    width: 6vw;
    white-space: nowrap;
    line-height: 8vh;
    height: 8vh;
    display: flex;
    align-items: center;
    z-index: 1;
}
.button{
    display: flex;
    height: 6vh;
    z-index: 1;
}
.button1{
    height: 6vh;
    width: 6vh;
    background-image: url(../../image/tab/个人链接.png);
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
}
.button2{
    height: 6vh;
    width: 6vh;
    background-image: url(../../image/tab/详细.png);
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
}
.user-back{
    position: absolute;
    left: calc(8vw + 8vh);
    height: 8vh;
    width: calc(35.5vw);
    display: flex;
    align-items: center;
}
.back{
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: 1;
    background-image: url(../../image/tab/框2.png);
    /* filter: invert(10%); */
    background-size: 100% 90%;
    background-repeat: no-repeat;
    background-position: left;
}
.ping{
    height: 4vh;
    width: 6vw;
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
    margin-left: auto;
    margin-right: 2vw;
    z-index: 1;
}
</style>