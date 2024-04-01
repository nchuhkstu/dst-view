import { createRouter,createWebHistory} from "vue-router";
const router = createRouter({
    routes:[
        {
            name: '首页',
            component:() => import('../pages/Home.vue')
        },
    ],
    history:createWebHistory()
})

export default router