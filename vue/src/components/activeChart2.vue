<template>
    <div id="activeChart2"></div>
</template>
<script>
import * as echarts from 'echarts';
import {getUser} from '../api/server.js'
export default {
    name:'activeChart2',
    data(){
        return{
            chart:null,
            users_role:[],
        }
    },
    methods:{
        initChart(){
            var chartContainer = document.getElementById('activeChart2');
            this.chart = echarts.init(chartContainer);
            // this.draw();
            // chartContainer.style.borderColor = this.borderColor;
        },
        draw() {
            if(this.chart!=null){
                var option = {
                    title: {
                        show:false,
                        text: '游戏角色分布图',
                        left: 'center',
                        textStyle:{
                            fontSize:20,
                            color:'white',
                            fontWeight:500,
                        }
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: function(params) {
                            return params.data.name + ' ' + params.data.value + '名玩家';
                        },
                    },
                    legend: {
                        orient: 'vertical',
                        right: '10%',
                        textStyle:{
                            fontSize:15,
                            color:'white',
                        }
                    },
                    series: [{
                        type: 'pie',
                        radius: '90%',
                        center:['50%','50%'],
                        data: this.users_role,
                        label:{
                            show:false,
                            position:'outside',
                            textStyle:{
                                fontSize:12,
                                color:'white',
                            }
                        },
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgb(0, 0, 0)'
                            }
                        }
                    }]
                };
                this.chart.setOption(option);
            }
        },
        handleGetUser(){
            getUser().then(response=>{
                for(let i=0;i<response.data.length;i++){
                    let flag=0;
                    this.users_role.forEach(function(item){
                        if(response.data[i]==item.name){
                            item.value++;
                            flag=1;
                        }
                    })
                    if(flag==0)
                        this.users_role.push({value:1,name:response.data[i]})
                }
                this.draw();
            })
        }
    },
    mounted(){
        this.initChart();
        this.handleGetUser();
    },
}
</script>
<style scoped>
#activeChart2{
    height: 100%;
    width: 100%;
    box-sizing: border-box;
}
</style>