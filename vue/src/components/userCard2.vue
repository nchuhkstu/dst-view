<template>
    <div :id="'userCard'+userid" class="userCard">
        <div class="number">
            {{ number+1 }}
        </div>
        <div class="avatar-back">
            <div class="avatar-border">
                <div class="avatar" :style="avatar"></div>
            </div>
        </div>
        <div class="user-back">
            <div class="back" :style="back"></div>
            <div class="name">{{ name }}</div>
            <div class="survivalDay">
                <div style="font-size: 3vh;line-height: 4vh; display: inline-block; font-family:Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;">{{ survival_day }}</div>
                <div style="font-size: 2vh;line-height: 4vh; display: inline-block;">天</div>
            </div>
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
    width: calc(100% - 1vw);
    height: 5vh;
    position: relative;
    margin-bottom: 1vh;
    align-items: center;
    padding: 0 0.5vw;
}
.number{
    width: 1.5vw;
    height: 5vh;
    line-height: 5vh;
    text-align: center;
    font-size: 2vh;
    color: white;
}
.avatar-back{
    height: 4vh;
    width: 4vh;
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
    height: 4vh;
    width: 4vh;
    border-radius: 50%;
    background-image: url(../../image/tab/框.png);
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
    position: relative;
}
.avatar{
    height: 4vh;
    width: 4vh;
    border-radius: 50%;
    background-size: 50% auto;
    background-repeat: no-repeat;
    background-position: center;
}
.name{
    height: 100%;
    /* display: flex; */
    line-height: 5vh;
    align-items: center;
    font-size: 2vh;
    padding-left: 0.5vw;
    color: white;
    width: calc(100% - 3vw);
    overflow: hidden;
    white-space: nowrap; /* 禁止文本换行 */
    text-overflow: ellipsis; /* 使用省略号表示被截断的文本 */
    z-index: 1;
}
.survivalDay{
    color: white;
    width: 3vw;
    text-align: end;
    padding-right: 0.5vw;
    white-space: nowrap;
    z-index: 1;
}
.user-back{
    position: absolute;
    left: calc(4vh + 2vw);
    height: 5vh;
    width: calc(100% - 4vh - 2.5vw);
    display: flex;
    align-items: center;
}
.back{
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    z-index: 0;
    background-image: url(../../image/tab/框2.png);
    /* filter: invert(10%); */
    background-size: 100% 80%;
    background-repeat: no-repeat;
    background-position: left;
}
</style>