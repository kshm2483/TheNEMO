<!-- 영화 검색 페이지 -->
<template>
  <v-container grid-list-md text-center>
    <v-layout justify-center wrap>
      <!-- 검색 폼 -->
      <v-flex xs10>
        <div class="display-2 pa-10">영화 검색</div>
        <MovieSearchForm :submit="searchMovies" />
        <v-btn class="ma-1" @click="viewSort(true)">view: desc</v-btn>
        <v-btn class="ma-1" @click="viewSort(false)">view: asc</v-btn>
        <v-btn class="ma-1" @click="rateSort(true)">rating: desc</v-btn>
        <v-btn class="ma-1" @click="rateSort(false)">rating: asc</v-btn>
      </v-flex>

      <!-- 검색 결과 -->
      <v-flex xs10>
        <MovieList :movie-list-cards="movieList" />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";
import MovieSearchForm from "../../MovieSearchForm";
import MovieList from "../../MovieList";
export default {
  components: {
    MovieList,
    MovieSearchForm
  },
  data () {
    return {
    }
  },
  computed: {
    ...mapState({
      movieList: state => state.data.movieSearchList
    })
  },
  methods: {
    ...mapActions("data", ["searchMovies"]),
    viewSort(bool) {
      let result = ''
      if (bool) {
        result = this.$store.state.data.movieSearchList.slice(0).sort((a, b) => { return b.viewCnt - a.viewCnt })
      } else {
        result = this.$store.state.data.movieSearchList.slice(0).sort((a, b) => { return a.viewCnt - b.viewCnt })
      }
      this.$store.commit('data/setMovieSearchList', result)
    },
    rateSort(bool) {
      let result = ''
      if (bool) {
        result = this.$store.state.data.movieSearchList.slice(0).sort((a, b) => { return b.rating - a.rating })
      } else {
        result = this.$store.state.data.movieSearchList.slice(0).sort((a, b) => { return a.rating - b.rating })
      }
      this.$store.commit('data/setMovieSearchList', result)
    }
  }
};
</script>