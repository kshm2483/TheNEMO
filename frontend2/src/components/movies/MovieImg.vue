<template>
  <div class="movieImg">
    <!-- movie -->
    <img v-if="isHoverChk()" :src="imgData.info.poster_url" alt="moviePoster" @click="infoActive" :class="{ selectedMovie: isSelectedMovie }">
    <!-- category -->
    <div class="movieImg__score" v-if="!isHoverChk()">
      <img style="cursor:default" :src="imgData.info.imgSrc" alt="moviePoster" @mouseover="scoreActive">
    </div>
  </div>
</template>

<script>
export default {
  props: {
    imgData: {
      type: Object,
      required: true
    },
  },
  data: () => ({
    isSelectedMovie: false,
    hoverChk: false,
  }),
  computed: {
    setToggle () {
      return this.$store.getters.getMovieToggle
    },
    setMovieInfo() {
      return this.$store.getters.getMovieInfo
    }
  },
  watch: {
    setToggle (val) {
      if (!val) { this.isSelectedMovie = false }
    },
    setMovieInfo (val) {
      if (val && val.varified === this.imgData.varified && val.info.id === this.imgData.info.id ) {
        this.isSelectedMovie = true
      } else {
        this.isSelectedMovie = false
      }
    }
  },
  methods: {
    infoActive() {
      // store selected
      this.$store.commit('selectedMovie', this.imgData)
      // MoviePage.vue -> 스크롤 이동
      this.$EventBus.$emit('movieInfoActive', this.imgData)
    },
    scoreActive() {
      console.log('hover');
    },
    isHoverChk() {
      if (this.$router.history.current["name"] === "Movie") {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style lang="scss" scoped>
</style>
