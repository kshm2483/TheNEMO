<template>
    <div class="flexCenter" style="color: white;">
        어드민 페이지입니다.

        <div>
            <select class="categoryForm" :name="pickedCorA" v-model="pickedCorA" @change="changeDefalut()">
                <option
                    :value="item.text"
                    :key="item.text"
                    v-for="item in choiceCorA">
                    {{ item.text }}
                </option>
            </select>

            <select class="categoryForm" :name="pickedMorU" v-model="pickedMorU" @change="changeDefalut()">
                <option
                    :value="item.text"
                    :key="item.text"
                    v-for="item in choiceMorU" >
                    {{ item.text }}
                </option>
            </select>
        </div>

        <div v-if="pickedCorA === 'Cluster'">
            <div v-if="pickedMorU==='Movie'">
                <select :name="configData.method" class="categoryForm" v-model="configData.method" >
                    <option :value="item.value" v-for="item in clusters" :key="item.value">{{item.text}}</option>
                </select>
                <div class="slidecontainer">
                    <input type="range" min="1" max="50" class="slider" id="myRange" v-model="configData.params">
                </div>
            </div>
            <div v-if="pickedMorU==='User'">
                <select :name="configData.method" class="categoryForm" v-model="configData.method" >
                    <option :value="item.value" v-for="item in clusters" :key="item.value">{{item.text}}</option>
                </select>
                <div class="slidecontainer">
                    <input type="range" min="1" max="50" class="slider" id="myRange" v-model="configData.params">
                </div>
            </div>
        </div>

        <div v-if="pickedCorA === 'Algorithm'">
            <div v-if="pickedMorU==='Movie'">
                <select :name="configData.method" class="categoryForm" v-model="configData.method" >
                    <option :value="item.value" v-for="item in Algorithms" :key="item.value">{{item.text}}</option>
                </select>
            </div>
            <div v-if="pickedMorU==='User'">
                <select :name="configData.method" class="categoryForm" v-model="configData.method" >
                    <option :value="item.value" v-for="item in Algorithms" :key="item.value">{{item.text}}</option>
                </select>
            </div>
        </div>

        <div class="btn btn--primary btn--lg" @click="playRecommend()" :class="{'btn--disabled' : checkAll()}">저기용</div>
    </div>

</template>
<script>
import api from '@/api'

export default {
    data() {
        return {
            pickedCorA: 'Choice C or A',
            pickedMorU: 'Choice M or U',

            configData: {method : '', params : ''},

            choiceCorA: [
                {text: "Choice C or A", value:""},
                {text: "Cluster", value:""},
                {text: "Algorithm", value:""},
                ],

            choiceMorU: [
                {text: "Choice M or U", value:""},
                {text: "Movie", value:""},
                {text: "User", value:""},
            ],

            clusters : [
                {text:'Choice Method', value:""},
                {text:'케이민지', value:"K"},
                {text:'가우스 엑스 마키나', value:"G"},
                {text:'하이라이스', value:"H"},
            ],

            Algorithms : [
                {text:'Choice Method', value:""},
                {text:'부산경남대표방송 KNN', value:"knn" ,},
                {text:'빨간약 파란약', value:"matrix"},
            ],
        }
    },
    mounted() {
        // axios.get(`${apiUrl}/cluster/user/`).thne(res => {
        //     console.log(res)
        // })
        // axios.get(`${apiUrl}/cluster/movie/`).thne(res => {
        //     console.log(res)
        // })
    },
     methods: {
        checkAll() {
            if (this.pickedCorA==="Cluster") {
                if (this.configData.method !== '' && this.configData.params !== 0) {
                    return false
                }
                else {
                    return true
                }
            } else {
                 if (this.configData.method !== '') {
                    return false
                }
                else {
                    return true
                }
            }
        },
        changeDefalut() {
            this.configData.method = ''
            this.configData.params = 0
        },
        async playRecommend() {

            if (this.pickedCorA==="Cluster") {
                if (this.pickedMorU === "User") {
                    const data = { method: this.configData.method, params: this.configData.params }
                    await api.goClusterUser(data)
                }
                else {
                    const data = { method: this.configData.method, params: this.configData.params }
                    await api.goClusterMovie(data)
                }
            } else {
                if (this.configData.method === "knn") {
                    if (this.pickedMorU === "User") {
                        const data = { method: this.configData.method}
                        await api.goClusterUser(data)
                    }
                    else {
                        const data = { method: this.configData.method}
                        await api.goClusterMovie(data)
                    }
                }
                else {
                    const data = { method: this.configData.method}
                    await api.goUserCustomizedRecommendation(data)
                }
            }
        }
    }
}
</script>
<style lang="scss">
.flexCenter{
    flex-direction: column;
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

.slidecontainer {
  width: 100%; /* Width of the outside container */
}

/* The slider itself */
.slider {
  -webkit-appearance: none;  /* Override default CSS styles */
  appearance: none;
  width: 100%; /* Full-width */
  height: 25px; /* Specified height */
  background: #d3d3d3; /* Grey background */
  outline: none; /* Remove outline */
  opacity: 0.7; /* Set transparency (for mouse-over effects on hover) */
  -webkit-transition: .2s; /* 0.2 seconds transition on hover */
  transition: opacity .2s;
  border-radius: var(--space-md);
}

/* Mouse-over effects */
.slider:hover {
  opacity: 1; /* Fully shown on mouse-over */
}

/* The slider handle (use -webkit- (Chrome, Opera, Safari, Edge) and -moz- (Firefox) to override default look) */
.slider::-webkit-slider-thumb {
  -webkit-appearance: none; /* Override default look */
  appearance: none;
  width: 25px; /* Set a specific slider handle width */
  height: 25px; /* Slider handle height */
  background: $primary; /* Green background */
  border-radius: 50%;
  cursor: pointer; /* Cursor on hover */
}

.slider::-moz-range-thumb {
  width: 25px; /* Set a specific slider handle width */
  height: 25px; /* Slider handle height */
  background: #4CAF50; /* Green background */
  cursor: pointer; /* Cursor on hover */
}
</style>
