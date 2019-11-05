<template>
  <div class="d-flex">
    <!-- 유저 정보가 들어가는 카드 -->
    <v-card class="mx-auto" max-width="344" flat>
      <v-card-text>
        <v-avatar size="164" style="margin-left: 2.5em;">
          <v-img src="https://t1.daumcdn.net/cfile/tistory/99A5D14E5AF0E7E91A"></v-img>
      </v-avatar>
        <div>{{ userData.age }} / {{ userData.gender }}</div>
        <p class="display-1 text--primary">
          {{ userData.username }}
        </p>
        <p>{{ userData.occupation }}</p>
        <p>{{ userData.is_staff? '관리자': '일반유저' }}</p>
        
        <div class="text--primary">
          이게 유저정보입니다.<br>
          뭔가 있어야할거 같아서 채웠습니다.
        </div>
      </v-card-text>
      <v-card-actions>
        <v-btn text @click="goTo()"><v-icon dark>back</v-icon></v-btn>
      </v-card-actions>
    </v-card>
    <!-- 클러스터 영화 / 유저가 나옴 -->
    <div>
      <UserClusteringDataCard :itemList="movieList"/>
      <UserClusteringDataCard :itemList="userList"/>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import router from "../../../router"
import UserClusteringDataCard from "./UserClusteringDataCard"

export default {
  components: {
    UserClusteringDataCard
  },
  data() {
    return {
      user: this.$route.params.user_id,

    }
  },
  mounted() {
    this.loadUser(this.user)
  },
  computed: {
    ...mapState({
      userData: state => state.data.userData,
      userList: state => state.data.userData.similaruser,
      movieList: state => state.data.userData.ratingmovie,
    }),
    
  },
  methods: {
    ...mapActions({
      loadUser: 'data/searchProfile'
    }),
    goTo() {
      this.$router.push('/')
    },
  }
}
</script>