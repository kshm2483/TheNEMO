import Vue from 'vue'
import Vuex from 'vuex'
// import actions from './actions'
import mutations from './mutations'
import getters from './getters'
import actions from './actions'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieSearchList: [],
    userData: [],
    selectedMovie: {
      'Activated': null,
      'ActivatedMovie': null,
      'selectedInfo': 1,
    },
    userData: [],
  },
  mutations,
  getters,
  actions
})
