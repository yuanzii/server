<template>
  <div>
    <div class="container-fluid col-6 pb-3 " v-for="(products, index) in this.orders.missed_orders"
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
                <p>{{ products[0].order_id }}</p>
              </div>
            </div>
            <div class="form-row">
              <div class="form-row col-md-6">
                <p>创建日期：</p>
                <p>{{ products[0].datetime }}</p>
              </div>
            </div>
            <div class="form-row">
              <div class="form-row col-12">
                <p>客户：</p>
                <p>{{ products[0].customer_id }}</p>
                <p>{{ products[0].customer_name }}</p>
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
              <button
                type="submit"
                class="btn btn-warning mb-4 mr-2 col-2 float-right"
                @click="onMissedOrder"
              >
                打印
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <p>hello</p>
    <pre>missed_orders = {{ missed }}</pre>
    <b-button
      type="button"
      class="btn btn-sm btn-danger"
      @click="onReleaseOrder"
      >剩余订单
    </b-button>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  data() {
    return {
      missed: []
    };
  },
  computed: {
    ...mapState({
      orders: state => state.orders.missed_orders
    })
  },
  created() {
  },
  methods: {
    onReleaseOrder() {
      this.missed = this.orders.missed_orders;
      console.log("aa" + this.missed);
    },
    onMissedOrder(){

    },
  }
};
</script>