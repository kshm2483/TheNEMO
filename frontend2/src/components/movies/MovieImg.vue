<template>
  <div class="movieImg">
    <!-- movie -->
    <img v-if="isRouterChk()" :src="imgData.info.poster_url" alt="moviePoster" @click="infoActive" :class="{ selectedMovie: isSelectedMovie }" onerror="this.onerror=null; this.src='http://kaverisias.com/wp-content/uploads/2018/01/catalog-default-img.gif'">
    <!-- category -->
    <div class="movieImg newImg" v-if="!isRouterChk()">
      <img @click="toggleModal(imgData.id)" style="cursor:default width:260px;height:373px; min-width:250px; max-width: 250px;" :src="imgData.imgSrc" alt="moviePoster" onerror="this.onerror=null; this.src='http://kaverisias.com/wp-content/uploads/2018/01/catalog-default-img.gif'">

      <!-- Modal -->
    <MovieDetailModal v-if="showModal" @close="val => showModal = val" :showModal = "showModal" :movieInfo="selectInfo" :imgData="{ imgSrc: imgData.imgSrc, title: imgData.title, id: imgData.id, genres: imgData.genres, overview: imgData.overview }"></MovieDetailModal>
      <div class="testMovie__detail" @click="toggleModal(imgData.id)">
        <h2 style="color: white;">{{ imgData.title }}</h2>
        <ul style=" display:inline;">
          <li v-for="genre in imgData.genres.slice(0, imgData.genres.length-1)" :key="genre" style="color: white; text-align:left; margin-bottom:2px; display:inline;" > {{genre}} |</li>
          <li v-for="genre in imgData.genres.slice(imgData.genres.length-1, imgData.genres.length)" :key="genre" style="color: white; text-align:left; margin-bottom:2px; display:inline;" > {{genre}} </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import MovieDetailModal from '@/components/movies/MovieDetailModal'
import api from '@/api'

export default {
  components: {
      MovieDetailModal
    },
  props: {
    imgData: {
      type: Object,
      required: true
    },
  },
  data: () => ({
    isSelectedMovie: false,
    hoverChk: false,
    showModal: false,
    selectInfo: {}


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
    // ...mapActions(["searchMovies"]),
    async selectMovie(id) {
      const resp = await api.searchMovies({'id': id})
      this.selectInfo = resp.data
    },
    infoActive() {
      // store selected
      this.$store.commit('selectedMovie', this.imgData)
      // MoviePage.vue -> 스크롤 이동
      this.$EventBus.$emit('movieInfoActive', this.imgData)
    },
    isRouterChk() {
      if (this.$router.history.current["name"] === "Movie") {
        return true
      } else {
        return false
      }
    },
    toggleModal(id) {
      this.selectMovie(id)
      this.showModal = true
    }
  }

}
</script>

<style lang="scss" scoped>
.testMovie__detail {
  display: inline-block;
  position: relative;
  white-space: nowrap;
  overflow: hidden;
  top: -162px;
  left: 2px;

  text-align: start;
  padding: var(--space-md);
  background-color: rgba(0, 0, 0, 0.8);
  width: auto;
  width: 210px;
  height: 120px;
  text-align: center;
  opacity: 0;
}
.testMovie__detail:hover {
  cursor:pointer;
}


</style>
