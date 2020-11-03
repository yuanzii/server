<template>
  <div id="app">
    <div v-if="$route.meta.keepAlive">
      <navbar></navbar>
      <keep-alive>
        <router-view />
      </keep-alive>
    </div>
    <!-- 路由匹配到的组件将显示在这里 -->

    <router-view v-if="!$route.meta.keepAlive" />
  </div>
</template>

<script>
import navbar from "./components/navbar";

export default {
  name: "Home",
  components: {
    navbar
  }
  // methods: {},
  // mounted() {}
};
</script>