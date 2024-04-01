<template>
    <div id="active">
        <div id="role">
            <activeChart2></activeChart2>
        </div>
        <div id="time">
            <activeChart></activeChart>
        </div>

    </div>
</template>
<script>
import activeChart from './activeChart.vue'
import activeChart2 from './activeChart2.vue';
export default{
    name:'active',
    components:{
        activeChart,
        activeChart2,
    },
    data(){
        return{
            
        }
    },
    methods:{
        
    },
    mounted(){
        
    }
}
</script>
<style scoped>
#active{
    height: 100%;
    width: 100%;
}
#role{
    height: 50%;
    width: 100%;
}
#time{
    height: 50%;
    width: 100%;
}
</style>