<template>
    <div class="networkCard">
        <div class="item">{{name}}</div>
        <div class="item">{{protocol}}</div>
        <div class="item">{{port}}</div>
        <div class="item">{{formatBytes(sent_per_bytes)+'/s'}}</div>
        <div class="item">{{formatBytes(sent_total_bytes)}}</div>
        <div class="item">{{formatBytes(recv_per_bytes)+'/s'}}</div>
        <div class="item">{{formatBytes(recv_total_bytes)}}</div>
    </div>
</template>
<script>
export default{
    name:'networkCard',
    props:{
        name:String,
        protocol:String,
        port:String,
        sent_per_bytes:Number,
        recv_per_bytes:Number,
        sent_total_bytes:Number,
        recv_total_bytes:Number,
    },
    methods:{
        formatBytes(size) {
            const units = ['B', 'KB', 'MB', 'GB', 'TB'];
            const base = 1024;
            let unitIndex = 0;
            while (size >= base && unitIndex < units.length - 1) {
                size /= base;
                unitIndex++;
            }
            return size.toFixed(2) + ' ' + units[unitIndex];
        }
    }
}
</script>
<style scoped>
.networkCard{
    height: 5vh;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
.item{
    height: 100%;
    width: 14%;
    font-size: 2vh;
    line-height: 2vh;
}
</style>