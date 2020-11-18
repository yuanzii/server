<template>
  <div>
    <div class="container-fluid col-6 pb-3 " v-for="(products, index) in this.list"
                    :key="index">
      <div class="row">
        <div
          class="container pt-4 pb-3 col-md-12 col-lg-12 border border-warning "
          style="box-shadow: 0 0 10px 0 rgba(0, 0, 0, .1);border-radius: 20px;"
        >
          <form>
            <h3 class="pb-3">订单信息</h3>
            <div class="form-row">
              <div class="form-row col-md-6">
                <p>订单编号：</p>
                <p>{{ products.waybill_id }}</p>
              </div>
            </div>
            <div class="form-row">
              <div class="form-row col-md-6">
                <p>创建日期：</p>
                <p>{{ products.order_create_time | formatDate }}</p>
              </div>
            </div>
            <div class="form-row">
              <div class="form-row col-12">
                <p>客户：</p>
                <p>{{ products.customer_id }}</p>
                <p>{{ products.customer_name }}</p>
              </div>
            </div>
            <div class="form-group pt-3">
              <table
                class="table container-fluid"
                style="word-break:break-all; word-wrap:break-all;"
              >
                <thead>
                  <tr>
                    <b-row class="">
                      <th class="col-md-2">ID</th>
                      <th class="col-md-3">P_Name</th>
                      <th class="col-md-3">P_Detal</th>
                      <th class="col-md-1">Count</th>
                      <th class="col-md-1">Price</th>
                      <th class="col-md-2">Total</th>
                    </b-row>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(product, index) in products"
                    :key="index"
                    style="white-space:nowrap;overflow:hidden;"
                  >
                    <b-row class="">
                      <td class="col-md-2">{{ product.product_id }}</td>
                      <td class="col-md-3">{{ product.product_name }}</td>
                      <td class="col-md-3">{{ product.product_detal }}</td>
                      <td class="col-md-1">{{ product.count }}</td>
                      <td class="col-md-1">{{ product.price }}</td>
                      <td class="col-md-2">{{ product.subtotal }}</td>
                    </b-row>
                  </tr>
                </tbody>
              </table>
              <!-- <button
                type="submit"
                class="btn btn-warning mb-4 mr-2 col-2 float-right"
                @click="onMissedOrder"
              >
                打印
              </button> -->
            </div>
          </form>
        </div>
      </div>
    </div>
    <p>hello</p>
    <pre>missed_orders = {{ list }}</pre>
    <!-- <b-button
      type="button"
      class="btn btn-sm btn-danger"
      @click="onReleaseOrder"
      >剩余订单
    </b-button> -->
  </div>
</template>

<script>
import { formatDate } from "../router/dateFilter";
import axios from "axios";
export default {
  data() {
    return {
      list: []
    };
  },
  filters: {
    formatDate(datetime) {
      var date = new Date(datetime);
      return formatDate(date, "yyyy-MM-dd hh:mm:ss");
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
      const path = "http://localhost:4000/waybill";
      axios
        .get(path)
        .then(res => {
          console.log(res.data)
          this.list = res.data;
          // console.log(res.data);
          // this.chachong();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // chachong(list){
    //   //Map()是筛选出来的,去重.
    //   const res = new Map();
    //   console.log(res)
    //   let list1 = list.filter((list) => !res.has(list.order_id)&& res.set(list.order_id, 1))
    //   this.list = list1
    // },
    // onDetalOrder(order_id) {
    //   let routeData = this.$router.resolve({
    //     path: "/all_orders/detail",
    //     query: {
    //       orderId: order_id
    //     }
    //   });
    //   window.open(routeData.href, "_blank");
    // },
    // onReleaseOrder(order_id) {
    //   let routeData = this.$router.resolve({
    //     path: "/all_orders/release",
    //     query: {
    //       orderId: order_id
    //     }
    //   });
    //   window.open(routeData.href, "_blank");
    // }
  }
};
</script>
