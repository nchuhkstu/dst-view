<template>
    <div id="world">
        <div class="world-navigation">
            <div class="navigation-border">
                <div class="navigation selected2" id="forest-button" @click="changeWorld('forest')">森林</div>
            </div>
            <div class="navigation-border">
                <div class="navigation" id="cave-button" @click="changeWorld('cave')">洞穴</div>
            </div>
        </div>
        <div class="line"><div class="line-1"></div><div class="line-2"></div><div class="line-3"></div></div>
        <div class="world-navigation">
            <div class="navigation-border">
                <div class="navigation selected3" id="rule-button" @click="changeRule('rule')">世界规则</div>
            </div>
            <div class="navigation-border">
                <div class="navigation" id="generate-button" @click="changeRule('generate')">世界生成</div>
            </div>
        </div>
        <div class="line"><div class="line-1"></div><div class="line-2"></div><div class="line-3"></div></div>
        <div id="world-set-scorllContainer">
            <div id="world-set">
                <template v-for="(category, label) in data" :key="label">
                    <div class="label">{{ label }}</div>
                    <template v-for="(value, key) in category" :key="key">
                        <worldCard :title="key" :value="CE(value)" class="worldCard" :world="world"></worldCard>
                    </template>
                </template>
            </div>
        </div>
    </div>
</template>
<script>
import worldCard from './worldCard.vue';
import { getWorld,getWorld2 } from '../api/server';
export default {
    name:"world",
    components:{
        worldCard,
    },
    computed:{
        data(){
            if(this.world=='forest'){
                if(this.rule=='rule'){
                    return this.forest_rule;
                }
                return this.forest_generate
            }
            else{
                if(this.rule=='rule'){
                    return this.cave_rule;
                }
                return this.cave_generate;
            }
        },
    },
    data(){
        return{
            world:'forest',
            rule:'rule',
            forest_rule:{
                全局:{活动:"自动",秋:"默认",冬:"默认",春:"默认",夏:"默认",昼夜选项:"默认",出生模式:"绚丽之门",冒险家死亡:"变鬼魂",在绚丽之门复活:"禁用",鬼魂理智值惩罚:"启用",死亡重置倒计时:"默认",皮弗娄牛交配频率:"默认",坎普斯:"默认",},
                活动:{盛夏鸦年华:"默认",万圣夜:"默认",冬季盛宴:"默认",火鸡之年:"默认",座狼之年:"默认",猪王之年:"默认",胡萝卜鼠之年:"默认",皮弗娄牛之年:"默认",浣猫之年:"默认",兔人之年:"默认",龙蝇之年:"默认",},
                冒险家:{额外起始资源:"第10天后",季节起始物品:"默认",防骚扰出生保护:"自动检测",离开游戏后物品掉落:"默认",血量上限惩罚:"默认",收到的伤害:"默认",温度伤害:"默认",饥饿伤害:"默认",黑暗伤害:"默认",理智怪兽:"默认",启蒙怪兽:"默认",},
                世界:{猎犬袭击:"默认",冰猎犬群:"默认",火猎犬群:"默认",森林石化:"默认",流星频率:"默认",狩猎:"默认",荒野裂隙开启:"默认",荒野裂隙频率:"默认",追猎惊喜:"默认",野火:"默认",闪电:"默认",雨:"默认",青蛙雨:"默认",},
                资源再生:{再生速度:"默认",仙人掌:"默认",基础资源:"默认",多枝树:"默认",常青树:"默认",月树:"默认",桦栗树:"默认",棕榈松果树:"默认",盐堆:"默认",胡萝卜:"默认",芦苇:"默认",花:"默认",},
                非自然传送门资源:{传送频率:"默认",发光蟹:"默认",棕榈松果树芽:"默认",火药猴:"默认",猴尾草:"默认",香蕉丛:"默认",},
                生物:{一角鲸:"默认",企鸥:"默认",兔人:"默认",兔子:"默认",浣猫:"默认",火鸡:"默认",猪:"默认",草壁虎转化:"默认",蜜蜂:"默认",蝴蝶:"默认",鱼群:"默认",鸟:"默认",鼹鼠:"默认",龙虾:"默认",},
                敌对生物:{恐怖猎犬:"默认",月亮码头海盗:"默认",月石企鸥:"默认",杀人蜂:"默认",海象:"默认",猎犬:"默认",破碎蜘蛛:"默认",蚊子:"默认",蜘蛛:"默认",蜘蛛战士:"默认",蝙蝠:"默认",青蛙:"默认",食人花:"默认",饼干切割机:"默认",鱼人:"默认",鱿鱼:"默认",鲨鱼:"默认",},
                巨兽:{克劳斯:"默认",帝王蟹:"默认",恐怖之眼:"默认",果蝇王:"默认",树精守卫:"默认",毒桦栗树:"默认",熊獾:"默认",独眼巨鹿:"默认",蚁狮贡品:"默认",蜂王:"默认",蜘蛛女王:"默认",邪天翁:"默认",麋鹿鹅:"默认",龙蝇:"默认",}
            },
            forest_generate:{
                全局:{起始季节:"秋"},
                世界:{生物群落:"联机版",出生点:"默认",世界大小:"中",分支:"默认",环形:"默认",道路:"默认",试金石:"默认",失败的冒险家:"默认",开始资源多样化:"经典",天体裂隙:"默认",盒中泰拉:"默认",舞台剧:"默认"},
                资源:{仙人掌:"默认",公牛海带茎:"默认",尖刺灌木:"默认",巨石:"默认",月亮树苗:"默认",月亮石:"默认",月树:"默认",树苗:"默认",所有树:"默认",棕榈松果树:"默认",池塘:"默认",流星区域:"默认",浆果丛:"默认",海岸公牛海带:"默认",海星:"默认",海蚀柱:"默认",温泉:"默认",燧石:"默认",石果灌木丛:"默认",胡萝卜:"默认",芦苇:"默认",花和邪恶花:"默认",草:"默认",蘑菇:"默认",迷你冰川:"默认",风滚草:"默认",},
                生物以及刷新点:{伏特羊:"默认",兔洞:"默认",沙拉蝾螈:"默认",猪屋:"默认",皮弗娄牛:"默认",秃鹫:"默认",空心树桩:"默认",胡萝卜鼠:"默认",蜜蜂蜂窝:"默认",鱼群:"默认",鼹鼠丘:"默认",龙虾窝:"默认"},
                敌对生物以及刷新点:{发条装置:"默认",杀人蜂蜂窝:"默认",海草:"默认",海象营地:"默认",漏雨的小屋:"默认",猎犬丘:"默认",破碎蜘蛛洞:"默认",蜘蛛巢:"默认",触手:"默认",高脚鸟:"默认"},
            },
            cave_rule:{
                世界:{地震:"默认",洞穴蠕虫攻击:"默认",荒野裂隙开启:"默认",荒野裂隙频率:"默认",远古大门:"默认",雨:"默认"},
                资源再生:{再生速度:"默认",光虫花:"默认",月亮蘑菇树:"默认",荧光花:"默认",蘑菇树:"默认"},
                生物:{兔人:"默认",尘蛾:"默认",猪:"默认",球状光虫:"默认",石虾:"默认",穴居猴:"默认",草壁虎转化:"默认",蘑菇地精:"默认",蛞蝓龟:"默认",蜗牛龟:"默认",鼹鼠:"默认"},
                敌对生物:{喷射蜘蛛:"默认",洞穴蜘蛛:"默认",穴居悬蛛:"默认",蜘蛛:"默认",蜘蛛战士:"默认",蝙蝠:"默认",裸鼹蝠:"默认",遗迹梦魇:"默认",鱼人:"默认"},
                巨兽:{噩梦猪人:"默认",果蝇王:"默认",树精守卫:"默认",毒菌蟾蜍:"默认",蜘蛛女王:"默认"},
            },
            cave_generate:{
                世界:{生物群落:"地下",出生点:"洞穴",世界大小:"默认",分支:"默认",环形:"默认",试金石:"默认",失败的冒险家:"默认",洞穴光照:"默认",开始资源多样化:"默认"},
                资源:{发光浆果:"默认",尖刺灌木:"默认",巨石:"默认",树苗:"默认",所有树:"默认",池塘:"默认",洞穴蕨类:"默认",浆果丛:"默认",燧石:"默认",芦苇:"默认",苔藓:"默认",草:"默认",荧光花:"默认",蘑菇:"默认",蘑菇树:"默认",香蕉:"默认"},
                生物以及刷新点:{兔屋:"默认",啜食者:"默认",石虾:"默认",穴居猴桶:"默认",蛞蝓龟窝:"默认"},
                敌对生物以及刷新点:{发条装置:"默认",梦魇裂隙:"默认",洞穴蠕虫:"默认",蛛网岩:"默认",蜘蛛巢:"默认",蝙蝠:"默认",触手:"默认"},
            }
        }
    },
    methods:{
        CE(value){
            if(value=='default')
                return '默认';
            if(value=='longseason')
                return '长';
            if(value=='verylongseason')
                return '极长';
            if(value=='random')
                return '随机';
            if(value=='shortseason')
                return '短'
            if(value=='veryshortseason')
                return '极短'
            if(value=='noseason')
                return '无'
            if(value=='longday')
                return '长 白天';
            if(value=='longdusk')
                return '长 黄昏';
            if(value=='longnight')
                return '长 夜晚';
            if(value=='noday')
                return '无 白天';
            if(value=='nodusk')
                return '无 黄昏';
            if(value=='nonight')
                return '无 夜晚';
            if(value=='onlyday')
                return '仅 白天';
            if(value=='onlydusk')
                return '仅 黄昏';
            if(value=='onlynight')
                return '仅 夜晚';
            if(value=='fixed')
                return '绚丽之门';
            if(value=='scatter')
                return '随机';
            if(value=='never')
                return '无';
            if(value=='rare')
                return '很少';
            if(value=='uncommon')
                return '较少';
            if(value=='often')
                return '较多';
            if(value=='mostly')
                return '很多';
            if(value=='always')
                return '大量';
            if(value=='insane')
                return '疯狂';
            if(value=='ocean_never')
                return '无';
            if(value=='ocean_rare')
                return '很少';
            if(value=='ocean_uncommon')
                return '较少';
            if(value=='ocean_often')
                return '较多';
            if(value=='ocean_mostly')
                return '很多';
            if(value=='ocean_always')
                return '大量';
            if(value=='ocean_insane')
                return '疯狂';
            if(value=='enabled')
                return '总是';
            if(value=='none')
                return '禁用';
            if(value=='few')
                return '慢';
            if(value=='many')
                return '快';
            if(value=='max')
                return '极快';
            if(value=='classic')
                return '经典';
            if(value=='highly random')
                return '非常随机';
            if(value=='small')
                return '小';
            if(value=='medium')
                return '中';
            if(value=='huge')
                return '巨大';
            if(value=='cave_default')
                return '地下';
            if(value=='caves')
                return '洞穴';
            else
                return value;
        },
        changeWorld(name){
            this.world = name;
            document.querySelectorAll('.navigation').forEach(element=>{
                element.classList.remove('selected2');
            })
            document.getElementById(name+'-button').classList.add('selected2');
        },
        changeRule(name){
            this.rule = name;
            document.querySelectorAll('.navigation').forEach(element=>{
                element.classList.remove('selected3');
            })
            document.getElementById(name+'-button').classList.add('selected3');
        },
        handleGetWorld(){
            getWorld().then(response=>{
                let data=response.data;
                this.forest_rule.全局.活动=data.specialevent;
                this.forest_rule.全局.秋=data.autumn;
                this.forest_rule.全局.冬=data.winter;
                this.forest_rule.全局.春=data.spring,
                this.forest_rule.全局.夏=data.summer;
                this.forest_rule.全局.昼夜选项=data.day;
                this.forest_rule.全局.出生模式=data.spawnmode;
                if(data.ghostenabled=='always')
                    this.forest_rule.全局.冒险家死亡='变鬼魂';
                else
                    this.forest_rule.全局.冒险家死亡='更换冒险家';
                if(data.portalresurection=='always')
                    this.forest_rule.全局.在绚丽之门复活='启用';
                else
                    this.forest_rule.全局.在绚丽之门复活='禁用';
                this.forest_rule.全局.鬼魂理智值惩罚=data.ghostsanitydrain;
                this.forest_rule.全局.死亡重置倒计时=data.resettime;
                this.forest_rule.全局.皮弗娄牛交配频率=data.beefaloheat;
                this.forest_rule.全局.坎普斯=data.krampus;

                this.forest_rule.生物.一角鲸=data.gnarwail;
                this.forest_rule.生物.企鸥=data.penguins;
                this.forest_rule.生物.兔人=data.bunnymen_setting;
                this.forest_rule.生物.兔子=data.rabbits_setting;
                this.forest_rule.生物.浣猫=data.catcoons;
                this.forest_rule.生物.火鸡=data.perd;
                this.forest_rule.生物.猪=data.pigs_setting;
                this.forest_rule.生物.草壁虎转化=data.grassgekkos;
                this.forest_rule.生物.蜜蜂=data.bees_setting;
                this.forest_rule.生物.蝴蝶=data.butterfly;
                this.forest_rule.生物.鱼群=data.fishschools;
                this.forest_rule.生物.鸟=data.birds;
                this.forest_rule.生物.鼹鼠=data.moles_setting;
                this.forest_rule.生物.龙虾=data.wobsters;

                this.forest_rule.活动.盛夏鸦年华=data.crow_carnival;
                this.forest_rule.活动.万圣夜=data.hallowed_nights;
                this.forest_rule.活动.冬季盛宴=data.winters_feast;
                this.forest_rule.活动.火鸡之年=data.year_of_the_gobbler;
                this.forest_rule.活动.座狼之年=data.year_of_the_varg;
                this.forest_rule.活动.胡萝卜鼠之年=data.year_of_the_carrat;
                this.forest_rule.活动.猪王之年=data.year_of_the_pig;
                this.forest_rule.活动.皮弗娄牛之年=data.year_of_the_beefalo;
                this.forest_rule.活动.浣猫之年=data.year_of_the_catcoon;
                this.forest_rule.活动.兔人之年=data.year_of_the_bunnyman;
                this.forest_rule.活动.龙蝇之年=data.year_of_the_dragonfly;

                if(data.extrastartingitems=='default')
                    this.forest_rule.冒险家.额外起始资源='第10天后';
                else if(data.extrastartingitems=='5')
                    this.forest_rule.冒险家.额外起始资源='第5天后';
                else if(data.extrastartingitems=='15')
                    this.forest_rule.冒险家.额外起始资源='第15天后';
                else if(data.extrastartingitems=='20')
                    this.forest_rule.冒险家.额外起始资源='第20天后';
                else if(data.extrastartingitems=='0')
                    this.forest_rule.冒险家.额外起始资源='总是';
                else
                    this.forest_rule.冒险家.额外起始资源='从不';
                this.forest_rule.冒险家.季节起始物品=data.seasonalstartingitems;
                if(data.spawnprotection=='default')
                    this.forest_rule.冒险家.防骚扰出生保护='自动检测';
                if(data.spawnprotection=='never')
                    this.forest_rule.冒险家.防骚扰出生保护='无';
                if(data.spawnprotection=='always')
                    this.forest_rule.冒险家.防骚扰出生保护='总是';

                if(data.dropeverythingondespawn=='always')
                    this.forest_rule.冒险家.离开游戏后物品掉落='所有';
                else
                    this.forest_rule.冒险家.离开游戏后物品掉落='默认';

                if(data.healthpenalty=='always')
                    this.forest_rule.冒险家.血量上限惩罚='启用';
                else
                    this.forest_rule.冒险家.血量上限惩罚='禁用';
                if(data.lessdamagetaken=='more')
                    this.forest_rule.冒险家.收到的伤害='较多';
                else if(data.lessdamagetaken=='none')
                    this.forest_rule.冒险家.收到的伤害='默认';
                else
                    this.forest_rule.冒险家.收到的伤害='较少';
                if(data.temperaturedamage=='nonlethal')
                    this.forest_rule.冒险家.温度伤害='非致命';
                else
                    this.forest_rule.冒险家.温度伤害='默认';
                
                if(data.hunger=='nonlethal')
                    this.forest_rule.冒险家.饥饿伤害='非致命';
                else
                    this.forest_rule.冒险家.饥饿伤害='默认';

                if(data.darkness=='nonlethal')
                    this.forest_rule.冒险家.黑暗伤害='非致命';
                else
                    this.forest_rule.冒险家.黑暗伤害='默认';
                this.forest_rule.冒险家.理智怪兽=data.shadowcreatures;
                this.forest_rule.冒险家.启蒙怪兽=data.brightmarecreatures;

                this.forest_rule.世界.猎犬袭击=data.hounds;
                this.forest_rule.世界.冰猎犬群=data.winterhounds;
                this.forest_rule.世界.火猎犬群=data.summerhounds;
                if(data.petrification=='none')
                    this.forest_rule.世界.森林石化='无';
                else
                    this.forest_rule.世界.森林石化=data.petrification;
                this.forest_rule.世界.流星频率=data.meteorshowers;
                this.forest_rule.世界.狩猎=data.hunt;
                this.forest_rule.世界.荒野裂隙开启=data.rifts_enabled;
                this.forest_rule.世界.荒野裂隙频率=data.rifts_frequency;
                this.forest_rule.世界.追猎惊喜=data.alternatehunt;
                this.forest_rule.世界.野火=data.wildfires;
                this.forest_rule.世界.闪电=data.lightning;
                this.forest_rule.世界.雨=data.weather;
                this.forest_rule.世界.青蛙雨=data.frograin;

                this.forest_rule.资源再生.胡萝卜=data.carrots_regrowth;
                this.forest_rule.资源再生.仙人掌=data.cactus_regrowth;
                this.forest_rule.资源再生.基础资源=data.basicresource_regrowth;
                this.forest_rule.资源再生.多枝树=data.twiggytrees_regrowth;
                this.forest_rule.资源再生.盐堆=data.saltstack_regrowth;
                this.forest_rule.资源再生.芦苇=data.reeds_regrowth;
                this.forest_rule.资源再生.棕榈松果树=data.palmconetree_regrowth;
                this.forest_rule.资源再生.月树=data.moon_tree_regrowth;
                this.forest_rule.资源再生.花=data.flowers_regrowth;
                this.forest_rule.资源再生.常青树=data.evergreen_regrowth;
                this.forest_rule.资源再生.桦栗树=data.deciduoustree_regrowth;
                this.forest_rule.资源再生.再生速度=data.regrowth;

                this.forest_rule.非自然传送门资源.传送频率=data.portal_spawnrate;
                this.forest_rule.非自然传送门资源.发光蟹=data.lightcrab_portalrate;
                this.forest_rule.非自然传送门资源.棕榈松果树芽=data.palmcone_seed_portalrate;
                this.forest_rule.非自然传送门资源.火药猴=data.powder_monkey_portalrate;
                this.forest_rule.非自然传送门资源.猴尾草=data.monkeytail_portalrate;
                this.forest_rule.非自然传送门资源.香蕉丛=data.bananabush_portalrate;

                this.forest_rule.敌对生物.蝙蝠=data.bats_setting;
                this.forest_rule.敌对生物.蜘蛛=data.spiders_setting;
                this.forest_rule.敌对生物.海象=data.walrus_setting;
                this.forest_rule.敌对生物.月亮码头海盗=data.pirateraids;
                this.forest_rule.敌对生物.恐怖猎犬=data.mutated_hounds;
                this.forest_rule.敌对生物.杀人蜂=data.wasps;
                this.forest_rule.敌对生物.月石企鸥=data.penguins_moon;
                this.forest_rule.敌对生物.猎犬=data.hound_mounds;
                this.forest_rule.敌对生物.破碎蜘蛛=data.moon_spider;
                this.forest_rule.敌对生物.蚊子=data.mosquitos;
                this.forest_rule.敌对生物.蜘蛛战士=data.spider_warriors;
                this.forest_rule.敌对生物.青蛙=data.frogs;
                this.forest_rule.敌对生物.鱼人=data.merms;
                this.forest_rule.敌对生物.食人花=data.lureplants;
                this.forest_rule.敌对生物.饼干切割机=data.cookiecutters;
                this.forest_rule.敌对生物.鱿鱼=data.squid;
                this.forest_rule.敌对生物.鲨鱼=data.sharks;

                this.forest_rule.巨兽.克劳斯=data.klaus;
                this.forest_rule.巨兽.帝王蟹=data.crabking;
                this.forest_rule.巨兽.恐怖之眼=data.eyeofterror;
                this.forest_rule.巨兽.果蝇王=data.fruitfly;
                this.forest_rule.巨兽.树精守卫=data.liefs;
                this.forest_rule.巨兽.毒桦栗树=data.deciduousmonster;
                this.forest_rule.巨兽.熊獾=data.bearger;
                this.forest_rule.巨兽.独眼巨鹿=data.deerclops;
                this.forest_rule.巨兽.蚁狮贡品=data.antliontribute;
                this.forest_rule.巨兽.蜂王=data.beequeen;
                this.forest_rule.巨兽.蜘蛛女王=data.spiderqueen;
                this.forest_rule.巨兽.邪天翁=data.malbatross;
                this.forest_rule.巨兽.麋鹿鹅=data.goosemoose;
                this.forest_rule.巨兽.龙蝇=data.dragonfly;

                if(data.season_start=='default')
                    this.forest_generate.全局.起始季节='秋';
                if(data.season_start=='winter')
                    this.forest_generate.全局.起始季节='冬';
                if(data.season_start=='spring')
                    this.forest_generate.全局.起始季节='春';
                else
                    this.forest_generate.全局.起始季节='夏';

                this.forest_generate.世界.生物群落=data.task_set;
                this.forest_generate.世界.出生点=data.start_location;
                if(data.world_size=='default')
                    this.forest_generate.世界.世界大小='大';
                else
                    this.forest_generate.世界.世界大小=data.world_size;
                this.forest_generate.世界.分支=data.branching;
                this.forest_generate.世界.环形=data.loop;
                this.forest_generate.世界.道路=data.roads;
                this.forest_generate.世界.试金石=data.touchstone;
                this.forest_generate.世界.失败的冒险家=data.boons;
                this.forest_generate.世界.开始资源多样化=data.prefabswaps_start;
                this.forest_generate.世界.天体裂隙=data.moon_fissure;
                this.forest_generate.世界.盒中泰拉=data.terrariumchest
                this.forest_generate.世界.舞台剧=data.stageplays;

                this.forest_generate.资源.仙人掌=data.cactus;
                this.forest_generate.资源.公牛海带茎=data.ocean_bullkelp;
                this.forest_generate.资源.尖刺灌木=data.marshbush;
                this.forest_generate.资源.巨石=data.rock;
                this.forest_generate.资源.月亮树苗=data.moon_sapling;
                this.forest_generate.资源.月亮石=data.moon_rock;
                this.forest_generate.资源.月树=data.moon_tree;
                this.forest_generate.资源.树苗=data.sapling;
                this.forest_generate.资源.所有树=data.trees;
                this.forest_generate.资源.棕榈松果树=data.palmconetree;
                this.forest_generate.资源.池塘=data.ponds;
                this.forest_generate.资源.流星区域=data.meteorspawner;
                this.forest_generate.资源.浆果丛=data.berrybush;
                this.forest_generate.资源.海岸公牛海带=data.moon_bullkelp;
                this.forest_generate.资源.海星=data.moon_starfish;
                this.forest_generate.资源.海蚀柱=data.ocean_seastack;
                this.forest_generate.资源.温泉=data.moon_hotspring;
                this.forest_generate.资源.燧石=data.flint;
                this.forest_generate.资源.石果灌木丛=data.moon_berrybush;
                this.forest_generate.资源.胡萝卜=data.carrot;
                this.forest_generate.资源.芦苇=data.reeds;
                this.forest_generate.资源.花和邪恶花=data.flowers;
                this.forest_generate.资源.草=data.grass;
                this.forest_generate.资源.蘑菇=data.mushroom;
                this.forest_generate.资源.迷你冰川=data.rock_ice;
                this.forest_generate.资源.风滚草=data.tumbleweed;

                this.forest_generate.生物以及刷新点.伏特羊=data.lightninggoat;
                this.forest_generate.生物以及刷新点.兔洞=data.rabbits;
                this.forest_generate.生物以及刷新点.沙拉蝾螈=data.moon_fruitdragon;
                this.forest_generate.生物以及刷新点.猪屋=data.pigs;
                this.forest_generate.生物以及刷新点.皮弗娄牛=data.beefalo;
                this.forest_generate.生物以及刷新点.秃鹫=data.buzzard;
                this.forest_generate.生物以及刷新点.空心树桩=data.catcoon;
                this.forest_generate.生物以及刷新点.胡萝卜鼠=data.moon_carrot;
                this.forest_generate.生物以及刷新点.蜜蜂蜂窝=data.bees;
                this.forest_generate.生物以及刷新点.鱼群=data.ocean_shoal;
                this.forest_generate.生物以及刷新点.鼹鼠丘=data.moles;
                this.forest_generate.生物以及刷新点.龙虾窝=data.ocean_wobsterden;

                this.forest_generate.敌对生物以及刷新点.发条装置=data.chess;
                this.forest_generate.敌对生物以及刷新点.杀人蜂蜂窝=data.angrybees;
                this.forest_generate.敌对生物以及刷新点.海草=data.ocean_waterplant;
                this.forest_generate.敌对生物以及刷新点.海象营地=data.walrus;
                this.forest_generate.敌对生物以及刷新点.漏雨的小屋=data.merm;
                this.forest_generate.敌对生物以及刷新点.猎犬丘=data.houndmound;
                this.forest_generate.敌对生物以及刷新点.破碎蜘蛛洞=data.moon_spiders;
                this.forest_generate.敌对生物以及刷新点.蜘蛛巢=data.spiders;
                this.forest_generate.敌对生物以及刷新点.触手=data.tentacles;
                this.forest_generate.敌对生物以及刷新点.高脚鸟=data.tallbirds;
            })
        },
        handleGetWorld2(){
            getWorld2().then(response=>{
                let data=response.data;

                this.cave_rule.世界.地震=data.earthquakes;
                this.cave_rule.世界.洞穴蠕虫攻击=data.wormattacks;
                this.cave_rule.世界.荒野裂隙开启=data.rifts_enabled_cave;
                this.cave_rule.世界.荒野裂隙频率=data.rifts_frequency_cave;
                this.cave_rule.世界.远古大门=data.atriumgate;
                this.cave_rule.世界.雨=data.weather;

                this.cave_rule.资源再生.再生速度=data.regrowth;
                this.cave_rule.资源再生.光虫花=data.lightflier_flower_regrowth;
                this.cave_rule.资源再生.月亮蘑菇树=data.mushtree_moon_regrowth;
                this.cave_rule.资源再生.荧光花=data.flower_cave_regrowth;
                this.cave_rule.资源再生.蘑菇树=data.mushtree_regrowth;

                this.cave_rule.生物.兔人=data.bunnymen_setting;
                this.cave_rule.生物.尘蛾=data.dustmoths;
                this.cave_rule.生物.猪=data.pigs_setting;
                this.cave_rule.生物.球状光虫=data.lightfliers;
                this.cave_rule.生物.石虾=data.rocky_setting;
                this.cave_rule.生物.穴居猴=data.monkey_setting;
                this.cave_rule.生物.草壁虎转化=data.grassgekkos;
                this.cave_rule.生物.蛞蝓龟=data.slurtles_setting;
                this.cave_rule.生物.蜗牛龟=data.snurtles;
                this.cave_rule.生物.蘑菇地精=data.mushgnome;
                this.cave_rule.生物.鼹鼠=data.moles_setting;

                this.cave_rule.敌对生物.喷射蜘蛛=data.spider_spitter;
                this.cave_rule.敌对生物.洞穴蜘蛛=data.spider_hider;
                this.cave_rule.敌对生物.穴居悬蛛=data.spider_dropper;
                this.cave_rule.敌对生物.蜘蛛=data.spiders_setting;
                this.cave_rule.敌对生物.蜘蛛战士=data.spider_warriors;
                this.cave_rule.敌对生物.蝙蝠=data.bats_setting;
                this.cave_rule.敌对生物.遗迹梦魇=data.nightmarecreatures;
                this.cave_rule.敌对生物.裸鼹蝠=data.molebats;
                this.cave_rule.敌对生物.鱼人=data.merms;

                this.cave_rule.巨兽.噩梦猪人=data.daywalker;
                this.cave_rule.巨兽.果蝇王=data.fruitfly;
                this.cave_rule.巨兽.树精守卫=data.liefs;
                this.cave_rule.巨兽.毒菌蟾蜍=data.toadstool;
                this.cave_rule.巨兽.蜘蛛女王=data.spiderqueen;

                this.cave_generate.世界.生物群落=data.task_set;
                this.cave_generate.世界.出生点=data.start_location;
                this.cave_generate.世界.世界大小=data.world_size;
                this.cave_generate.世界.分支=data.branching;
                this.cave_generate.世界.环形=data.loop;
                this.cave_generate.世界.试金石=data.touchstone;
                this.cave_generate.世界.失败的冒险家=data.boons;
                this.cave_generate.世界.洞穴光照=data.cavelight;
                this.cave_generate.世界.开始资源多样化=data.prefabswaps_start;

                this.cave_generate.资源.发光浆果=data.wormlights;
                this.cave_generate.资源.尖刺灌木=data.marshbush;
                this.cave_generate.资源.巨石=data.rock;
                this.cave_generate.资源.树苗=data.sapling;
                this.cave_generate.资源.所有树=data.trees;
                this.cave_generate.资源.池塘=data.cave_ponds;
                this.cave_generate.资源.洞穴蕨类=data.fern;
                this.cave_generate.资源.浆果丛=data.berrybush;
                this.cave_generate.资源.燧石=data.flint;
                this.cave_generate.资源.芦苇=data.reeds;
                this.cave_generate.资源.苔藓=data.lichen;
                this.cave_generate.资源.草=data.grass;
                this.cave_generate.资源.荧光花=data.flower_cave;
                this.cave_generate.资源.蘑菇=data.mushroom;
                this.cave_generate.资源.蘑菇树=data.mushtree;
                this.cave_generate.资源.香蕉=data.banana;
                
                this.cave_generate.生物以及刷新点.兔屋=data.bunnymen;
                this.cave_generate.生物以及刷新点.啜食者=data.slurper;
                this.cave_generate.生物以及刷新点.石虾=data.rocky;
                this.cave_generate.生物以及刷新点.穴居猴桶=data.monkey;
                this.cave_generate.生物以及刷新点.蛞蝓龟窝=data.slurtles;

                this.cave_generate.敌对生物以及刷新点.发条装置=data.chess;
                this.cave_generate.敌对生物以及刷新点.梦魇裂隙=data.fissure;
                this.cave_generate.敌对生物以及刷新点.洞穴蠕虫=data.worms;
                this.cave_generate.敌对生物以及刷新点.蛛网岩=data.cave_spiders;
                this.cave_generate.敌对生物以及刷新点.蜘蛛巢=data.spiders;
                this.cave_generate.敌对生物以及刷新点.蝙蝠=data.bats;
                this.cave_generate.敌对生物以及刷新点.触手=data.tentacles;
            })
        }
    },
    mounted(){
        this.handleGetWorld();
        this.handleGetWorld2();
    }
}
</script>
<style scoped>
#world{
    height: 100%;
    width: 100%;
}
.world-navigation{
    width: calc(100% - 2vw);
    margin: 0 1vw;
    padding-top: 1vh;
    height: 4vh;
    display: flex;
    font-size: 2vh;
}
.navigation{
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    background-image: url('../../image/navigation/导航背景1.png'); /* 背景图片路径 */
    background-size: 100% 90%;
    background-repeat: no-repeat;
    background-position: bottom;
    position: absolute;
    left: 0px;
    top: 0;
    z-index: 0;
    justify-content: center;
    color: rgb(200,200,150);
    cursor: pointer;
}
.navigation.selected2{
    background-image: url('../../image/navigation/导航背景2.png'); /* 背景图片路径 */
    color: black;
}
.navigation.selected2:hover {
    color: initial;
}
.navigation.selected3{
    background-image: url('../../image/navigation/导航背景2.png'); /* 背景图片路径 */
    color: black;
}
.navigation.selected3:hover {
    color: initial;
}
.navigation:hover{
    color: orange;
}
.navigation-border{
    height: 100%;
    width: 10vw;
    z-index: 100;
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
    margin-right: 1vw;
    position: relative;
}
.navigation-border:hover{
    background-image: url('../../image/navigation/导航背景装饰.png'); /* 背景图片路径 */
}
#world-set{
    width: calc(100% - 1vw);
    /* height: 100%; */
    display: flex;
    flex-wrap: wrap;
    align-content: baseline;
    margin-right: 1vw;
    gap: 0.5vw;
}
.line{
    height: 0.6vh;
    width: 100%;
}
.line-1{
    height: 0.2vh;
    width: 100%;
    background-color: rgb(140,130,120);
}
.line-2{
    height: 0.2vh;
    width: 100%;
    background-color: rgb(160,150,140);
}
.line-3{
    height: 0.2vh;
    width: 100%;
    background-color: rgb(180,170,160);
}
#world-set-scorllContainer{
    width: calc(100% - 2vw);
    margin: 1vh 1vw;
    margin-bottom: 0;
    height: calc(100% - 12.2vh);
    overflow-y: scroll;
    display: flex;
    flex-wrap: wrap;
}
#world-set-scorllContainer::-webkit-scrollbar{
    width: 1vw;
}
#world-set-scorllContainer::-webkit-scrollbar-track{
    background-image: url('../../image/tab/滑轨.png');
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
}
#world-set-scorllContainer::-webkit-scrollbar-thumb{
    height: 1vh;
    background-image: url('../../image/navigation/滑轨按钮.png');
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
}
#world-set-scorllContainer::-webkit-scrollbar-button:start{
    height: 1vh;
    background-image: url('../../image/navigation/滑轨按钮上.png');
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
}
#world-set-scorllContainer::-webkit-scrollbar-button:end{
    height: 1vh;
    background-image: url('../../image/navigation/滑轨按钮下.png');
    background-size: 100% auto;
    background-repeat: no-repeat;
    background-position: center;
}
.label{
    width: 100%;
    height: 6vh;
    background-color: rgb(40,30,20);
    color: white;
    font-size: 2.5vh;
    line-height: 2.5vh;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 1vh;
    justify-content: center;
}
.worldCard{
    flex-basis: calc(33.33% - 0.3333vw);
}
</style>