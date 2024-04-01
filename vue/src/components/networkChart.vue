<template>
    <div :id="'chart-' + name" class="chart"></div>
</template>
<script>
import * as echarts from 'echarts';
export default{
    name:'networkChart',
    props:{
        name:String,
        lineColor:String,
        itemColor:String,
        borderColor:String,
        xline:Boolean,
        yline:Boolean,
    },
    data(){
        return{
            totalCpu: Array(59).fill(null).concat(0),
            chart:null,
            init:false,
        }
    },
    methods:{
        initChart(){
            var chartContainer = document.getElementById('chart-'+this.name);
            this.chart = echarts.init(chartContainer);
            chartContainer.style.borderColor = this.borderColor;
        },
        draw() {
            if(this.chart!=null){
                var option;
                option = {
                    grid:{ // 让图表占满容器
                        top:"0px",
                        left:"0px",
                        right:"0px",
                        bottom:"0px",
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        splitLine:{ 
                            show: this.xline,
                            lineStyle: {
                                width: 1, // 设置网格线的宽度
                            }
                        }
                    },
                    yAxis: {
                        type: 'value',
                        splitLine: { 
                            show: this.yline,
                            lineStyle: {
                                width: 1, // 设置网格线的宽度
                            }
                        },
                    },
                    series: [
                        {
                            data: this.totalCpu,
                            type: 'line',
                            areaStyle: {},
                            symbol: 'none',      // 设置端点样式为 'none'
                            lineStyle: {
                                width: 1, // 设置线条宽度为2像素
                                color:this.lineColor,
                            },
                            itemStyle:{
                                color:this.itemColor,
                            }
                        }
                    ],
                    animation:false,
                };
                this.chart.setOption(option);
            }
        },
    },
    mounted(){
        this.initChart();
        this.draw();
    },
    activated(){
        window.addEventListener('resize', this.chart.resize);
        if(this.init==true)
            this.chart.resize();
        this.init=true;
    },
    deactivated(){
        window.removeEventListener('resize', this.chart.resize);
    },
}
</script>
<style scoped>
.chart{
    height: 100%;
    width: 100%;
    box-sizing: border-box;
    border: 1px solid rgb(17,125,187);
    background-color: rgb(200,200,200);
}
</style>