<template>
  <div id="navbar">
    <!-- Image and text -->
    <b-navbar toggleable="lg" type="light" variant="light">
      <b-navbar-brand class="nav">
        <img src="#" class="d-inline-block align-top" alt="logo" />
        <router-link to="/">ရွှေသဲ ကားအော်ဒါ</router-link>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="nav">
          <b-nav-item>
            <router-link to="/" exact>ပင်မစာမျက်နှာ</router-link>
          </b-nav-item>
          <b-nav-item>
            <router-link to="/all_orders">全部订单</router-link>
          </b-nav-item>
          <b-nav-item>
            <routerLink to="/missed_orders" exact>未接订单</routerLink>
          </b-nav-item>
          <b-nav-item>
            <routerLink to="/navbar">已接订单</routerLink>
          </b-nav-item>
          <b-nav-item>
            <routerLink to="/navbar">订单追踪</routerLink>
          </b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: "navbar",
  // components: {
  //   home,
  // },
};
</script>
<style>
.nav a{
  color: rgb(116, 112, 112);
}
.nav a:hover{
  color: rgb(80, 78, 78);
  text-decoration: none;
  font-size: 18px;
}
.nav a.router-link-exact-active{
	/* background-color: orange; */
	color: black;
  font-size: 18px;
  text-decoration: none;
}
</style>
