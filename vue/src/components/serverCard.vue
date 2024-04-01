<template>
    <div id="serverCard">
        <div id="icon">

        </div>
        <div id="avatar-back">
            <div id="avatar-border">
                <div id="avatar"></div>
            </div>
        </div>
        <div id="user-back">
            <div id="server-text">[Host]</div>
            <div></div>
            <div id="ping" :style="pingImage"></div>
        </div>
    </div>
</template>
<script>
export default{
    name:'serverCard',
    props:{
        ping:String,
    },
    computed:{
        pingImage(){
            return{
                backgroundImage : "url('/image/tab/服务器ping"+this.ping+".png')"
            }
        },
    }
}
</script>
<style scoped>
#serverCard{
    display: flex;
    width: calc(100% - 3vw);
    height: 8vh;
    position: relative;
    margin-bottom: 1vh;
    margin-right: 3vw;
}
#icon{
    height: 8vh;
    width: 8vw;
}
#avatar-back{
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
#avatar-border{
    height: 8vh;
    width: 8vh;
    border-radius: 50%;
    background-image: url(../../image/tab/框.png);
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
}
#avatar{
    height: 8vh;
    width: 8vh;
    border-radius: 50%;
    background-image: url(../../image/tab/服务器.png);
    background-size: 50% auto;
    background-repeat: no-repeat;
    background-position: center;
}
#server-text{
    height: 100%;
    display: flex;
    align-items: center;
    font-size: 4vh;
    padding-left: 0.5vw;
    color: white;
    margin-left: 0.5vw;
}
#user-back{
    position: absolute;
    left: calc(8vh + 8vw);
    height: 8vh;
    width: calc(35.5vw);
    background-image: url(../../image/tab/框2.png);
    filter: invert(10%);
    background-size: 100% 90%;
    background-repeat: no-repeat;
    background-position: left;
    display: flex;
    align-items: center;
}
#ping{
    height: 4vh;
    width: 7vw;
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
    margin-left: auto;
    margin-right: 2vw;
}
</style>