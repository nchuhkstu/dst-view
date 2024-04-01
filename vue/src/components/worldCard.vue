<template>
    <div :id="'worldCard'+worldCardId" class="worldCard">
        <img class="worldCard-icon" :src="src">
        <div class="worldCard-message">
            <div class="worldCard-title">{{ title }}</div>
            <div class="worldCard-value">{{ value }}</div>
        </div>
    </div>    
</template>
<script>
export default {
    name:'worldCard',
    props:{
        worldCardId:Number,
        title:String,
        value:String,
        world:String,
    },
    data(){
        return{
            src:"../../image/world/"+this.world+"/"+this.title+".png",
        }
    }
}
</script>
<style scoped>
.worldCard{
    display: flex;
    height: 6vh;
    width: 100%;
    background-color: rgb(40,30,20);
    border-radius: 1vh;
}
.worldCard-icon{
    height: 5vh;
    width: 5vh;
    margin: 0.5vh 0.5vw;
}
.worldCard-message{
    height: 100%;
    width: calc(100% - 5vh - 1vw);
}
.worldCard-title{
    font-size: 1.8vh;
    line-height: 3vh;
    height: 3vh;
    display: flex;
    justify-content: center;
    color: ghostwhite;
    align-items: center;
}
.worldCard-value{
    font-size: 1.5vh;
    line-height: 3vh;
    height: 3vh;
    display: flex;
    justify-content: center;
    color: orange;
    align-items: center;
}
</style>