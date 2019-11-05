<template>
  <div class="movieItem" v-if="infoToggle">
    <div class="movieInfo">
      <div class="movieTcontent">
        <h1>{{ movieInfo.title }}</h1>
        <div class="movieRG">
          <p class="movieR">평균 점수 {{ movieInfo.average_rating }}</p>
          <p class="movieG" v-for="genre in movieInfo.genres_array" :key="genre"># {{ genre }}</p>
        </div>
      </div>
      <transition-group name="test">
        <div class="movieContent" v-if="infoBtnToggle === 1" key="contentInfo">
          <div class="movieOV">
            <p>{{ movieInfo.overview }}</p>
          </div>
        </div>
        <div class="movieContent movieContent__score" v-if="infoBtnToggle === 2" key="contentSimilar">
          <!-- <h1>2page</h1> -->
          <div>
            <div class="movieAvgR">
              <h3>평균 점수 {{ movieInfo.average_rating }}</h3>
              <span>{{ movieInfo.view_cnt }} 명</span>
            </div>
            <div>
              <div v-for="(i, index) in scorePaginatedData" :key="i.id">
                <div class="rateBox rateBox__0" v-if="index === 0">
                  {{ i.user }}
                  {{ i.rating }}
                  <star class="rateStar" :score="i"/>
                </div>
                <div class="rateBox rateBox__1" v-if="index === 1">
                  {{ i.user }}
                  {{ i.rating }}
                  <star class="rateStar" :score="i"/>
                </div>
                <div class="rateBox rateBox__2" v-if="index === 2">
                  {{ i.user }}
                  {{ i.rating }}
                  <star class="rateStar" :score="i"/>
                </div>
                <div class="rateBox rateBox__3" v-if="index === 3">
                  {{ i.user }}
                  {{ i.rating }}
                  <star class="rateStar" :score="i"/>
                </div>
              </div>
              <div>
                <button class="pageBtn pageBtn__rprev" :disabled="scorePageNum === 0" @click="pagination('s', false)"><fa-icon icon="angle-left"/></button>
                <button class="pageBtn pageBtn__rnext" :disabled="scorePageNum >= scorePageCount - 1" @click="pagination('s', true)"><fa-icon icon="angle-right"/></button>
              </div>
            </div>
          </div>
        </div>
        <div class="movieContent movieContent__card" v-if="infoBtnToggle === 3" key="contentDetail">
          <!-- <h1>3page</h1> -->
          <div>
            <div style="display: flex;">
              <div v-for="i in moviePaginatedData" :key="i" style="width: 15%; position: relative; left: 25%;">
                <MovieMiniCard :movieId="i"/>
              </div>
              <div>
                <button class="pageBtn pageBtn__mprev" :disabled="moviePageNum === 0" @click="pagination('m', false)"><fa-icon icon="angle-left"/></button>
                <button class="pageBtn pageBtn__mnext" :disabled="moviePageNum >= moviePageCount - 1" @click="pagination('m', true)"><fa-icon icon="angle-right"/></button>
              </div>
            </div>
          </div>
        </div>
      </transition-group>
    </div>
    <div class="movieBackImg" :style="bgStyle">
    </div>
    <div class="movieBtnGroups">
      <button :class="{ activate: infoBtnToggle === 1 }" @click="infoBtnSwitch(1)">콘텐츠 정보</button>
      <button :class="{ activate: infoBtnToggle === 2 }" @click="infoBtnSwitch(2)">평점 정보</button>
      <button :class="{ activate: infoBtnToggle === 3 }" @click="infoBtnSwitch(3)">비슷한 콘텐츠</button>
    </div>
    <div class="movieClose" @click="closeInfoBtn">
      <fa-icon icon="times"/>
    </div>
  </div>
</template>

<script>
import MovieMiniCard from '@/components/movies/MovieMiniCard'
import star from '@/components/modules/star'

const BACKDROP_BASE = "https://image.tmdb.org/t/p/original/"

export default {
  components: {
    MovieMiniCard,
    star,
  },
  props: {
    movieInfo: {
      type: Object,
      required: true
    },
    varified: {
      type: String,
      required: true
    },
    scorePageSize: {
      type: Number,
      required: false,
      default: 4
    },
    moviePageSize: {
      type: Number,
      required: false,
      default: 5
    }
  },
  data: () => ({
    scorePageNum: 0,
    moviePageNum: 0,
    infoDetail: [],
    infoToggle: false,
    infoBtnToggle: 1,
    movieBACKURL: ''
  }),
  mounted() {
    // MovieList.vue에서 받은 $EventBus
    this.$EventBus.$on('closeMovieCard', () => {
      this.infoToggle = false
    })
  },
  computed: {
    setToggle () {
      return this.$store.getters.getMovieToggle
    },
    setMovieInfo() {
      return this.$store.getters.getMovieInfo
    },
    bgStyle() {
      return {
        'background-image': `url(${ BACKDROP_BASE }/${ this.movieBACKURL.info.backdrop_url })`,
        'background-repeat': 'no-repeat',
        'background-size': 'cover',
        'mask-image': 'linear-gradient(to left, rgba(0,0,0,1), rgba(0,0,0,0))'
      }
    },
    scorePageCount () {
      let listLeng = this.movieInfo.rating.length, listSize = this.scorePageSize, page = Math.floor((listLeng - 1) / listSize) + 1
      return page
    },
    scorePaginatedData () {
      const start = this.scorePageNum * this.scorePageSize, end = start + this.scorePageSize;
      return this.movieInfo.rating.slice(start, end)
    },
    moviePageCount () {
      let listLeng = this.movieInfo.similarmovie.length, listSize = this.moviePageSize, page = Math.floor((listLeng - 1) / listSize) + 1
      return page
    },
    moviePaginatedData () {
      const start = this.moviePageNum * this.moviePageSize, end = start + this.moviePageSize;
      return this.movieInfo.similarmovie.slice(start, end)
    },
  },
  watch: {
    setToggle (val) {
      this.infoToggle = false
      if (val && this.varified === this.$store.getters.getMovieInfo.varified) {
        this.infoToggle = true
      }
    },
    setMovieInfo (val) {
      if (val && this.varified === this.$store.getters.getMovieInfo.varified) {
        this.infoDetail = this.movieInfo
        this.movieBACKURL = this.$store.getters.getMovieInfo
      }
    },
  },
  methods: {
    changeMovieInfo(movieData) {
      this.infoDetail = movieData
    },
    closeInfoBtn() {
      // store 비우기
      this.infoToggle = false
      this.$store.commit('selectedMovie')
      this.infoBtnToggle = 1
      this.scorePageNum = 0
      this.moviePageNum = 0
    },
    infoBtnSwitch(num) {
      this.infoBtnToggle = num
    },
    pagination(str, bool) {
      if (bool) {
        if (str === 's') {
          this.scorePageNum++
        } else {
          this.moviePageNum++
        }
      } else {
        if (str === 's') {
          this.scorePageNum--
        } else {
          this.moviePageNum--
        }
      }
    },
  }
}
</script>

<style lang="scss">
.test-enter-active,
.test-leave-active {
  transition-duration: 0.5s;
  transition-property: height, opacity, transform;
  transition-timing-function: cubic-bezier(0.55, 0, 0.1, 1);
  overflow: hidden;
}
.test-enter,
.test-leave-active {
  opacity: 0;
  transform: translate(2em, 0);
}

.test-leave-active,
.test-enter {
  opacity: 0;
  transform: translate(-2em, 0);
}

.rateBox {
  display: flex;
  position: relative;
  width: 30%;
  height: 8vh;
  &__0 {
    position: absolute;
    top: 90%;
    left: 30%;
  }
  &__1 {
    position: absolute;
    top: 90%;
    right: 4%;
  }
  &__2 {
    position: absolute;
    bottom: -60%;
    left: 30%;
  }
  &__3 {
    position: absolute;
    bottom: -60%;
    right: 4%;
  }
  .rateStar {
    position: absolute;
    top: 30%;
    left: 10%;
  }
}
</style>
