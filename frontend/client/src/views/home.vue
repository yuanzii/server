<template>
  <div>
    <b-tabs
      active-nav-item-class="font-weight-normal text-uppercase text-danger"
      active-tab-class="font-weight-normal text-success"
      content-class="mt-3"
    >
      <b-tab title="First" active>
        <firstTab></firstTab>
      </b-tab>
      <b-tab title="Second">
        <secondTab></secondTab>
      </b-tab>
      <b-tab title="Third">
        <thirdTab></thirdTab>
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
// @ is an alias to /src
import firstTab from "../components/firstTab";
import secondTab from "../components/secondTab";
import thirdTab from "../components/thirdTab";

export default {
  name: "home",
  components: {
    firstTab,
    secondTab,
    thirdTab
  },
  data() {
    return {
      // list: {
      //   head: []
      // }
    };
  },
};
</script>
