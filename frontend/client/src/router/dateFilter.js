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


// 后台数据时间戳转换成日期格式
export function formatDate(datetime) {
    let date = new Date(datetime);
    let y = date.getFullYear();
    let MM = date.getMonth() + 1;
    MM = MM < 10 ? "0" + MM : MM;
    let d = date.getDate();
    d = d < 10 ? "0" + d : d;
    let h = date.getHours();
    let H = h-6 //得到的时间再减于6，这样就可以好排查<10的数+0了
    h = H < 10 ? "0" + H : H ;
    let m = date.getMinutes();
    m = m < 10 ? "0" + m : m;
    let s = date.getSeconds();
    s = s < 10 ? "0" + s : s;
    return y + "-" + MM + "-" + d + " " + h + ":" + m + ":" + s;
}