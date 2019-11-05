<template>
  <v-form v-model="valid">
    <v-container>
      <v-row>
        <v-col
          cols="8"
        >
          <v-text-field
            v-model="username"
            :rules="[rules.nameRules, rules.required]"
            :counter="10"
            label="Username"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="8"
        >
        <v-text-field
            v-model="password"
            :rules="[rules.passwordRules, rules.required]"
            :type="show_password ? 'text' : 'password'"
            label="Password"
            required
            @keydown.enter="logIn"
          ></v-text-field>
        </v-col>

        <v-row justify="end">
            <v-btn
                @click="logIn">
                Send
            </v-btn>
        </v-row>

      </v-row>
    </v-container>
  </v-form>
</template>
<script>
import api from '@/api'
import swal from 'sweetalert';

export default {
  name : 'SignInForm',
  data: () => ({
    username: '',
    password: '',
    show_password: false,
    valid: false,
    rules: {
        required: value => !!value || 'Required.',
        nameRules: v => v.length <= 10 || 'Name must be less than 10 characters',
    },
  }),
  methods: {
    async logIn() {
      // console.log(this.username, this.password)
      const form = { id: this.username, pw: this.password }
      const result = await api.logIn(form)
      if (result === false) {
        this.username = ''
        this.password = ''
      } else {
        this.$router.push('/')
      }
    },
  }
}
</script>