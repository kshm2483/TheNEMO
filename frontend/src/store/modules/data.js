import api from '../../api'

// initial state
const state = {
  // shape: [{ id, title, genres, viewCnt, rating }]
  movieSearchList: [],
  userData: [],
}

// actions
const actions = {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params)
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.view_cnt,
      rating: d.average_rating,
      comments: d.rating,
      similarmovie: d.similarmovie
    }))
    commit('setMovieSearchList', movies)
  },
  async searchProfile({ commit }, params) {
    const resp = await api.searchProfile(params)
    const profile = resp.data
    commit('setProfileSearch', profile)
  }
}

// getters
const getters = {
  selectMovie: (state) => (id) => {
    return state.movieSearchList.find(movie => movie.id === id)
  }
}
// mutations
const mutations = {
  setMovieSearchList(state, movies) {
    state.movieSearchList = movies.map(m => m)
  },
  setProfileSearch(state, profile) {
    state.userData = profile
  }
}

export default {
  namespaced: true,
  state,
  actions,
  getters,
  mutations
}