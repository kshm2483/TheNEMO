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
          ></v-text-field>
          <v-text-field
            v-model="passwordConfirm"
            :rules="passwordConfirmRules"
            label="Password Confirm"
            :type="show_password ? 'text' : 'password'"
            required
          ></v-text-field>
        </v-col>

        <v-col
          cols="8"
        >
         <v-select
          :items="genders"
          v-model="gender"
          :rules="[rules.required]"
          label="Gender"
          item-value="value"
          item-text="text"
          id="GenderSelect"
          required
        ></v-select>
        </v-col>

        <v-col
          cols="8"
        >
         <v-select
          :items="ages"
          v-model="age"
          :rules="[rules.required]"
          label="Age"
          item-value="value"
          item-text="text"
          id="AgeSelect"
          required
        ></v-select>
        </v-col>

        <v-col
          cols="8"
        >
         <v-select
          :items="occupations"
          v-model="occupation"
          :rules="[rules.required]"
          label="Occupation"
          item-value="text"
          id="occupationSelect"
          required
        ></v-select>
        </v-col>
        <v-row justify="end">
            <v-btn
                :disabled=!valid
                @click="signUpSend">
                send
            </v-btn>
        </v-row>

      </v-row>
    </v-container>
  </v-form>
</template>
<script>
import api from '@/api'

export default {
  name : 'SignUpForm',
  data: () => ({
      username: '',
      password: '',
      passwordConfirm: '',
      gender: '',
      age:'',
      occupation : '',
      show_password: false,
      valid: false,
      rules: {
          required: value => !!value || 'Required.',
          nameRules: v => v.length <= 10 || 'Name must be less than 10 characters',
          passwordRules: v => v.length >= 8 || 'Password must be more than 8 characters',
      },
      genders: [
          {text:  "Male", value : "M"},
          {text:  "Female", value : "F"},
      ],
      ages: [
          {text:  "Under 18", value : 1},
          {text:  "18-24", value : 18},
          {text:  "25-34", value : 25},
          {text:  "35-44", value : 35},
          {text:  "45-49", value : 45},
          {text:  "50-55", value : 50},
          {text:  "56+", value : 56},
      ],
      occupations: [
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
          {text:  "K-12 studen", value : 10},
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
      ],
  }),
  computed: {
      passwordConfirmRules() {
      return [
          () => (this.password === this.passwordConfirm) || '??',
      ]
    },
  },
  methods: {
      async signUpSend() {
          const data = {
            profiles: {
              'username': this.username,
              'password': this.password,
              'gender': this.gender,
              'age': this.age,
              'occupation' : this.occupation
            }
          }
          const resp = await api.signUp(data)
          this.$emit('signUpComplete')
      }
  },
}
</script>
