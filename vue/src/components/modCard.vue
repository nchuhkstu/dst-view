<template>
    <div :id="'mod-'+modid" class="modCard">
        <img class="icon" :src=src>
        <div class="modCard-information">
            <div class="title">{{ title }}</div>
            <div class="content">启用</div>
        </div>
    </div>
</template>
<script>
export default {
    name:'modCard',
    props:{
        modid:String,
        title:String,
    },
    data(){
        return{
            src:import.meta.env.VITE_NGINX_API+"/images/"+this.modid+".jpg"
        }
    }
}
</script>
<style scoped>
.modCard{
    margin-bottom: 1vh;
    background-color: rgb(45,36,25);
    height: 8vh;
    width: calc(100% - 0.5vw);
    display: flex;
    border-radius: 10px;
    align-items: center;
    cursor: pointer;
}
.icon{
    margin-left: 0.5vw;
    height: 6.5vh;
    width: 6.5vh;
}
.modCard-information{
    height: 6.5vh;
    width: calc(100% - 6.5vh - 1.5vw);
    padding-left: 0.5vw;
    padding-right: 0.5vw;
}
.title{
    height: 3.5vh;
    line-height: 3.5vh;
    width: 100%;
    font-size: 2vh;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: white;
}
.content{
    height: 2.5vh;
    line-height: 2.5vh;
    width: 100%;
    font-size: 1.5vh;
    color: green;
}
</style>