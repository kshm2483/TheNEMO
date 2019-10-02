<template>
  <div class="movieItem" v-if="infoToggle">
    <!--  -->
    <div class="movieInfo">
      <transition-group name="test">
        <div v-if="infoBtnToggle === 1" key="contentInfo" style="position:absolute; width: 35vw;">
          <!-- movie info -->
          <div>
            <div>
              <h1>{{ infoDetail.info.title }}</h1>
              <p>{{ infoDetail.info.rating }} {{ infoDetail.info.adult }}</p>
            </div>
            <div>
              <h2 v-for="genre in infoDetail.info.genres" :key="genre">{{ genre }}</h2>
              <p>{{ infoDetail.info.overview }}</p>
            </div>
          </div>
        </div>
        <div v-if="infoBtnToggle === 2" key="contentSimilar" style="position:absolute;">
          <h1>2page</h1>
        </div>
        <div v-if="infoBtnToggle === 3" key="contentDetail" style="position:absolute;">
          <h1>3page</h1>
        </div>
      </transition-group>
    </div>
    <div class="movieBackImg" :style="bgStyle">
    </div>
    <div class="movieBtnGroups">
      <button :class="{ activate: infoBtnToggle === 1 }" @click="infoBtnSwitch(1)">콘텐츠 정보</button>
      <button :class="{ activate: infoBtnToggle === 2 }" @click="infoBtnSwitch(2)">비슷한 콘텐츠</button>
      <button :class="{ activate: infoBtnToggle === 3 }" @click="infoBtnSwitch(3)">상세 정보</button>
    </div>
    <div class="movieClose" @click="closeInfoBtn">
      <fa-icon icon="times"/>
    </div>
  </div>
</template>

<script>
const BACKDROP_BASE = "https://image.tmdb.org/t/p/original/"

export default {
  props: {
    varified: {
      type: String,
      required: true
    }
  },
  data: () => ({
    infoDetail: [],
    infoToggle: false,
    infoBtnToggle: 1
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
        'background-image': `url(${ BACKDROP_BASE }/${ this.infoDetail.info.backdrop_url })`,
        'background-repeat': 'no-repeat',
        'background-size': 'cover',
        'mask-image': 'linear-gradient(to left, rgba(0,0,0,1), rgba(0,0,0,0))'
      }
    }
  },
  watch: {
    setToggle (val) {
      if (val && this.varified === this.$store.getters.getMovieInfo.varified) {
        this.infoToggle = true
      }
    },
    setMovieInfo (val) {
      if (val && this.varified === this.$store.getters.getMovieInfo.varified) {
        this.infoDetail = this.$store.getters.getMovieInfo
      }
    }
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
    },
    infoBtnSwitch(num) {
      this.infoBtnToggle = num
    }
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
</style>
