<template>
    <v-row>
        <v-col cols="10">
        <p>유저 목록에 대한 알고리즘</p>
        <div>
            <v-select
                :items="algorithms"
                v-model="configUser.method"
                item-value="value"
                item-text="text"
                label="Algorithms"
                id="AlgorithmsSelect"
            ></v-select>
            <v-slider
                v-model="configUser.params"
                min="2"
                max="50"
                thumb-label="always"
                label="params"
            ></v-slider>
            {{configUser.method}}
        </div>
        <v-btn @click="clusteruser">저굥</v-btn>
        <br>
        <br>
        <br>
        <br>
        <p>영화 목록에 대한 알고리즘</p>
        <div>
            <v-select
                :items="algorithms"
                v-model="configMovie.method"
                item-value="value"
                item-text="text"
                label="Algorithms"
                id="AlgorithmsSelect"
            ></v-select>
            <v-slider
                v-model="configMovie.params"
                min="2"
                max="50"
                
                thumb-label="always"
                label="params"
            ></v-slider>
        </div>
        <v-btn @click="clustermovie">저굥</v-btn>
        </v-col>
    </v-row>
</template>

<script>
import axios from 'axios'
import api from '@/api'
const apiUrl = '/api'
export default {
    data() {
        return {
            configUser: {
                method : '',
                params : ''
            },

            configMovie: {
                method : '',
                params : ''
            },
            
            algorithms : [
                {value:"K" ,text:'케이민지'},
                {value:"G" ,text:'가우스 엑스 마키나'},
                {value:"H" ,text:'하이라이스'},    
            ]
        }
    },
    mounted() {
        axios.get(`${apiUrl}/cluster/user/`).thne(res => {
            console.log(res)
        })
        axios.get(`${apiUrl}/cluster/movie/`).thne(res => {
            console.log(res)
        })
    },
     methods: {
        async clusteruser() {
            const data = { method: this.configUser.method, params: this.configUser.params }
            await api.goClusterUser(data)
        },
        async clustermovie() {
            const data = { method: this.configMovie.method, params: this.configMovie.params }
            await api.goClusterMovie(data)
        },
    }
}
</script>
<style>
    
</style>