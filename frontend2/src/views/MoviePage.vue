<template>
  <div class="moviePage">
    <div v-for="movieItem in movieItems" :key="movieItem.varified">
      <MovieList :id="movieItem.varified" :movieItem="movieItem"/>
      <div style="color:white;">
      </div>
      <transition name="fade" mode="out-in">
        <MovieCard :varified="movieItem.varified" :movieInfo="selectInfo"/>
      </transition>
    </div>
    <div class="lds-bg"/>
  </div>
</template>

<script>
import api from '@/api'
import { mapState, mapActions, mapGetters } from "vuex"
import MovieList from '@/components/movies/MovieList'
import MovieCard from '@/components/movies/MovieCard'

export default {
  components: {
    MovieList,
    MovieCard
  },
  data: () => ({
    movieItems: [],
    selectInfo: {}
  }),
  computed: {
    ...mapState({
      movieList: state => state.movieSearchList
    }),
    ...mapGetters({
      myMovie: 'getUserMovieData'
    })
  },
  mounted() {
    // MovieImg.vue => 영화 정보 오픈 시 스크롤
    this.$EventBus.$on('movieInfoActive', (payload) => {
      let waitPlease = true
      if (waitPlease) {
        this.selectMovie(payload.info.id)
      }
      setTimeout(() => {
        waitPlease = false
        this.scrollCard(payload.varified)
      }, 10)
    }),
    this.searchMovies()
  },
  watch: {
    movieList() {
      this.setMovieItems()
    }
  },
  methods: {
    ...mapActions(["searchMovies"]),
    scrollCard(locationId) {
      const element = document.getElementById(locationId)
      const elemRect = element.getBoundingClientRect()
      const offset = elemRect.bottom + window.pageYOffset - 100
      window.scrollTo({top: offset, behavior: 'smooth'})
    },
    setMovieItems() {
      // # 1
      // 내 추천 영화 => profile your_taste_movie
      let reAry = this.myMovie.your_taste_movie.split('|').map(Number).sort((a, b) => { return a - b }).filter(function(item, pos, ary) { return !pos || item != ary[pos - 1];})
      let recommendAry = []
      reAry.forEach((el) => { recommendAry.push(this.movieList.find(movie => movie.id === el)) })

      // # 2
      // 장르별 영화 => movie genre
      let reGenre = []
      let redict = {}
      recommendAry.forEach((el) => { reGenre.push(el.genres) })

      for (var i=0; i < reGenre.length; i++) {
        for (var j=0; j < reGenre[i].length; j++) {
          if (!redict[reGenre[i][j]]) {
            redict[reGenre[i][j]] = 1
          } else {
            redict[reGenre[i][j]] += 1
          }
        }
      }
      let maxKey = Object.keys(redict).reduce((a, b) => redict[a] > redict[b] ? a : b)
      // setting genreMovieItems
      this.getMovieListItem('genre', maxKey)

      // # 3
      // 나름 높은거
      let highAry = []
      for (var k=0; k < this.movieList.length; k++) {
        if (Number(this.movieList[k].title.slice(-5, -1)) > 1997) {
          highAry.push(this.movieList[k])
        }
      }
      this.movieItems.push({ varified: `당신에게 딱 맞는 위한 영화`, items: recommendAry })
      this.movieItems.push({ varified: "since 98's", items: highAry })
    },
    async selectMovie(id) {
      const resp = await api.searchMovies({'id': id})
      this.selectInfo = resp.data
    },
    async getMovieListItem(param, val) {
      if (param === 'genre') {
        const resp = await api.searchMovies({ 'genre': val })
        this.movieItems.push({ varified: val, items: resp.data })
      }
      if (param === 'occupation') {
        const resp = await api.searchMovies({ 'occupation': val })
        this.movieItems.push({ varified: val, items: resp.data })
      }
    }
  }
}
</script>
