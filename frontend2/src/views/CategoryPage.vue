<template>
  <div class="moviePage" @wheel="scroll()">
    <div>
      <MovieCateForm/>
      <MovieCategory :movieItems="showSearchMovies"/>
      <div class="lds-bg">
        <div v-if="loadScroll" class="lds-dual-ring"></div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCateForm from '@/components/movies/MovieCategoryForm'
import MovieCategory from '@/components/movies/MovieCategoryList'

export default {
  components: {
    MovieCateForm,
    MovieCategory
  },
  data: () => ({
    loadCall: false,
    loadScroll: false,

    searchMovies: [],
    showSearchMovies: [],

    throwData: false,
  }),
  mounted() {
    // App.vue => 영화 정보 받음
    this.$EventBus.$on('movieSearchList', (payload) => {
      if (payload.str === null || payload.str === '') {
        this.getInitialMovies()
      } else {
        this.setSearchMovies(payload.payload)
      }
    })
    // MovieCategoryForm.vue => gere filter
    this.$EventBus.$on('selectGenre', (payload) => {
      this.genreFilter(payload)
    })
    this.scroll()
  },
  beforeMount() {
    this.getInitialMovies()
  },
  methods: {
    getInitialMovies () {
      this.searchMovies = this.$store.state.movieSearchList
      this.showSearchMovies = this.$store.state.movieSearchList.slice(0, 12)
      this.throwData = false
    },
    setSearchMovies(movieList) {
      this.searchMovies = movieList
      if ( movieList.length > 11 ) {
        this.showSearchMovies = this.searchMovies.slice(0, 12)
      } else {
        this.showSearchMovies = this.searchMovies
        this.throwData = true
      }
    },
    scroll() {
        let bOfW = Math.round(document.documentElement.scrollTop + window.innerHeight) >= document.documentElement.offsetHeight
        if ( bOfW && this.loadCall === false && this.throwData === false ) {
          this.loadCall = true
          this.loadScroll = true
          let i = this.showSearchMovies.length
          let a = i
          if ( a+12 > this.searchMovies.length ) {
            for ( a; a < this.searchMovies.length; a++) {
              this.showSearchMovies.push(this.searchMovies[a])
            }
            this.throwData = true
          } else {
            for ( a; a < i+12; a++ ) {
              this.showSearchMovies.push(this.searchMovies[a])
            }
          }
          setTimeout(() => {
            this.loadScroll = false
            this.loadCall = false
          }, 1000)
        }
    },
    genreFilter(genre) {
      let filterGenre
      if (genre != 'All genres') {
        filterGenre = this.searchMovies.filter((item) => {
          return item.genres.includes(genre)
        })
      } else {
        filterGenre = this.searchMovies
      }
      if (filterGenre.length > 11) {
        this.showSearchMovies = filterGenre.slice(0, 12)
      } else {
        this.showSearchMovies = filterGenre
        this.throwData = true
      }
    }
  }
}
</script>
<style lang="scss">
.lds-bg {
  position: relative;
  height: 20vh;
  width: 100%;
  background: linear-gradient(to bottom, rgba(70, 70, 70, 0), rgb(18, 18, 18));
}
.lds-dual-ring {
  display: inline-block;
  position: absolute;
  bottom: 5vh;
  width: 64px;
  height: 64px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 46px;
  height: 46px;
  margin: 1px;
  border-radius: 50%;
  border: 5px solid #fff;
  border-color: #fff transparent #fff transparent;
  animation: lds-dual-ring 0.5s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
