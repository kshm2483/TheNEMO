export default {
  getMovieToggle: state => state.selectedMovie.Activated,
  getMovieInfo: state => state.selectedMovie.ActivatedMovie,
  getUserMovieData: state => state.userData
}
