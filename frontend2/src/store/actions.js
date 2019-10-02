import api from '@/api'
export default {
  async searchMovies({ commit }, params) {
    const resp = await api.searchMovies(params)
    const movies = resp.data.map(d => ({
      id: d.id,
      title: d.title,
      genres: d.genres_array,
      viewCnt: d.view_cnt,
      rating: d.average_rating,
      comments: d.rating,
      similarmovie: d.similarmovie,
      poster_url: d.poster_url,
      backdrop_url: d.backdrop_url,
      overview: d.overview,
      adult: d.adult,
    }))
    commit('setMovieSearchList', movies)
  },
  async searchProfile({ commit }, params) {
    const resp = await api.searchProfile(params)
    const payload = resp.data
    commit('setProfileSearch', payload)
  }
}
