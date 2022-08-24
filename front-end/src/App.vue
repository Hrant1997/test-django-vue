<template>
  <div id="app">
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item :to="{ name: 'home' }" class="text-white">Home</b-nav-item>
        <b-nav-item :to="{ name: 'shipments' }">Shipments</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <b-container>
      <router-view></router-view>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
