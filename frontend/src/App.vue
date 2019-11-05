<template>
  <v-app id="app">
    <v-app-bar app clipped-left color="indigo">
      <v-app-bar-nav-icon class="white--text" @click="drawer = !drawer" />
      <span class="title ml-3 mr-5 white--text">영화 추천 서비스</span>
      <v-spacer />

    </v-app-bar>

    <v-navigation-drawer v-model="drawer" app clipped color="grey lighten-4">
      <v-list dense class="grey lighten-4">  
          <v-list-item @click="goMyProfile(choices.profile.path)" v-if="choices.login.is_login">
            <v-list-item-action>
              <v-icon></v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choices.profile.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item @click="goTo(choices.admin.path)" v-if="choices.admin.staff==true">
            <v-list-item-action>
              <v-icon></v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choices.admin.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item @click="goTo(choices.login.path)" v-if="!choices.login.is_login">
            <v-list-item-action>
              <v-icon>{{ choices.login.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choices.login.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item @click="goTo(choices.search.path)">
            <v-list-item-action>
              <v-icon>{{ choices.search.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 font-weight-bold black--text">{{ choices.search.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>

          <v-list-item @click="logOut" v-if="choices.login.is_login">
            <v-list-item-action>
              <v-icon></v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title class="subtitle-2 font-weight-bold black--text">Sign Out</v-list-item-title>
            </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-content>
      <v-container fluid fill-height class="grey lighten-4">
        <v-layout justify-center align-center>
          <!-- each pages will be placed here -->
          <router-view />
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import router from "./router";
import session from "./api/modules/session";
import api from "./api";
import swal from 'sweetalert';

export default {
  data: () => ({
    drawer: null,
    choices: {
      profile :{
        icon: "mdi-settings_applications",
        text: "내 프로필",
        path: "user-detail",
      },
      admin :{
        icon: "mdi-settings_applications",
        text: "관리자 페이지",
        path: "admin-page",
        staff: false
      },
      login: {
        icon: "mdi-shop",
        text: "로그인",
        path: "login-page",
        is_login : false,
      },
      search: {
        icon: "mdi-movie",
        text: "영화 검색",
        path: "movie-search"
      }
    }
  }),
  updated() {
      this.choices.login.is_login = session.check()
      this.choices.admin.staff = session.checkStaff()
    },
  methods: {
    goTo: function(path) {
      router.push({ name: path });
    },
    goMyProfile: function(path) {
      const data = JSON.parse(sessionStorage.getItem("drf"))
      router.push({ 
        name: path,
        params: {user_id:data.id} });
    },
    async logOut() {
      const data = JSON.parse(sessionStorage.getItem("drf"))
      const result = await api.logOut()
      this.$router.push({ name: 'login-page' })
    }
  }
};
</script>

<style>
#keep .v-navigation-drawer__border {
  display: none;
}
</style>