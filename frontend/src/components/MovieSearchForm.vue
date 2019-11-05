<template>
  <v-form ref="form">

    <!-- <v-btn @click="onSwitch">search :{{ tab? "title": "genre"}}</v-btn> -->
    <v-layout>
      <v-flex xs10 >
      <v-btn  class="ma-1" @click="change(1)">title</v-btn>
      <v-btn  class="ma-1" @click="change(2)">genre</v-btn>
      <v-btn  class="ma-1" @click="change(3)">age</v-btn>
      <v-btn  class="ma-1" @click="change(4)">gender</v-btn>
      <v-btn  class="ma-1" @click="change(5)">occupation</v-btn>
      </v-flex>
      <v-flex xs2>
      <v-btn class="ma-1" @click="onSubmit" color="primary">Search</v-btn>
      </v-flex>
    </v-layout>
    <div>{{ this.$store.state.data.movieSearchList.length }} 개의 영화데이터
      <div v-show="check==1">
        <v-text-field v-model="title" label="영화 제목" />
        <v-layout justify-center pa-8>
        </v-layout>
      </div>
      <div v-show="check==2">
        <v-row justify="space-around">
          <v-select
          :items="genres"
          v-model="genre"
          label="Genre"
          item-value="text"
          id="genreSelect"
          required
        ></v-select>
        </v-row>
      </div>
      <div v-show="check==3">
        <v-select
          :items="ages"
          v-model="age"
          label="Age"
          item-value="value"
          item-text="text"
          id="AgeSelect"
          required
        ></v-select>
        <v-layout justify-center pa-10>
        </v-layout>
      </div>
      <div v-show="check==4">
       <v-checkbox v-for="item in chkItems" v-model="gender" class="mx-2" :label=item.text :value=item.value :key="item"></v-checkbox>
      </div>
      <div v-show="check==5">
        <v-select
          :items="occupations"
          v-model="occupation"
          label="Occupation"
          item-value="text"
          id="occupationSelect"
          required
        ></v-select>
      <v-layout justify-center pa-10>
      </v-layout>
      </div>
    </div>
  </v-form>
</template>

<script>
export default {
  props: {
    submit: {
      type: Function,
      default: () => {}
    }
  },
  data() {
    return {
      check:0,
      tab: true,
      title: "",
      genre: "",
      age: '',
      gender: '',
      occupation: '',
      chkItems: [
        { value: "M", text : "Male"},
        { value: "F", text : "Female"},
      ],
      genres: [
        {text: "Action"},{text: "Adventure"},
        {text: "Animation"},{text: "Children"},
        {text: "Comedy"},{text: "Crime"},
        {text: "Documentary"},{text: "Drama"},
        {text: "Fantasy"},{text: "Film-Noir"},
        {text: "Horror"},{text: "Musical"},
        {text: "Mystery"},{text: "Romance"},
        {text: "Sci-Fi"},{text: "Thriller"},
        {text: "War"},{text: "Western"},
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
    }
  },
  methods: {
    change (num){
      this.check = num      
    },
    onSubmit: function() {
      const params = {
        title: this.title,
        genre: this.genre,
        age:this.age,
        gender:this.gender,
        occupation: this.occupation,
      };
      this.submit(params);
    },
    onSwitch() {
      if (this.tab === true) {
        this.tab = false
        this.title = ""
      } else {
        this.tab = true
        this.genre = ""
      }
    }
  }
};
</script>