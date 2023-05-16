<template>
  <div>
    <a @click="toggle"><a href="#">Books</a></a>
    <div v-if="active">
    <a href="#">Anus</a>
    <a href="#">Anus</a>
    <a href="#">Anus</a>
    <a href="#">Anus</a>
    <a @click="toggl"><a href="#">Genre</a></a>
    <div v-if="activ">
      <a href="#">Hentai</a>
      <a href="#">Hentai</a>
      <a href="#">Hentai</a>
      <a href="#">Hentai</a>
      <a href="#">Hentai</a>
      <a href="#">Hentai</a>
      <a href="#">Hentai</a>
      <a href="#">Hentai</a>
      <a href="#">Hentai</a>
      <a href="#">Hentai</a>
    </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */ 
  export default {
    data () {
      return {
        active: false
      }
    },
    methods: {
      toggle () {
        this.active = !this.active
      },
      toggl () {
        this.activ = !this.activ
      }
    }
  }
</script>

<style>

</style>