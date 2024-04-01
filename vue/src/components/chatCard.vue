<template>
    <div class="chatCard">
        <div class="message">
            <div class="time">{{ formatTime }}</div>
            <div class="content" :style="{color:messageType}">{{ message }}</div>
        </div>
    </div>
</template>
<script>
export default{
    name:'chatCard',
    data(){
        return{
            
        }
    },
    computed:{
        formatTime() {
            const date = new Date(this.time);
            const formattedMonth = date.getMonth();
            const formattedDay = date.getDate();
            const formattedHours = String(date.getHours()).padStart(2, '0');
            const formattedMinutes = String(date.getMinutes()).padStart(2, '0');
            if(this.last_message_time!=null&&new Date(this.last_message_time).getDate()!=new Date(this.time).getDate()||this.last_message_time==null)
                return `${formattedMonth}-${formattedDay} ${formattedHours}:${formattedMinutes}`;
            if(this.last_message_time!=null&&this.time - this.last_message_time < 1000*60)
                return null;
            return `${formattedHours}:${formattedMinutes}`;
        },
        messageType(){
            if(this.type=='join')
                return '#94d6da';
            else if(this.type=='leave')
                return '#ed1941';
            else if(this.type=='say')
                return 'white';
            else if(this.type=='death')
                return 'yellow';
            else if(this.type=='resurrect')
                return '#f15a22';
            else
                return 'gray';
        }
    },
    props:{
        message:String,
        type:String,
        time:Number,
        last_message_time:Number,
    },
    methods:{

    },
    mounted(){

    }
}
</script>
<style scoped>
.chatCard{
    width: 100%;
    margin-top: 1.5vh;
    margin-bottom: 2vh;
}
.message{
    width: 100%;
}
.time{
    width: 100%;
    font-size: 1vh;
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
}
.content{
    width: 100%;
    font-size: 2vh;
    color: white;
}
</style>