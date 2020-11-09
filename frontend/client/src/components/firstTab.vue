<template>
  <div>
    <b-modal ref="emptyModal" title="出错啦！" hide-footer>
      <b-form class="w-100">
        <h3>{{ empty }}</h3>
      </b-form>
    </b-modal>

    <b-form
      @submit="onSubmit"
      @reset="onReset"
      class="container-fluid"
      onkeypress="return event.keyCode != 13;"
    >
      <b-row>
        <b-form-group class="col-md-6" label="Customer Id-Name:">
          <b-form-input
            type="text"
            v-model="customers.customer_id"
            @keyup.enter="c_change"
            @keyup.delete="deletide_customer_id"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group class="col-md-6" label="CustomerName:">
          <b-form-input
            type="text"
            v-model="customers.customer_name"
            @keyup.delete="deletide_customer_name"
            required
          ></b-form-input>
        </b-form-group>
      </b-row>
      <b-row>
        <b-form-group class="col-md-2" label="ID:">
          <b-form-input
            type="text"
            v-model="addProductForm.product_id"
            @keyup.enter="p_change"
            @keyup.delete="delete_product_id"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group class="col-md-3" label="P_Name:">
          <b-form-input
            type="text"
            v-model="addProductForm.product_name"
            @keyup.delete="delete_product_name"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group class="col-md-3" label="P_Detail:">
          <b-form-input
            type="text"
            v-model="addProductForm.product_detal"
            @keyup.delete="delete_product_detail"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group class="col-md-1" label="Count:">
          <b-form-input
            type="text"
            v-model="addProductForm.count"
            oninput="value=value.replace(/\D/g,'')"
            v-on:input="count_change"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group class="col-md-1" label="Price:">
          <b-form-input
            type="text"
            v-model="addProductForm.price"
            oninput="value=value.replace(/\D/g,'')"
            v-on:input="count_change"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group class="col-md-2" label="Total:">
          <b-form-input
            type="text"
            v-model="addProductForm.subtotal"
            oninput="value=value.replace(/\D/g,'')"
            required
          ></b-form-input>
        </b-form-group>
      </b-row>
      <b-button-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-button-group>
    </b-form>
    <pre>empty = {{ empty }}</pre>
    <pre>customers = {{ customers }}</pre>
    <pre>products = {{ products }}</pre>
    <pre>addProductForm = {{ addProductForm }}</pre>
  </div>
</template>

<script>
import axios from "axios";
import { bus } from "../router/bus";
export default {
  name: "firstTab",
  data() {
    return {
      empty: {},
      customers: {
        customer_id: "",
        customer_name: ""
      },
      products: [],
      addProductForm: {
        product_id: "",
        product_name: "",
        product_detal: "",
        count: "",
        price: "",
        subtotal: ""
      }
    };
  },
  //   从bus.js获取数据,清空表单
  created() {
    bus.$on("init_products", data => {
      this.products = data;
    });
    bus.$on("init_customers", data => {
      this.customers = data;
    });
  },
  methods: {
    // 查询客户
    c_change: function() {
      this.customers.customer_id = this.customers.customer_id.toUpperCase();
      var send_info = {
        customer_id: this.customers.customer_id
      };
      const path = "http://localhost:4000/get_customer";
      axios
        .post(path, send_info)
        // 返回到前端
        .then(response => {
          this.customers.customer_name = response.data["address"];
          if (this.customers.customer_name == null) {
            this.empty = response.data;
            this.$refs.emptyModal.show();
          }
        })
        .catch(error => {
          console.error(error);
        });
    },
    deletide_customer_id() {
      this.customers.customer_name = "";
    },
    deletide_customer_name() {
      this.customers.customer_id = "";
    },
    delete_product_id() {
      this.addProductForm.product_name = "";
      this.addProductForm.product_detal = "";
      this.addProductForm.price = "";
      this.count_change();
    },
    delete_product_name() {
      this.addProductForm.product_id = "";
      this.addProductForm.product_detal = "";
      this.addProductForm.price = "";
      this.count_change();
    },
    delete_product_detail() {
      this.addProductForm.product_id = "";
      this.addProductForm.product_name = "";
      this.addProductForm.price = "";
      this.count_change();
    },
    //   查询商品
    p_change: function() {
      this.addProductForm.product_id = this.addProductForm.product_id.toUpperCase();
      //   把客户端输入的ID存成json 后端才能接收
      var send_info = {
        product_id: this.addProductForm.product_id
      };
      const path = "http://localhost:4000/get_product";
      axios
        .post(path, send_info)
        // 返回到前端
        .then(response => {
          console.log(response.data);
          this.addProductForm.product_name = response.data["mm_name"];
          this.addProductForm.product_detal = response.data["d_name"];
          this.addProductForm.price = response.data["price"];
          if (this.addProductForm.product_name == null) {
            this.empty = response.data;
            this.$refs.emptyModal.show();
          }
          this.count_change();
        })
        .catch(error => {
          console.error(error);
        });
    },
    // 计算价钱
    count_change() {
      this.addProductForm.subtotal =
        this.addProductForm.count * this.addProductForm.price;
    },
    initForm() {
      this.addProductForm.product_id = "";
      this.addProductForm.product_name = "";
      this.addProductForm.product_detal = "";
      this.addProductForm.count = "";
      this.addProductForm.price = "";
      this.addProductForm.subtotal = "";
    },
    onSubmit(evt) {
      evt.preventDefault();
      // 提交表单后需要初始化addProductForm{},所以把里面的数据转移给Products
      const Products = {
        product_id: this.addProductForm.product_id,
        product_name: this.addProductForm.product_name,
        product_detal: this.addProductForm.product_detal,
        count: this.addProductForm.count,
        price: this.addProductForm.price,
        subtotal: this.addProductForm.subtotal
      };
      // 查重 find()
      const result = this.products.find(
        ele => ele.product_id == Products.product_id //ele是一个临时变量，表示数组的一个元素，
      );
      if (result) {
        //如果不为null，说明products[]中已经有了此种商品
        result.count = Number(Products.count) + Number(result.count);
        result.subtotal = result.count * result.price;
      } else {
        //如果products[]中还没有这种商品,往里添加一个对象
        this.products.push(Products);
      }
      //   传参到secondTab组件
      this.dataToBrother();
      this.initForm();
    },
    // 清空表单
    onReset(evt) {
      evt.preventDefault();
      this.initForm();
    },
    //   firstTab组件的值传递到bus.js,secondTab从bus.js获取值
    dataToBrother() {
      bus.$emit("products", this.products);
      bus.$emit("customers", this.customers);
    }
  }
};
</script>