
<template>
  <div>
    <table
      class="table container-fluid"
      style="word-break:break-all; word-wrap:break-all;"
    >
      <thead>
        <tr>
          <b-row class="ml-3 mr-3">
            <th style="width:5%;">序</th>
            <th style="width:15%;">订单编号</th>
            <th style="width:10%;">客户编号</th>
            <th style="width:15%;">客户</th>
            <th style="width:10%;">合计</th>
            <th style="width:15%;">创建日期</th>
            <th style="width:10%;">状态</th>
            <th style="width:20%;">操作</th>
          </b-row>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(product, index) in this.list" :key="index">
          <b-row class="ml-3 mr-3" style="margin-bottom:-0.5rem;">
            <td style="width:5%;">{{ index }}</td>
            <td style="width:15%;">{{ product.order_id }}</td>
            <td style="width:10%;">{{ product.customer_id }}</td>
            <td style="width:15%;">{{ product.customer_name }}</td>
            <td style="width:10%;">{{ product.total_amount }}</td>
            <td style="width:15%;">{{ product.datetime | formatDate }}</td>
            <td style="width:10%;">未配送完</td>
            <td style="width:20%;">
              <div>
                <b-button
                  type="button"
                  class="btn btn-sm btn-info"
                  @click="onDetalOrder(product.order_id)"
                  >订单详情
                </b-button>
                <!-- <button
                    type="button"
                    class="btn btn-sm btn-warning"
                    @click="onDetalOrder(product.order_id)"
                    >发起订单
                  </button> -->
                <b-button
                  type="button"
                  class="btn btn-sm btn-danger"
                  @click="onReleaseOrder(product.order_id)"
                  >剩余订单
                </b-button>
              </div>
            </td>
          </b-row>
        </tr>
      </tbody>
    </table>
    <!-- <pre>list = {{ list }}</pre> -->
  </div>
</template>
          
         
<script>
import axios from "axios";
export default {
  data() {
    return {
      list: []
    };
  },
  filters: {
    formatDate: function(value) {
      let date = new Date(value);
      let y = date.getFullYear();
      let MM = date.getMonth() + 1;
      MM = MM < 10 ? "0" + MM : MM;
      let d = date.getDate();
      d = d < 10 ? "0" + d : d;
      let h = date.getHours();
      h = h < 10 ? "0" + h : h;
      let m = date.getMinutes();
      m = m < 10 ? "0" + m : m;
      let s = date.getSeconds();
      s = s < 10 ? "0" + s : s;
      return y + "-" + MM + "-" + d + " " + h + ":" + m + ":" + s;
    }
  },
  computed: {},
  created() {},
  // 实例被激活时使用，用于重复激活一个实例的时候
  // 配合keep-alive标签使用!
  activated: function() {
    console.log("activate");
    this.load_orders();
  },
  // 实例没有被激活时
  deactivated: function() {
    console.log("deactivated");
  },
  methods: {
    load_orders() {
      console.log("load_orders");
      const path = "http://localhost:4000/orders";
      axios
        .get(path)
        .then(res => {
          console.log(res.data);
          this.list = res.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
    onDetalOrder(order_id) {
      let routeData = this.$router.resolve({
        path: "/all_orders/detail",
        query: {
          orderId: order_id
        }
      });
      window.open(routeData.href, "_blank");
    },
    onReleaseOrder(order_id) {
      let routeData = this.$router.resolve({
        path: "/all_orders/release",
        query: {
          orderId: order_id
        }
      });
      window.open(routeData.href, "_blank");
    }
  }
};
</script>