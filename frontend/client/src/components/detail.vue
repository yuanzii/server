<template>
  <div>
    <!-- container-fluid -->
    <div class="container p-3">
      <div class="row">
        <div
          class="container pt-4 p-3 col-md-12 col-lg-12 border border-warning "
          style="box-shadow: 0 0 10px 0 rgba(0, 0, 0, .1);border-radius: 20px;"
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

              <div class="form-group pt-3">
                <table
                  class="table container-fluid"
                  style="word-break:break-all; word-wrap:break-all;"
                >
                  <thead>
                    <tr>
                      <b-row class="">
                        <th class="col-md-1">ID</th>
                        <th class="col-md-3">P_Name</th>
                        <th class="col-md-3">P_Detal</th>
                        <th class="col-md-1">Count</th>
                        <th class="col-md-1">Price</th>
                        <th class="col-md-3">Total</th>
                      </b-row>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(product, index) in orderList"
                      :key="index"
                      style="white-space:nowrap;overflow:hidden"
                    >
                      <b-row class="">
                        <td class="col-md-1">{{ product.product_id }}</td>
                        <td class="col-md-3">{{ product.product_name }}</td>
                        <td class="col-md-3">{{ product.product_detal }}</td>
                        <td class="col-md-1">{{ product.count }}</td>
                        <td class="col-md-1">{{ product.price }}</td>
                        <td class="col-md-1">{{ product.subtotal }}</td>
                        <td class="col-md-2">
                          <div class="btn-group" role="group">
                            <button
                              type="button"
                              class="btn btn-warning btn-sm"
                              v-b-modal.product-update-modal
                              @click="editProduct(product)"
                            >
                              Update
                            </button>
                            <button
                              type="button"
                              class="btn btn-danger btn-sm"
                              @click="onDeleteProduct(index)"
                            >
                              Delete
                            </button>
                          </div>
                        </td>
                      </b-row>
                    </tr>
                    <tr>
                      <b-row>
                        <td class="col-md-2"></td>
                        <td class="col-md-3"></td>
                        <td class="col-md-3"></td>
                        <td class="col-md-1"></td>
                        <td class="col-md-1">Total:</td>
                        <td class="col-md-2">
                          {{ orderList[0].total_amount }}
                        </td>
                      </b-row>
                    </tr>
                  </tbody>
                </table>
              </div>
            </template>
          </form>
        </div>
      </div>
    </div>
    <pre>orderId = {{ order_id }}</pre>
    <pre>loading = {{ loading }}</pre>
    <pre>orderList = {{ orderList }}</pre>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      order_id: this.$route.query.orderId,
      loading: false,
      orderList: []
    };
  },

  created() {
    this.fetchOrder();
  },

  methods: {
    fetchOrder() {
      var order_id = this.$route.query.orderId;
      console.log(order_id);
      const path = `http://localhost:4000/orders/${order_id}`;
      axios.put(path).then(
        res => {
          this.orderList = res.data;
        },
        error => {
          console.log(error);
        }
      );

      this.loading = false;
    }
  }
};
</script>