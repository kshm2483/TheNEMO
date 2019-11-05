<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <div>
      <!-- {{ genresStr }}  -->
      <v-layout justify-center>
        <v-rating
          :value="movie.rating"
          color="indigo"
          background-color="indigo"
          half-increments
          dense
          readonly
        />
        <div class="grey--text ml-4">{{ movie.rating }}</div>
      </v-layout>
      영화 설명 같은거 들어감
      <h2>비슷한 영화</h2>
      <MovieClusteringDataCard :itemList="movie.similarmovie"/>
      <h2>{{ movie.viewCnt }} comments</h2>
      <div>
        <p v-for="item in movie.comments">
          <v-btn text
            @click="goTo(item.user)">{{ item.user.name }}</v-btn>
          <v-layout justify-center>
            <v-rating
              :value="item.rating"
              color="indigo"
              background-color="indigo"
              half-increments
              dense
              readonly
            />
            <div class="grey--text ml-4">{{ item.rating }}</div>
          </v-layout>
        </p>
      </div>
    </div>
    <v-btn text @click="goTo()"><v-icon dark>back</v-icon></v-btn>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import router from "../../../router"
import MovieClusteringDataCard from "./MovieClusteringDataCard"

export default {
  components: {
    MovieClusteringDataCard
  },
  data() {
    return {
      movie: '',
      movieId: this.$route.params.movie_id,
      movieList: [],
    }
  },
  computed: {
    ...mapGetters("data", ['selectMovie'])
  },
  mounted() {
    this.movie = this.selectMovie(this.movieId)
  },
  methods: {
    goTo(user) {
      if (user) {
        router.push({ name: 'user-detail', params: { user_id: user.id } });
      } else {
        router.go(-1)
      }
    },
  }
}
</script>