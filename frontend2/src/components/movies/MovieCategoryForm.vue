<template>
  <div>
    <h1>보고싶은 작품을 찾아보세요</h1>
    <select class="categoryForm" :name="genre" v-model="genre" @change="chk">
      <option
        :value="item.text"
        :key="item.text"
        v-for="item in genres">{{ item.text }}</option>
    </select>
    <select class="categoryForm" :name="age" v-model="age"  @change="chk">
      <option
        :value="item.text"
        :key="item.text"
        v-for="item in ages">{{ item.text }}</option>
    </select>
    <select class="categoryForm" :name="occupation" v-model="occupation"  @change="chk">
      <option
        :value="item.text"
        :key="item.text"
        v-for="item in occupations">{{ item.text }}</option>
    </select>
    <select class="categoryForm categoryForm__Sort" :name="sortOption" v-model="sortOption"  @change="chk">
      <option
        :value="item.text"
        :key="item.text"
        v-for="item in sortOptions">{{ item.text }}</option>
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      check:0,
      tab: true,
      title: "",
      genre: "All genres",
      age: "All ages",
      gender: "",
      occupation: "All occupations",
      sortOption: "view: desc",
      chkItems: [
        { value: "M", text : "Male"},
        { value: "F", text : "Female"},
      ],
      genres: [
        {text: "All genres"},
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
        {text:  "All ages", value : 0},
        {text:  "Under 18", value : 1},
        {text:  "18-24", value : 18},
        {text:  "25-34", value : 25},
        {text:  "35-44", value : 35},
        {text:  "45-49", value : 45},
        {text:  "50-55", value : 50},
        {text:  "56+", value : 56},
      ],
      occupations: [
        {text:  "All occupations", value : 0},
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
      sortOptions: [
        {text:  "view: desc"},
        {text:  "view: asc"},
        {text:  "rating: desc"},
        {text:  "rating: asc"},
      ]
    }
  },
  methods: {
    chk() {
      console.log(this.genre, this.age, this.occupation)
    }
  }
}
</script>

<style scoped lang="scss">
h1 {
  color: $white;
  text-align: left;
  margin: {
    left: 8vw;
    top: 20vh;
  }
}
.categoryForm {
  margin: {
    right: 1vw;
  }
  padding: var(--space-xs);
  border: none;
  border-radius: calc(0.3 * var(--radius-sm));

  background-color:grey;
  width: 15vw;
  height: 7vh;

  color: white;
  font-size: 1.4em;
  &__Sort {
    margin: {
      left: 20vw;
    }
  }
}
</style>
