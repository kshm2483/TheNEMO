<template>
  <div id="app" @wheel="checkScroll()">
    <div class="subscription" v-if="!subscription && isNotInConfig()">
      <ul>
        <h1>영화가 보고 싶으시면 구독을 누르십시요</h1>
        <div class="btn btn--primary btn--lg" @click="goSubscription()">구독</div>
      </ul>
    </div>
    <header class="navBar"  :class="{navBar__down : (whereScroll !== 0) && (userDropdown === false), navBar__notHome : isNotInConfig()}" >
      <nav class="navItems">
        <div class="navItems__title">
          <div class="navItems__option" @click="checkLoginANDgo()">NEMO</div>
        </div>
        <div class="navItems__body">
          <div>
            <!-- <div v-if="isNotInConfig() && searchToggle === true" @click="searchToggle = !searchToggle">검색</div> -->
            <fa-icon
              icon="search"
              v-if="isNotInConfig() && searchToggle === true"
              @click="searchToggle = !searchToggle; setFocus(true);"
              />
            <transition name="fade" mode="out-in">
              <div>
                <input type="text"
                  v-model="searchInput"
                  v-if="isNotInConfig() && searchToggle === false"
                  ref="search"
                  placeholder="Search"
                  @blur="escapeBlur"
                  @keyup.enter="searchTitle()"
                  alt="Search"
                >
                <div v-if="isNotInConfig() && searchToggle === false" class="testdiv">
                  <p v-for="i in resultQuery" :key="i.id">
                    {{ i.title }}
                  </p>
                </div>
              </div>
            </transition>
          </div>
          <router-link :to="{ name: 'Admin' }" v-if="isStaff && isNotInConfig()">Admin</router-link>
          <router-link :to="{ name: 'Movie' }" v-if="isNotInConfig()">Movie</router-link>
          <router-link :to="{ name: 'Search' }" v-if="isNotInConfig()">Search</router-link>
          <div class="navItems__option" @click="userDropdown = !userDropdown; setFocus(false);" v-if="isNotInConfig()">MyInfo</div>
          <router-link :to="{ name: 'Sign' }" v-if="!isNotInConfig()">Login</router-link>
        </div>
      </nav>
    </header>
        <ul class="divFocus" v-if="userDropdown === true" ref="search" @blur="userDropdown = !userDropdown" tabindex="1">
          <p style="cursor: default; color:white;">{{userInfo}}</p>
          <div class="separater"></div>
          <p @click="goProfile()">Profile</p>
          <p @click="logOut()">Logout</p>
        </ul>
    <transition name="fade" mode="out-in">
      <router-view/>
    </transition>
    <footer>
      Copyright 2019. CyberGhost. All rights reserved.
    </footer>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex"
import session from "@/api/modules/session";
import router from "@/router";
import api from "./api";

export default {
  name: 'app',
  components: {
  },
  data() {
    return{
      subscription : false,
      userInfo : false,
      isStaff: false,
      userDropdown : false,
      whereScroll : 0,
      searchToggle : true,
      // search
      searchInput: null,
      searchItems: [],
    }
  },
  computed: {
    ...mapState({
      movieList: state => state.movieSearchList
    }),
    resultQuery() {
      if (this.searchInput) {
        return this.movieList.filter((item) => {
          return this.searchInput.toLowerCase().split(' ').every(v => item.title.toLowerCase().includes(v))
        })
      } else {
        return this.movieList
      }
    }
  },
  mounted() {
    if (JSON.parse(sessionStorage.getItem("drf"))) {
      this.subscription = JSON.parse(sessionStorage.getItem("drf")).subscription
    }
    this.searchMovies()
    this.checkScroll()
  },
  updated() {
    if (session.check()) {
      const data = JSON.parse(sessionStorage.getItem("drf"))
      this.userInfo = data.username
      this.isStaff = session.checkStaff()
    }
    else {
      this.userInfo = false
      this.isStaff = false
    }
    if (JSON.parse(sessionStorage.getItem("drf"))) {
      this.subscription = JSON.parse(sessionStorage.getItem("drf")).subscription
    }
  },
  methods: {
    ...mapActions(["searchMovies"]),
      async goSubscription() {
        const form = { id : JSON.parse(sessionStorage.getItem("drf")).id}
        const result = await api.playSubscription(form)
        if (result) {
          this.subscription = JSON.parse(sessionStorage.getItem("drf")).subscription
        }
      },
     isNotInConfig() {
      if (session.check()) {
        return true
      }
      else {
        return false
      }
    },
    checkLoginANDgo() {
        if (session.check()) {
          return router.push({name : 'Movie'})
        }
        else {
          return router.push({path : '/'})
        }
    },
    goProfile(){
      const data = JSON.parse(sessionStorage.getItem("drf"))
      router.push({
            name : 'Profile',
            params: {user_id:data.id}
          },this.blurFocus())
    },
    checkScroll() {
      window.onscroll = () => {
        this.whereScroll = window.pageYOffset
      }
    },
    setFocus(bool) {
      if (bool === true && this.$route.name !== 'Search') {
        this.$router.push({ name: 'Search' })
      }
      let _this = this
      _this.$nextTick()
        .then(() => { _this.$refs.search.focus() })
    },
    escapeBlur() {
      this.searchInput = null
      this.searchToggle = !this.searchToggle
    },
    blurFocus() {
      let _this = this
      _this.$nextTick()
        .then(() => { _this.$refs.search.blur() })
    },
    async logOut() {
      await api.logOut()
      this.$router.push({ name: 'Home' },
      this.blurFocus())
    },
    searchTitle() {
      const busInput = { payload: this.resultQuery, str: this.searchInput}
      this.$EventBus.$emit('movieSearchList', busInput)
    }
  },
}
</script>

<style lang="scss">
#app {
  text-align: center;
}

// CSS transition
.fade-enter-active, .fade-leave-active {
  transition: all .3s ease;
}
.fade-enter, .fade-leave-active {
  opacity: 0;
}
</style>

<style scoped lang="scss">
footer {
  position: absolute;

  width:100%;

  line-height: 25vh;
  height: 25vh;
  color: rgba(255, 255, 255, 0.7);
  background-color: rgb(18, 18, 18);
}
</style>
