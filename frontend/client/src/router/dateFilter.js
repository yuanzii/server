import Vue from "vue"
// 引入moment
import moment from "moment"

// // 第一个参数 input 是传递过来的时间挂载过滤器的是一个时间戳    
// // 第二个参数 dateFormat 是挂载的过滤器格式
// Vue.filter('dateFormat',function(input,dateFormat){
//     // 1592484972321
//     console.log(input);
//     // YYYY/MM/DD HH:mm:ss 
//     console.log(dateFormat);
//     return moment(input).format(dateFormat)

// }) 
Vue.prototype.$moment = moment