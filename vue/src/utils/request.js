import axios from 'axios'
export function request(config){
    const instance = axios.create({
        baseURL: import.meta.env.VITE_BASE_API,
        timeout:500000
    })
    //添加请求拦截器
    instance.interceptors.request.use(function(config){
        //在发送请求之前做些什么
        const token = localStorage.getItem('token'); // 从localStorage中获取令牌
        if(token){
            config.headers['X-token'] = token;      //给所有的请求头加这个字段
        }
        
        return config;
    },function(error){
        //在请求错误做些什么
        return Promise.reject(error);
    });

    //添加响应拦截器
    instance.interceptors.response.use(function(response){
        //2xx范围内的状态码都会触发该函数
        //对响应数据做些什么
        return response;
    },function(error){
        //超出2xx范围内的状态码都会触发该函数
        //对响应错误做些什么
        return Promise.reject(error);
    });
    return instance(config)

}