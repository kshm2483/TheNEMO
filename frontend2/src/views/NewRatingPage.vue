<template>
  <div class="moviePage">
      <span class="newRatingTitle">영화 평점 주세요</span>
      <newRatingCategory :movieItems="searchMovie"/>
      <div class="lds-bg">
        <div v-if="loadScroll" class="lds-dual-ring"></div>
      </div>
      <footer class="nr--footer">
        <span> 평점을 준 갯수 {{cntRated}}</span>
        <p>평점을 준 영화가 많아 질수록 추천 영화의 정확도가 높아집니다.</p>
        <div class="btn btn--primary" @click="goMain()">여기까지</div>
        <div></div>
      </footer>
    </div>
</template>

<script>
import newRatingCategory from '@/components/newrating/newRatingCategory'
import { mapActions } from "vuex"

export default {
  components: {
    newRatingCategory
  },
  data: () => ({
    loadCall: false,
    loadScroll: false,
    persons: [],
    searchMovie: [],
    cntRated : 0,
  }),
  mounted() {
    this.searchMovies()
    // MovieImg.vue => 영화 정보 오픈 시 스크롤
    // this.$EventBus.$on('movieInfoActive', (payload) => {
    //   this.scrollCard(payload.varified)
    // })
    this.scroll(this.searchMovie)
  },
  created() {
    this.$EventBus.$on('increment', (text) => {
    this.cntRated += text;
});
  },
  beforeMount() {
    this.getInitialMovies()
  },
  methods: {
    ...mapActions(["searchMovies"]),
    goMain() {
        this.$router.push({
            name : 'Movie'
          })
      },
    getInitialMovies () {
      for (var i = 0; i < 12; i++) {
        this.searchMovie.push(this.$store.state.movieSearchList[i])
      }
    },
    scroll(movieItem) {
      window.onscroll = () => {
        let bOfW = Math.round(document.documentElement.scrollTop + window.innerHeight) >= document.documentElement.offsetHeight
        if (bOfW && this.loadCall === false) {
          this.loadCall = true
          this.loadScroll = true
          // axios.get(`https://randomuser.me/api/`)
          //   .then(response => {
          //     let i = this.movieItems[0].items.length+1
          //     let a = i
          //     for (a; a < i+12; a++) {
          //       this.movieItems[0].items.push(a)
          //     }
          //     this.loadScroll = false
          //     this.loadCall = false
          //   })
          let i = movieItem.length
          let a = i
          for ( a; a < i+12; a++ ) {
            movieItem.push(this.$store.state.movieSearchList[a])
          }
          setTimeout(() => {
            this.loadScroll = false
            this.loadCall = false
          }, 1000)
        }
      }
    }
  },

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
