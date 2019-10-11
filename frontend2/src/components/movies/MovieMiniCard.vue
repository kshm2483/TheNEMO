<template>
  <div>
    <p>{{ setMovie.title }}</p>
    <img class="testImg" :src="setMovie.poster_url" alt="movieposter" onerror="this.onerror=null; this.src='http://kaverisias.com/wp-content/uploads/2018/01/catalog-default-img.gif'">
  </div>
</template>

<script>
export default {
  props: {
    movieId: {
      type: Number,
      required: true
    }
  },
  computed: {
    setMovie() {
      return this.$store.state.movieSearchList[this.movieId-1]
    }
  }
}
</script>

<style scoped lang="scss">
p {
  margin: 0;
}
.testImg {
  position: absolute;
  top: 81%;
  right: 18%;
  width: 10vw;
  height: 30vh;
}
</style>
