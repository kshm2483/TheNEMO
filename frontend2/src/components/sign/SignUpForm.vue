<template>
      <div class="filler">
        <div class="LoginForm">
          <header class="LoginForm__Header">회원가입</header>
          <form>
            <input type="text" class="LoginForm__Input" :class="{LoginForm__Err : checkNickName()}" id="NICKNAME" v-model="nickName" placeholder="아이디" autocomplete="username" autofocus>
            <p class="checkText" v-if="checkNickName()" >아이디는 최소 8글자 이상이어야 합니다.</p>
            <input type="password" class="LoginForm__Input" :class="{LoginForm__Err : checkPassword()}" id="PASSWORD" v-model="password" placeholder="비밀번호" autocomplete="new-password">
            <p class="checkText" v-if="checkPassword()" >비밀번호는 최소 8글자 이상이어야 합니다.</p>
            <input type="password" class="LoginForm__Input" :class="{LoginForm__Err : checkPasswordConfirm()}" id="PASSWORDCONFIRM" v-model="passwordconfirm" placeholder="비밀번호 확인" autocomplete="new-password">
            <p class="checkText" v-if="checkPasswordConfirm()" >비밀번호가 일치하지 않습니다.</p>
          </form>

          <div class="separater"></div>

          <div v-for="items in SignupList" :key="items.label">
            <p class="label" :id="items.label">{{items.label}}</p>
            <select :name="items.name" class="LoginForm__Drop" v-model="items.name">
                <option :value="item.value" v-for="item in items.option" :key="item.value">{{item.text}}</option>
            </select>
          </div>

          <div class="separater"></div>

          <div class="btn btn--primary btn--lg LoginForm__btn" :class="{'btn--disabled' : checkAll() }" @click="signUpSend">회원가입</div>
          <p style="display:inline; font-size: 0.8em; color:grey;">이미 회원이신가요? </p> <p class="LoginForm__SignUp" @click="Go">돌아가기</p>
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
      passwordconfirm : '',

      SignupList : [
        { label : 'gender',
          name : '',
          option: [
              {text:  "Male", value : "M"},
              {text:  "Female", value : "F"},
          ]},
        { label : 'age',
          name : '',
          option: [
            {text:  "Under 18", value : 1},
            {text:  "18-24", value : 18},
            {text:  "25-34", value : 25},
            {text:  "35-44", value : 35},
            {text:  "45-49", value : 45},
            {text:  "50-55", value : 50},
            {text:  "56+", value : 56},
        ]},
        { label : 'occupation',
          name : '',
          option: [
            {text:  "other", value : 0},
            {text:  "academic/educator", value : 1},
            {text:  "artist", value : 2},
            {text:  "clerical/admin", value : 3},
            {text:  "college/grad student", value : 4},
            {text:  "customer service", value : 5},
            {text:  "doctor/health care", value : 6},
            {text:  "executive/managerial", value : 7},
            {text:  "farmer", value : 8},
            {text:  "homemaker", value : 9},
            {text:  "K-12 student", value : 10},
            {text:  "lawyer", value : 11},
            {text:  "programmer", value : 12},
            {text:  "retired", value : 13},
            {text:  "sales/marketing", value : 14},
            {text:  "scientist", value : 15},
            {text:  "self-employed", value : 16},
            {text:  "technician/engineer", value : 17},
            {text:  "tradesman/craftsman", value : 18},
            {text:  "unemployed", value : 19},
            {text:  "writer", value : 20},
        ]},
      ]
    }
  },
  methods: {
    Go() {
      this.$emit('transForm');
      window.scrollTo(0, 0);
    },
    checkAll() {
      if (this.nickName === ''|| this.password === '' || this.passwordconfirm === '' || this.SignupList[0].name === '' || this.SignupList[1].name === '' || this.SignupList[2].name === '' || this.checkNickName() || this.checkPassword() || this.checkPasswordConfirm()) {
        return true
      }
    },
    checkNickName() {
      if (this.nickName != '' && this.nickName.length <= 7) {
        return true
      }
    },
    checkPassword() {
      if (this.password != '' && this.password.length <= 7) {
        return true
      }
    },
    checkPasswordConfirm() {
      if (this.passwordconfirm != '' && this.passwordconfirm != this.password) {
        return true
      }
    },
    async signUpSend() {
      const data = {
        profiles: {
          'username': this.nickName,
          'password': this.password,
          'gender': this.SignupList[0].name,
          'age': this.SignupList[1].name,
          'occupation' : this.SignupList[2].option[this.SignupList[2].name].text
        }
      }
      const resp = await api.signUp(data)
      if (resp) {
        const form = { id: this.nickName, pw: this.password }
        const result = await api.logIn(form)
        if (result === false) {
          this.nickName = ''
          this.password = ''
        } else {
          this.$router.push('/profile')
        }
      } else {
        alert('error')
      }
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
