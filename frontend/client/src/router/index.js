import Vue from "vue";
import VueRouter from "vue-router";
import home from "../views/home.vue";
import detail from "../components/detail.vue";
import release from "../components/release.vue";
import edit from "../components/edit.vue";

Vue.use(VueRouter);

// const detail = {
//   template: "<h2>{{this.$route.query.id}}</h2>"
// }


const routes = [
  {
    path: "/",
    name: "home",
    component: home,
    meta: {
      keepAlive: true
    }
  },
  {
    path: "/all_orders",
    name: "all_orders",
    component: () =>
      import("../views/all_orders.vue"),
    meta: {
      keepAlive: true
    }
  },
  {
    path: "/all_orders/detail",
    name: "detail",
    component: detail,
    meta: {
      keepAlive: false
    }
  },
  {
    path: "/all_orders/release",
    name: "release",
    component: release,
    meta: {
      keepAlive: true
    }
  },
  {
    path: "/all_orders/edit",
    name: "edit",
    component: edit,
    meta: {
      keepAlive: false
    }
  },
  {
    path: "/missed_orders",
    name: "missed_orders",
    component: () =>
      import("../views/missed_orders.vue"),
    meta: {
      keepAlive: true
    }
  },
];

const router = new VueRouter({
  // linkActiveClass: 'active',
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
