<template>
  <div>
    <!-- 로그인 / 회원가입 분리 -->
    <div class="flexCenter flexCenter__sign">
      <!-- login form -->
      <SignForm v-if="signToggle" @transForm="signToggle = !signToggle"/>
      <SignUpForm v-if="!signToggle" @transForm="signToggle = !signToggle"/>
    </div>
  </div>
</template>

<script>
import SignForm from '@/components/sign/SignForm'
import SignUpForm from '@/components/sign/SignUpForm'

export default {
  components: {
    SignForm,SignUpForm
  },
  data(){
    return {
      signToggle : true,
    }
  },
  mounted() {
    if (this.$route.params.directSignup === true) {
      this.signToggle = false
    }
  },
}
</script>

<style lang="scss">

</style>
