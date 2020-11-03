<template>
  <div>
    <b-modal
      ref="editProductModal"
      id="product-update-modal"
      title="Update"
      hide-footer
    >
      <b-form @submit="onSubmitUpdate" @reset="onCancelUpdate" class="w-100">
        <b-form-group label="အရေအတွက်:">
          <b-form-input
            type="text"
            v-model="editForm.count"
            oninput="value=value.replace(/\D/g,'')"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group label="စျေးနှုန်း:">
          <b-form-input
            type="text"
            v-model="editForm.price"
            oninput="value=value.replace(/\D/g,'')"
            required
          ></b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <!-- Order 查看订单页面 -->
    <b-modal
      ref="OrderModal"
      id="order-modal"
      size="xl"
      title="Order"
      hide-footer
    >
      <b-form @submit="OnSubmitOrder" @reset="onCancelUpdate">
        <b-row>
          <!-- <div v-if="customers.customer_name == ''">
            <b-modal ref="emptyModal" title="出错啦！">
              <b-form class="w-100">
                <h3>请输入客户信息</h3>
              </b-form>
            </b-modal>
          </div> -->
          <span class="col-6">{{ customers.customer_id }}</span>
          <span class="col-6">{{ customers.customer_name }}</span>
        </b-row>
        <b-row>
          <span class="col-md-2">创建时间:</span>
          <span class="col-md-10">{{ datetime }}</span>
        </b-row>
        <table
          class="table container-fluid mt-3"
          style="word-break:break-all; word-wrap:break-all;"
        >
          <b-row>
            <th class="col-md-2">ID</th>
            <th class="col-md-3">P_Name</th>
            <th class="col-md-3">P_Detal</th>
            <th class="col-md-1">Count</th>
            <th class="col-md-1">Price</th>
            <th class="col-md-2">Total</th>
          </b-row>
          <tr v-for="(product, index) in products" :key="index">
            <b-row>
              <td class="col-md-2">{{ product.product_id }}</td>
              <td class="col-md-3">{{ product.product_name }}</td>
              <td class="col-md-3">{{ product.product_detal }}</td>
              <td class="col-md-1">{{ product.count }}</td>
              <td class="col-md-1">{{ product.price }}</td>
              <td class="col-md-2">{{ product.subtotal }}</td>
            </b-row>
          </tr>
          <tr>
            <b-row>
              <td class="col-md-2"></td>
              <td class="col-md-3"></td>
              <td class="col-md-3"></td>
              <td class="col-md-1"></td>
              <td class="col-md-1">Total:</td>
              <td class="col-md-2">{{ total_amount }}</td>
            </b-row>
          </tr>
        </table>

        <b-button-group>
          <b-button type="submit" variant="info">SubmitOrder</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <!-- 表格 -->
    <table class="table container-fluid">
      <thead>
        <tr>
          <b-row class="ml-3 mr-3">
            <th class="col-6">CustomerID</th>
            <th class="col-6">CustomerName</th>
          </b-row>
        </tr>
      </thead>
      <tbody>
        <tr>
          <b-row class="ml-3 mr-3">
            <td class="col-6">{{ customers.customer_id }}</td>
            <td class="col-6">{{ customers.customer_name }}</td>
          </b-row>
        </tr>
      </tbody>
    </table>
    <table
      class="table container-fluid"
      style="word-break:break-all; word-wrap:break-all;"
    >
      <thead>
        <tr>
          <b-row class="ml-3 mr-3">
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
        <tr v-for="(product, index) in products" :key="index">
          <b-row class="ml-3 mr-3">
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
      </tbody>
    </table>
    <b-button-group>
      <b-button
        type="button"
        variant="info"
        v-b-modal.order-modal
        @click="onViewOrder"
        >ViewOrder</b-button
      >
    </b-button-group>
    <b-button-group>
      <b-button type="reset" @click="selectGood()">新窗口带参数2</b-button>
    </b-button-group>
    <pre>list = {{ list }}</pre>
    <pre>customers = {{ customers }}</pre>
    <pre>products = {{ products }}</pre>
    <pre>editForm = {{ editForm }}</pre>
    <pre>total_amount = {{ total_amount }}</pre>
    <pre>datetime = {{ datetime }}</pre>
  </div>
</template>

<script>
import axios from "axios";
import { bus } from "../router/bus";
export default {
  data() {
    return {
      list: {
        // head: [
        //   {
        //     order_id: 20201017090714,
        //     customer_id: "A280",
        //     customer_name: "?????????",
        //     total_amount: 102,
        //     datetime: 1602925614000
        //   },
        //   {
        //     order_id: 20201017091102,
        //     customer_id: "A283",
        //     customer_name: "အားခွင်း ဟောင်လိတ်",
        //     total_amount: 18600,
        //     datetime: 1602925874000
        //   },
        //   {
        //     order_id: 20201017091230,
        //     customer_id: "A285",
        //     customer_name: "ကိုစိုး ကချင်ရွာ",
        //     total_amount: 53500,
        //     datetime: 1602925936000
        //   }
        // ]
      },
      orders: "",
      customers: {},
      products: [],
      editForm: {
        product_id: "",
        product_name: "",
        product_detal: "",
        count: "",
        price: "",
        subtotal: ""
      },
      total_amount: {},
      datetime: {}
    };
  },
  //   接收组件firstTab传到bus.js里的值
  created() {
    bus.$on("products", data => {
      this.products = data;
    });
    // bus.$off("saveTheme")
    bus.$on("customers", data => {
      this.customers = data;
    });
    // this.click();
  },
  methods: {
    // click() {
    //   this.$store.commit("print/setPrint", {
    //     list: this.list
    //   });
    // },
    //   点击编辑按钮,editForm单独获取products里的值,分成两个v-model,为了不被第一个v-model影响
    editProduct(product) {
      this.editForm.product_id = product.product_id;
      this.editForm.count = product.count;
      this.editForm.price = product.price;
    },
    // 提交编辑好的数据
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editProductModal.hide();
      this.editForm.subtotal = this.editForm.count * this.editForm.price;

      //   利用findIndex()找出要编辑的products[]里的索引,改变products[]里的数据
      const index = this.products.findIndex(
        //ele是一个临时变量，表示数组的一个元素，
        ele => ele.product_id == this.editForm.product_id
      );
      //  现在要更新index这个索引里的数据
      this.products[index].count = this.editForm.count;
      this.products[index].price = this.editForm.price;
      this.products[index].subtotal = this.editForm.subtotal;
    },
    // 取消按钮，取消编辑
    onCancelUpdate() {
      this.$refs.editProductModal.hide();
      this.$refs.OrderModal.hide();
    },
    // 删除按钮
    onDeleteProduct(index) {
      // 删除所点击的products[]里的该索引
      this.products.splice(index, 1);
    },
    // 订单合计
    totalSumAll() {
      let total_amount = 0;
      this.products.forEach(item => {
        //遍历subtotal这个字段，并累加
        total_amount += item.subtotal;
      });
      //返回
      this.total_amount = total_amount;
    },
    // 查看订单按钮
    onViewOrder() {
      this.datetime = this.$moment().format("YYYY/MM/DD HH:mm:ss");
      this.totalSumAll();
    },
    // 提交订单
    OnSubmitOrder(evt) {
      evt.preventDefault();
      const Orders = {
        customer_id: this.customers.customer_id,
        customer_name: this.customers.customer_name,
        total_amount: this.total_amount,
        datetime: this.datetime
      };
      // 表格内没有填客户和商品信息不能提交订单
      if (this.products == "") {
        alert("请填写完整的数据");
        this.$refs.OrderModal.hide();
      } else {
        // 如果表格内容不为空，把数据输入到this.orders
        this.orders = Orders;
        this.$refs.OrderModal.hide();
        this.SubmitOrder();
        this.initOrder();
        this.dataToBrother();
      }
    },
    // 传到bus.js,清空firstTab组件里的表单
    dataToBrother() {
      bus.$emit("init_products", this.products);
      bus.$emit("init_customers", this.customers);
    },
    initOrder() {
      this.products = [];
      (this.customers = {
        customer_id: "",
        customer_name: ""
      }),
        (this.total_amount = {});
    },
    SubmitOrder() {
      var send_info = {
        orders: this.orders,
        products: this.products
      };
      const path = "http://localhost:4000/orders";
      axios
        .post(path, send_info)
        .then(res => {
          // this.DetalOrder();
          console.log(res);
        })
        .catch(error => {
          console.error(error);
        });
    },
    DetalOrder() {
      console.log("DetalOrder");
      const path = "http://localhost:4000/last_product";
      axios
        .get(path)
        .then(res => {
          console.log(res);
          const head = {
            order_id: res.data[0].order_id,
            customer_id: res.data[0].customer_id,
            customer_name: res.data[0].customer_name,
            total_amount: res.data[0].total_amount,
            datetime: res.data[0].datetime
          };
          this.list.head.push(head);

          this.$store.commit("print/setPrint", {
            //print 表示vuex的文件名
            list: this.list
          });
        })

        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>