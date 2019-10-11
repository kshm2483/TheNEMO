<template>
  <div
    class="movieList"
    @mouseover="mouseOver"
    @mouseleave="mouseLeave">
    <transition name="slide" mode="out-in">
      <div style="height: 2em;">
        <p>{{ movieItem.varified }}</p>
        <MovieImg
          v-for="i in paginatedData" :key="i.id"
          :imgData="{info: i, varified: movieItem.varified }"/>
      </div>
    </transition>
    <div v-show="true" style="display: inline;">
      <button class="pageBtn pageBtn__prev" :disabled="pageNum === 0" @click="pagination(false)"><fa-icon icon="angle-left"/></button>
      <button class="pageBtn pageBtn__next" :disabled="pageNum >= pageCount - 1" @click="pagination(true)"><fa-icon icon="angle-right"/></button>
    </div>
  </div>
</template>

<script>
import MovieImg from './MovieImg'

export default {
  components: {
    MovieImg
  },
  props: {
    movieItem: {
      type: Object,
      required: true
    },
    pageSize: {
      type: Number,
      required: false,
      default: 6
    }
  },
  data: () => ({
    pageNum: 0,
    showBtn: false,
  }),
  computed: {
    pageCount () {
      let listLeng = this.movieItem.items.length, listSize = this.pageSize, page = Math.floor((listLeng - 1) / listSize) + 1
      return page
    },
    paginatedData () {
      const start = this.pageNum * this.pageSize, end = start + this.pageSize;
      return this.movieItem.items.slice(start, end)
    }
  },
  methods: {
    pagination(bool) {
      if (bool) {
        this.pageNum++
      } else {
        this.pageNum--
      }
      this.closeInfoBtn()
    },
    mouseOver() {
      this.showBtn = true
    },
    mouseLeave() {
      this.showBtn = false
    },
    closeInfoBtn() {
      // $store 비우기
      this.$store.commit('selectedMovie')
      // 리스트 양옆으로 넘길때 MovieCard.vue 닫기
      this.$EventBus.$emit('closeMovieCard')
    },
  },
}
// pagination 참고링크 : https://pewww.tistory.com/5
</script>
