<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <div
          class="container pt-4 col-md-12 "
          style="box-shadow: 0 0 10px 0 rgba(0, 0, 0, .1);"
        >
          <form>
            <!-- function: “TypeError: Cannot read property 'type' of undefined” -->
            <template v-if="orderList[0]">
              <h3 class="pb-3">订单信息</h3>
              <div class="form-row">
                <div class="form-row col-md-6">
                  <p>订单编号：</p>
                  <p>{{ orderList[0].order_id }}</p>
                </div>
              </div>
              <div class="form-row">
                <div class="form-row col-md-6">
                  <p>创建日期：</p>
                  <p>{{ orderList[0].datetime }}</p>
                </div>
              </div>
              <div class="form-row">
                <div class="form-row col-12">
                  <p>客户：</p>
                  <p>{{ orderList[0].customer_id }}</p>
                  <p>{{ orderList[0].customer_name }}</p>
                </div>
              </div>
              <table
                class="table container-fluid"
                style="word-break:break-all; word-wrap:break-all;"
              >
                <thead>
                  <tr>
                    <b-row
                      class="form-row"
                      style="word-break:break-all; word-wrap:break-all;"
                    >
                      <th style="width:5%;">序</th>
                      <th style="width:10%;">ID</th>
                      <th style="width:25%;">P_Name</th>
                      <th style="width:30%;">P_Detal</th>
                      <th style="width:10%;">Count</th>
                      <th style="width:10%;">Price</th>
                      <th style="width:10%;">Total</th>
                    </b-row>
                  </tr>
                </thead>
                <tbody>
                  <tr
                    v-for="(product, index) in orderList"
                    :key="index"
                    style="white-space:nowrap;overflow:hidden"
                  >
                    <b-row class="form-row">
                      <td style="width:5%;">{{ index + 1 + "." }}</td>
                      <td style="width:10%;">{{ product.product_id }}</td>
                      <td style="width:25%;">{{ product.product_name }}</td>
                      <td style="width:30%;">{{ product.product_detal }}</td>
                      <td style="width:10%;">{{ product.count }}</td>
                      <td style="width:10%;">{{ product.price }}</td>
                      <td style="width:10%;">{{ product.subtotal }}</td>
                    </b-row>
                  </tr>
                </tbody>
              </table>
              <button
                type="button"
                class="btn btn-primary mb-4 mr-2 col-2 float-right"
                @click="onEditOrder(orderList[0].order_id)"
              >
                编辑
              </button>
            </template>
          </form>
        </div>
      </div>
    </div>

    <pre>orderList = {{ orderList }}</pre>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      orderList: []
    };
  },
  computed: {},

  created() {
    this.fetchOrder();
  },
  methods: {
    fetchOrder() {
      //拿到查询字段，订单的id后进行axios请求
      var send_info = {
        order_id : this.$route.query.orderId
      }
      console.log(send_info);
      const path = "http://localhost:4000/orders";
      axios.put(path,send_info).then(
        res => {
          this.orderList = res.data;
        },
        error => {
          console.log(error);
        }
      );

      this.loading = false;
    },
    onEditOrder(order_id) {
      let routeData = this.$router.resolve({
        path: "/all_orders/edit",
        query: {
          orderId: order_id
        }
      });
      window.open(routeData.href, "_blank");
    }
  }
};
</script>
