<template>
  <div>
    <div class="profile">
      <!-- 유저 정보 시작 -->
      <div class="profile-banner">
        <!-- 유저 이미지 시작 -->
        <div class="profile-banner__image">
          <img src="@/assets/image/defaultUserImage.jpg" alt="" style="width: 10vw; height: 10vw;">
        </div>
        <!-- 유저 이미지 끝 -->

        <!-- 유저 상세 정보 시작 -->
        <div class="profile-banner-right">

          <!-- 유저 명 / 성별 / 수정 버튼 시작-->
          <div class="profile-banner-right__head">
            <div class="username">
               {{ userData.username }} (<span v-if="userData.gender == 'M'">Man</span> <span v-else>Women</span>)
            </div>
            <div class="btn btn--primary btn--md" @click="Go">
              Edit
            </div>
          </div>
          <!-- 유저 명 / 성별 / 수정 버튼 끝 -->

          <div class="separater"></div>

          <div class="profile-banner-right__body">
            <!-- 유저 상세 정보 상단  -->
            <div class="profile-banner-right__body-top">
              <p v-if="userData.age === 1"><b>나이 : </b>Under 18</p>
              <p v-else><b>나이 : </b>{{ userData.age }}</p>
              <p><b>직업 : </b>{{ userData.occupation }}</p>
            </div>
            <!-- 유저 상세 정보 하단  -->
            <div class="profile-banner-right__body-bottom">
              <p><b>한줄 코멘트</b></p>

            </div>
          </div>
        </div>
        <!-- 유저 상세 정보 끝 -->
      </div>
      <!-- 유저 정보 끝 -->

      <!-- 프로필 토글 버튼 시작 -->
      <div class="profileToggle">
        <p class="btn" :class="{profileToggle__select : checkToggle === 1}" @click="checkToggle = 1">평가한 영화</p>
        <p class="btn" :class="{profileToggle__select : checkToggle === 2}" @click="checkToggle = 2">유사한 유저</p>
      </div>
      <!-- 프로필 토글 버튼 끝 -->

      <!-- 프로필 하단 컴포넌트 시작 -->
        <!-- 유저가 본 영화 목록 시작 -->
        <div class="profile-myMovie" v-if="checkToggle === 1">
          <MovieImg v-for="movie in movieItems" :key="movie.id" :imgData="{ imgSrc: movie.poster_url, title: movie.title, id: movie.id, genres: movie.genres, varified: 'none', overview: movie.overview }"/>
        </div>
        <!-- 유저가 본 영화 목록 끝 -->

        <!-- 유저와 유사한 유저 목록 시작 -->
        <div class="profile-similarUser" v-if="checkToggle === 2">
          <!-- i (similar user id 값)만 UserCard에 전달해주는 것임) -->
          <!-- userData.similaruser.slice(0,5) -->
          <UserCard v-for="i in userData.similaruser" :key="i" style="display:inline-block;" :simUserId="i"/>
        </div>
        <!-- 유저와 유사한 유저 목록 끝 -->
      <!-- 프로필 하단 컴포넌트 시작 -->
    </div>
    <div class="lds-bg"/>
  </div>
</template>

<script>
import api from '@/api'
import UserCard from '@/components/profile/UserCard'
import MovieImg from '@/components/movies/MovieImg'
import { mapState, mapActions, mapGetters } from "vuex";

export default {
  components: {
    UserCard,
    MovieImg
  },
  data() {
    return{
      user: this.$route.params.user_id,

      checkToggle : 1,

      userInfo: [
        {imgurl:require("@/assets/image/defaultUserImage.jpg")},
      ],

      movieItems: [],
      selectInfo: {}
   }
 },
 computed: {
    setUserData() {
      return this.$store.state.userData
    },
    ...mapState({
      userData: state => state.userData,
      userList: state => state.userData.similaruser,
      movieList: state => state.movieSearchList
    }),
    ...mapGetters({
      myMovie: 'getUserMovieData'
    })
  },
  watch: {
    movieList() {
      this.setMovieItems()
    }
  },
  mounted() {
    this.loadUser(this.user),
    this.searchMovies()
  },
  methods: {
    ...mapActions({
        loadUser: 'searchProfile'
      }),
    ...mapActions(["searchMovies"]),
    setMovieItems() {
      this.setUserData.ratingmovie.forEach((el) => { this.movieItems.push(this.movieList.find(movie => movie.id === el))})
    },
    async selectMovie(id) {
      const resp = await api.searchMovies({'id': id})
      this.selectInfo = resp.data
    },
    Go() {
      this.$emit('transForm');
      window.scrollTo(0, 0);
    },
  }
}
</script>
