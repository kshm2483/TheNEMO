<template>
  <div>

    <div class="SimilarUserInfo" v-if="simUserInfo.username">
        <!-- similar users info -->
            <!-- 유저 이미지 -->
              <div class="SimilarUserInfo-banner">
                  <div class="SimilarUserInfo-banner_img">
                  <img src="@/assets/image/defaultUserImage.jpg" alt="" style="width: 70px; height: 70px;">
                  </div>
                </div>
              <!-- 유저 신상정보 -->
              <div style="margin-top:2px; margin-bottom:2px">
                <span style ="display:inline-block;color:black; font-weight: bold; margin-right:1px;">{{ simUserInfo.username }}</span>
                <span style ="display:inline-block;color:black;margin-left:1px;">({{ simUserInfo.gender }})</span>
              </div>
              <div class="separater separater__1" style="background-color: gainsboro ;">.</div>
              <div style="color:black; margin-left:10px; margin-right:10px;" >
                 <p>나이: {{simUserInfo.age}}</p>
                <p>직업: {{simUserInfo.occupation}}</p>
                <p>한줄평: {{simUserInfo.description}} </p>
              </div>
    </div>
    <div v-else class="lds-dual-ring">
    </div>
  </div>
</template>

<script>
import api from '@/api'
import { mapState } from "vuex";


export default {
    name : 'UserCard',
    data: () => ({
      //  similar user 모든 정보 담기
      simUserInfo:[],

    infoBtnToggle: 2
    }),
    props : [
      'simUserId'
    ],

    computed: {
    ...mapState({
      userData: state => state.userData,
      userList: state => state.userData.similaruser,
      movieList: state => state.userData.ratingmovie,
    })
    },
    //axios 요청값 받는거
    mounted () {
      {
        // id에 해당하는 userData가 맞는지를 확인하는 함수를 불러오면서, 동시에 지금 받은 id 값을 가지고 오기
      this.setUserProfile(Number(this.simUserId))
      }
    },
    methods: {
      async setUserProfile(userId) {
        const resp = await api.searchProfile(userId)
        // console.log(resp.data)
        this.simUserInfo = resp.data
      }
    },
// api 요청하고 retrun 된 res 값을 -- this.userInfo
// const res = aixos.get("~~~")
// console.log(res)

// aixos.get("~~~").then(res=>{
//   console.log(res)
// })


}
</script>
<style lang="scss" scope>
  //   background-color: grey;
  //   margin-top:var(--space-xxxxs);
  //   margin-bottom:var(--space-xxxxs);
  // }

</style>

