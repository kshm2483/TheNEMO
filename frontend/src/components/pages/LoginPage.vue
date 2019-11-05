<template>
    <v-container>
        <v-row  justify="center">
            <v-btn v-if="signToggle" @click="signToggle = !signToggle">
                Sign Up
            </v-btn>
            <v-btn v-if="!signToggle" @click="signToggle = !signToggle">
                Sign In
            </v-btn>
            <SignUpForm v-on:signUpComplete="signToggle = false" v-if="signToggle"/>
            <SignInForm v-if="!signToggle"/>
        </v-row>
    </v-container>
</template>
<script>
import SignInForm from '@/components/forms/SignInForm.vue'
import SignUpForm from '@/components/forms/SignUpForm.vue'
  export default {
    name : 'LoginForm',
    components : {
        SignInForm, SignUpForm
    },
    data: () => ({
        username: '',
        password: '',
        passwordConfirm: '',
        email: '',
        show_password: false,
        valid: false,
        rules: {
            required: value => !!value || 'Required.',
            nameRules: v => v.length <= 10 || 'Name must be less than 10 characters',
            passwordRules: v => v.length >= 8 || 'Password must be more than 8 characters',
        },
        signToggle : false,
    }),
    computed: {
        passwordConfirmRules() {
        return [
            () => (this.password === this.passwordConfirm) || '??',
        ]
      },
    },
    watch: {
        signToggle() {
            console.log(this.signToggle)
        }
    }
  }
</script>