export default {
  selectedMovie : ( state, payload ) => {
    if (payload) {
      state.selectedMovie.Activated = payload.varified
    } else {
      state.selectedMovie.Activated = false
    }
    state.selectedMovie.ActivatedMovie = payload
  },
  setMovieSearchList(state, payload) {
    state.movieSearchList = payload.map(m => m)
  },
  setProfileSearch(state, payload) {
    state.userData = payload
  }
}
