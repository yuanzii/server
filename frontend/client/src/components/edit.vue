<template>
  <div>
    <b-modal
      ref="editProductModal"
      id="product-update-modal"
      title="Update"
      hide-footer
    >
      <b-form @submit="onSubmitUpdate" @reset="onCancelUpdate" class="w-100">
        <div v-if="warning">
          <h4>⚠ 不能填超过订单数量的数字!</h4>
        </div>
        <b-form-group label="အရေအတွက်:">
          <b-form-input
            type="text"
            v-model="editForm.count"
            oninput="value=value.replace(/\D/g,'')"
            v-on:change="limited()"
            required
          ></b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>

    <div class="container-fluid">
      <div class="row">
        <div
          class="container pt-4 col-md-12 "
          style="box-shadow: 0 0 10px 0 rgba(0, 0, 0, .1);"
        >
          <form v-if="show_message">
            <h1>订单提交完成✔</h1>
          </form>
          <form v-if="show_form">
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
            </template>
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
                    <th style="width:5%;">
                      <input
                        type="checkbox"
                        @change="selectAll"
                        v-model="allSelected"
                      />
                    </th>
                    <th style="width:10%;">ID</th>
                    <th style="width:25%;">P_Name</th>
                    <th style="width:30%;">P_Detal</th>
                    <th style="width:10%;">Count</th>
                    <th style="width:10%;">Price</th>
                    <th style="width:10%;"></th>
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
                    <td style="width:5%;">
                      <input
                        type="checkbox"
                        v-model="selected"
                        :value="product"
                        number
                      />
                      <!-- :value="product"——>点击checkbox,把product装到selected[]里
                      或者：selected[]里有一个product == 点击了该checkbox,这就是[全选]的原理-->
                    </td>
                    <td style="width:10%;">{{ product.product_id }}</td>
                    <td style="width:25%;">{{ product.product_name }}</td>
                    <td style="width:30%;">{{ product.product_detal }}</td>
                    <td style="width:10%;">{{ product.count }}</td>
                    <td style="width:10%;">{{ product.price }}</td>
                    <td>
                      <div style="width:10%;" class="btn-group" role="group">
                        <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          v-b-modal.product-update-modal
                          @click="editProduct(product)"
                        >
                          Update
                        </button>
                      </div>
                    </td>
                  </b-row>
                </tr>
              </tbody>
            </table>
            <button
              type="submit"
              class="btn btn-primary mb-4 mr-2 col-2 float-right"
              v-b-modal.waybill-modal
              @click="view_waybill"
            >
              确定
            </button>
          </form>
        </div>
      </div>
    </div>

    <b-modal
      ref="wayBillModal"
      id="waybill-modal"
      title="WayBill"
      size="xl"
      hide-footer
    >
      <template v-if="selected[0]">
        <h3 class="pb-3">订单信息</h3>
        <div class="form-row">
          <div class="form-row col-md-6">
            <p>订单编号：</p>
            <p>{{ selected[0].order_id }}</p>
          </div>
        </div>
        <div class="form-row">
          <div class="form-row col-md-6">
            <p>创建日期：</p>
            <p>{{ selected[0].datetime }}</p>
          </div>
        </div>
        <div class="form-row">
          <div class="form-row col-12">
            <p>客户：</p>
            <p>{{ selected[0].customer_id }}</p>
            <p>{{ selected[0].customer_name }}</p>
          </div>
        </div>
        <table
          class="table container-fluid"
          style="word-break:break-all; word-wrap:break-all;"
        >
          <thead>
            <tr>
              <b-row class="ml-3 mr-3">
                <th class="col-md-2">ID</th>
                <th class="col-md-4">P_Name</th>
                <th class="col-md-4">P_Detal</th>
                <th class="col-md-2">Count</th>
                <!-- <th class="col-md-1">Price</th>
              <th class="col-md-3">Total</th> -->
              </b-row>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(product, index) in selected" :key="index">
              <b-row class="ml-3 mr-3">
                <td class="col-md-2">{{ product.product_id }}</td>
                <td class="col-md-4">{{ product.product_name }}</td>
                <td class="col-md-4">{{ product.product_detal }}</td>
                <td class="col-md-2">{{ product.count }}</td>
                <!-- <td class="col-md-1">{{ product.price }}</td> -->
                <!-- <td class="col-md-1">{{ product.subtotal }}</td> -->
              </b-row>
            </tr>
          </tbody>
          <button
            type="submit"
            class="btn btn-primary mb-4 mr-2 col-2 float-right"
            @click="submit_waybill(selected[0].order_id)"
          >
            发起订单
          </button>
        </table>
      </template>
    </b-modal>

    <pre>editForm = {{ editForm }}</pre>
    <pre>originalCount = {{ originalCount }}</pre>
    <pre>warning = {{ warning }}</pre>
    <pre>show_form = {{ show_form }}</pre>
    <pre>show_message = {{ show_message }}</pre>
    <pre>orderList = {{ orderList }}</pre>
    <span>Selected Datas: {{ selected }}</span>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      show_form: true,
      show_message: false,

      orderList: [],
      warning: false,

      selected: [], //已选中的数据
      allSelected: false, //是否是全选。false=默认不选中。

      editForm: {
        product_id: "",
        product_name: "",
        product_detal: "",
        count: "",
        price: "",
        subtotal: ""
      },
      originalCount: [],
      releasedGood: []
    };
  },
  computed: {},

  created() {
    this.fetchOrder();
  },
  // 监听data数据，数据改变时触发
  watch: {
    selected: function() {
      if (this.selected.length == this.orderList.length) {
        this.allSelected = true;
      } else {
        this.allSelected = false;
      }
    }
  },
  methods: {
    fetchOrder() {
      //拿到查询字段，订单的id后进行axios请求
      var order_id = this.$route.query.orderId;
      const path = `http://localhost:4000/orders/${order_id}`;
      axios.get(path).then(
        res => {
          console.log("fetchOrder");
          this.orderList = res.data;
          this.original_count();
        },
        error => {
          console.log(error);
        }
      );
    },
    original_count() {
      console.log("original_count()");
      for (let index = 0; index < this.orderList.length; index++) {
        console.log("for");
        const originalCount = {
          product_id: this.orderList[index].product_id,
          count: this.orderList[index].count
        };
        console.log(originalCount);

        const result = this.originalCount.find(
          ele => ele.product_id == this.orderList[index].product_id
        );
        console.log(result);
        // 检查originalCount，如果有相同的商品就换成最新数量
        if (result) {
          console.log("chongfu");
          this.originalCount.splice(result, 1);
          console.log(this.originalCount);
          this.originalCount.push(originalCount);
          console.log(this.originalCount);
        } else {
          console.log("else");
          this.originalCount.push(originalCount);
          console.log(this.originalCount);
        }
      }
      const index = this.originalCount.findIndex(ele => ele.count == 0);
      console.log(index);
      if (index == -1) {
        console.log("没有0");
      } else {
        this.originalCount.splice(index, 1);
        this.orderList.splice(index, 1);
      }
    },
    limited() {
      const index = this.originalCount.findIndex(
        ele => ele.product_id == this.editForm.product_id
      );
      if (this.editForm.count > this.originalCount[index].count) {
        this.warning = true;
        this.editForm.count = "";
      } else {
        this.warning = false;
        this.editForm.count;
      }
    },
    view_waybill(evt) {
      evt.preventDefault();
    },
    // submit_waybill() {
    //   var send_info = {
    //     waybill: this.selected
    //   };
    //   const path = "http://localhost:4000/waybill";
    //   axios.post(path, send_info).then(
    //     res => {
    //       console.log("submit_waybill()" + res);
    //       this.$refs.wayBillModal.hide();
    //       for (let z = 0; z < this.orderList.length; z++) {
    //         for (let x = 0; x < this.selected.length; x++) {
    //           if (this.orderList[z].product_id != this.selected[x].product_id) {
    //               console.log("有更改了，但是没提交数据")
    //               this.orderList[z].count = this.originalCount[z].count;

    //             } else {
    //               console.log("没有");
    //             }
    //           // const index = this.orderList.findIndex(
    //           //   ele => ele.product_id != this.selected[x].product_id
    //           // );
    //           // console.log(index);
    //           // if (index == -1) {
    //           //   console.log("没有");
    //           // } else {
    //           //   console.log("有更改了，但是没提交数据")
    //           //   this.orderList[index].count = this.originalCount[index].count;
    //           // }
    //           for (let y = 0; y < this.originalCount.length; y++) {
    //             if (
    //               this.originalCount[y].product_id ==
    //               this.selected[x].product_id
    //             ) {
    //               this.selected[x].count =
    //                 this.originalCount[y].count - this.selected[x].count;
    //               //this.selected[x].count 和被改变的orderList.count 是实时变动
    //             }
    //           }
    //           // for (let index = 0; index < this.orderList.length; index++) {
    //           //   if (this.orderList[index].product_id != this.selected[x].product_id) {
    //           //     console.log("有更改了，没提交数据")
    //           //     this.orderList[index].count = this.originalCount[index].count;

    //           //   } else {
    //           //     console.log("没有");
    //           //   }
    //           // }
    //         }
    //       }

    //       this.original_count();
    //       this.released_waybill();
    //       this.show_form = true;
    //       this.show_message = true;
    //       this.initOrder();
    //     },
    //     error => {
    //       console.log(error);
    //     }
    //   );
    // },
    submit_waybill() {
      var send_info = {
        waybill: this.selected
      };
      const path = "http://localhost:4000/waybill";
      axios.post(path, send_info).then(
        res => {
          console.log("submit_waybill()" + res);
          this.$refs.wayBillModal.hide();
            for (let x = 0; x < this.selected.length; x++) {
              for (let y = 0; y < this.originalCount.length; y++) {
                if (
                  this.originalCount[y].product_id ==
                  this.selected[x].product_id
                ) {
                  this.selected[x].count =
                    this.originalCount[y].count - this.selected[x].count;
                  //this.selected[x].count 和被改变的orderList.count 是实时变动
                }
              }
          }
          this.original_count();
          this.released_waybill();
          this.show_form = true;
          this.show_message = true;
          this.initOrder();
        },
        error => {
          console.log(error);
        }
      );
    },
    released_waybill() {
      var order_id = this.$route.query.orderId;
      var send_info = {
        released_waybill: this.orderList
      };
      const path = `http://localhost:4000/orders/${order_id}`;
      axios.put(path, send_info).then(
        res => {
          console.log("released_waybill()" + " " + res);
        },
        error => {
          console.log(error);
        }
      );
    },
    initOrder() {
      this.selected = [];
    },

    selectAll: function() {
      this.selected = [];

      if (this.allSelected) {
        this.selected = this.orderList; //选择orderList[]里的全部数据
      }
    },

    editProduct(product) {
      this.warning = false;
      this.editForm.product_id = product.product_id;
      this.editForm.product_name = product.product_name;
      this.editForm.product_detal = product.product_detal;
      this.editForm.count = product.count;
      this.editForm.price = product.price;
      this.editForm.subtotal = product.subtotal;
    },
    // 提交编辑好的数据
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editProductModal.hide();
      const index = this.orderList.findIndex(
        ele => ele.product_id == this.editForm.product_id
      );
      this.orderList[index].count = this.editForm.count;
    },
    onCancelUpdate(evt) {
      evt.preventDefault();
      this.warning = false;
      this.$refs.editProductModal.hide();
    }
  }
};
</script>
