<template>
    <div id="mod" v-if="mods">
        <div id="mods">
            <div id="navigation">
                <div id="classification"></div>
                <div id="search">
                    <input id="search-input" placeholder="搜索" v-model="searchText">
                </div>
            </div>
            <div id="modContainer">
                <modCard v-for="(mod,index) in filteredMods" v-bind:key="index" :title="mod.title" :modid="mod.modid" @click="select(index)"></modCard>
            </div>
        </div>
        <div id="mod-information">
            <div id="information-top">
                <img id="icon" :src="this.api + '/images/'+mods[number].modid+'.jpg'">
                <div id="top-right">
                    <div id="title">{{ mods[number].title }}</div>
                    <div id="author">作者：{{ mods[number].author }}</div>
                    <div id="size">文件大小：{{ mods[number].size }}</div>
                    <div id="time">
                        <div id="publishiTime">发布时间：{{ mods[number].push_time }}</div>
                        <div id="updateTime">更新时间：{{ mods[number].update_time }}</div>
                    </div>
                </div>
            </div>
            <div id="information-bottom" v-html="mods[number].description" class="html"></div>
        </div>
    </div>
</template>
<script>
import modCard from './modCard.vue';
import {getMod} from '../api/server.js'
export default{
    name:'mod',
    components:{
        modCard,
    },
    data(){
        return{
            mods:null,
            number:0,
            searchText: '',
            api:import.meta.env.VITE_NGINX_API,
        }
    },
    methods:{
        handleGetMod(){
            getMod().then(response=>{
                this.mods = response.data;
            })
        },
        select(number){
            this.number = number;
        }
    },
    computed: {
        filteredMods() {
            if (!this.mods) 
                return [];
            const filtered = this.mods.filter(mod => {
                return mod.title.toLowerCase().includes(this.searchText.toLowerCase());
            });
            return filtered;
        },
    },
    mounted(){
        this.handleGetMod();
    }
}
</script>
<style scoped>
#mod{
    height: 100%;
    width: 100%;
    display: flex;
}
#mods{
    height: 100%;
    width: 29%;
    margin-left: 1%;
}
#navigation{
    width: 100%;
    height: 5vh;
    display: flex;
    align-items: center
}
#classification{
    height: 4vh;
    width: 0px;
}
#search{
    height: 4vh;
    width: 100%;
    background-image: url(../../image/tab/搜索框1.png);
    background-size: 100% 80%;
    background-repeat: no-repeat;
    background-position: center;
    display: flex;
    justify-content: center;
    align-items: center;
}
#search:hover{
    background-image: url(../../image/tab/搜索框2.png);
}
#search-input{
    height: 3.5vh;
    width: calc(100% - 0.5vw);
    background-color: transparent;
    border: none;
    outline: none;
    padding: 0.5vw;
    font-size: 1.5vh;
}
#modContainer{
    width: 100%;
    height: calc(100% - 5vh);
    overflow-y: scroll;
    overflow-x: hidden;
}
#modContainer::-webkit-scrollbar{
    width: 15px;
    margin-left: 0.5vw;
}
#modContainer::-webkit-scrollbar-track{
    background-image: url('../../image/tab/滑轨.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
}
#modContainer::-webkit-scrollbar-thumb{
    height: 10px;
    background-image: url('../../image/navigation/滑轨按钮.png');
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: top;
}
#modContainer::-webkit-scrollbar-button:start{
    height: 30px;
    background-image: url('../../image/navigation/滑轨按钮上.png');
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
}
#modContainer::-webkit-scrollbar-button:end{
    height: 30px;
    background-image: url('../../image/navigation/滑轨按钮下.png');
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
}
#mod-information{
    margin-top: 1vh;
    margin-left: 0.5vw;
    height: calc(100% - 1vh);
    width: calc(70% - 0.5vw);
    color: white;
}
#information-top{
    width: 100%;
    height: 15vh;
    display: flex;
}
#icon{
    height: 15vh;
    width: 15vh;
}
#top-right{
    height: 15vh;
    width: calc(100% - 15vh - 0.5vw);
    margin-left: 0.5vw;
}
#title{
    height: 5vh;
    font-size: 4vh;
    line-height: 5vh;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
#author{
    height: 4vh;
    font-size: 2vh;
    line-height: 4vh;
    color:orange
}
#size{
    height: 3vh;
    font-size: 2vh;
    line-height: 3vh;
}
#time{
    display: flex;
    font-size: 1.5vh;
    height: 3vh;
    line-height: 3vh; 
}
#publishTime{
}
#updateTime{
    margin-left: 0.5vw;
}
#information-bottom{
    width: 100%;
    height: calc(100% - 16vh);
    margin-top: 1vh;
    /* white-space: wrap; */
    overflow-y:scroll;
    overflow-x: hidden;
    text-overflow: ellipsis;
    font-size: 2vh;
    color: white;
}
#information-bottom::-webkit-scrollbar {
  width: 0px;
}
</style>
<style>
a{
    color: white;
    text-decoration: none;
    cursor: pointer;
    font-size: 14px;
}
a:hover{
    color:#54a5d4;
}
#information-bottom img {
  max-width: 100%;
  object-fit: contain; /* 或者 object-fit: cover; */
}
</style>