<template>
  <div  class="filler">
    <div class="LoginForm">
      <header class="LoginForm__Header">로그인</header>
      <form>
        <input type="text" class="LoginForm__Input" id="NICKNAME" v-model="nickName" placeholder="아이디" autocomplete="username" autofocus>
        <input type="password" class="LoginForm__Input" id="PASSWORD" v-model="password" placeholder="비밀번호" autocomplete="new-password" @keydown.enter="logIn()">
      </form>
      <div class="separater"></div>
      <div class="btn btn--primary btn--lg LoginForm__btn" @click="logIn()">로그인</div>
      <p style="display:inline; font-size: 0.8em; color:grey;">아직 회원이 아니신가요? </p> <p class="LoginForm__SignUp" @click="Go">회원가입</p>
    </div>
  </div>
</template>

<script>
import api from '@/api'

export default {
  data() {
    return {
      nickName : '',
      password : '',
    }
  },
  methods: {
    async logIn() {
      const form = { id: this.nickName, pw: this.password }
      const result = await api.logIn(form)
      if (result === false) {
        this.nickName = ''
        this.password = ''
      } else {
        this.$router.push('/movie')
      }
    },
    Go() {
      this.$emit('transForm');
      window.scrollTo(0, 0);
    }
  }

}
</script>

<style lang="scss" scoped>

.filler {
  position: absolute;
  width: 500px;
  height: 800px;
  background-color: #151515;
  padding: var(--space-xl);
  border-radius: var(--radius-sm);
}

.flex {
  display: flex;
  flex-direction: column;
}

.LoginForm {
    &__Input{
    margin-top: var(--space-sm);
    padding: var(--space-xs);
    border-radius: calc(0.3 * var(--radius-sm));
    border: none;

    background-color:grey;
    width: 480px;
    height: 1.4em;

    color: white;
    font-size: 1.5em;

    }

    &__Header {
      text-align: start;
      font-size: 2em;
      font-weight: 700;
      color: white;
    }

    &__btn {
      width: 470px;
    }

    &__SignUp {
      display: inline;
      margin-top: var(--space-sm);

      font-size: 0.8em;
      color: white;
    }

    &__SignUp:hover {
      cursor: pointer;
    }
}
.signFade-enter-active, .signFade-leave-active {
  transition: all 0.3s ease ;
}

.signFade-enter, .signFade-leave-active {
  opacity: 0;
}
</style>
