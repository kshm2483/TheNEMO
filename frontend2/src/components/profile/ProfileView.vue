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
            <div v-for="item in movieItems" :key="item.genre">
              <MovieList :id="item.genre" :item="item"/>
              <transition name="fade" mode="out-in">
                <MovieCard :varified="item.genre"/>
              </transition>
            </div>
        </div>
        <!-- 유저가 본 영화 목록 끝 -->

        <!-- 유저와 유사한 유저 목록 시작 -->
        <div class="profile-similarUser" v-if="checkToggle === 2">
        </div>
        <!-- 유저와 유사한 유저 목록 끝 -->
      <!-- 프로필 하단 컴포넌트 시작 -->
    </div>
  </div>
</template>

<script>
import MovieList from '@/components/movies/MovieList'
import MovieCard from '@/components/movies/MovieCard'
import { mapState, mapActions } from "vuex";

export default {
components: {
    MovieList,
    MovieCard
  },
 data() {
   return{
     user: this.$route.params.user_id,

     checkToggle : 1,

     userInfo: [
       {imgurl:require("@/assets/image/defaultUserImage.jpg")},
     ],

     movieItems: [{genre:'action', items: [1,2,3,4,5,6,7,8,9,10]}]
   }
 },
  mounted() {
    this.loadUser(this.user)
    // MovieImg.vue => 영화 정보 오픈 시 스크롤
    this.$EventBus.$on('movieInfoActive', (payload) => {
      this.scrollCard(payload.varified)
    })
  },
  computed: {
    ...mapState({
      userData: state => state.userData,
      userList: state => state.userData.similaruser,
      movieList: state => state.userData.ratingmovie,
    }),
    
  },
  methods: {
    ...mapActions({
      loadUser: 'searchProfile'
    }),
    goTo() {
      this.$router.push('/')
    },
    scrollCard(locationId) {
      const element = document.getElementById(locationId)
      const elemRect = element.getBoundingClientRect()
      const offset = elemRect.bottom + window.pageYOffset - 100
      window.scrollTo({top: offset, behavior: 'smooth'})
    },
    Go() {
      this.$emit('transForm');
      window.scrollTo(0, 0);
    },
  }
}

</script>

<style scoped lang="scss">

</style>
