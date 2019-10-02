<template>
    <transition name="slide" mode="out-in">
      <div>
        <div class="separater separater__trans"></div>
        <newRatingImg v-for="item in movieItems[0].items" :key="item" :imgData="{ imgSrc, id:item, varified: movieItems[0].genre }"/>
      </div>
    </transition>
</template>

<script>
import newRatingImg from './newRatingImg'

export default {
  components: {
    newRatingImg
  },
  props: {
    movieItems: {
      type: Array,
      required: true
    },
    pageSize: {
      type: Number,
      required: false,
      default: 6
    }
  },
  data: () => ({
    showBtn: false,
    imgSrc: "https://w.namu.la/s/5ef7389c2e210b3a176ae30b068a73637be82cab0d09ac986e16b85a6aa66f3caa54365c528a40f056643f53c8aa32f442f423754b2317648ee65d4408e9612d7dfe4a2dd9d7db50c0d2bc4d5bc3aef988b1cb3efe57dcb27486859ad0e08113",
  }),
  methods: {
    closeInfoBtn() {
      // $store 비우기
      this.$store.commit('selectedMovie')
      // 리스트 양옆으로 넘길때 MovieCard.vue 닫기
      this.$EventBus.$emit('closeMovieCard')
    },
  },
}
</script>
