import Vue from 'vue'
import VueRouter from 'vue-router'
import EmptyPage from '../components/pages/EmptyPage'
import MovieSearchPage from '../components/pages/movies/MovieSearchPage'
import MovieDetailPage from '../components/pages/movies/MovieDetailPage'
import UserDetailPage from '../components/pages/users/UserDetailPage'
import LoginPage from '../components/pages/LoginPage'
import AdminPage from '../components/pages/admins/AdminPage'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    { path: '/', component: EmptyPage, name: 'home' },
    { path: '/movies/search', component: MovieSearchPage, name: 'movie-search' },
    { path: '/movies/:movie_id', component: MovieDetailPage, name: 'movie-detail'},
    { path: '/users/:user_id', component: UserDetailPage, name: 'user-detail'},
    { path: '/login', component: LoginPage, name: 'login-page'},
    { path: '/admin', component: AdminPage, name: 'admin-page'},
  ],
  scrollBehavior() {
    return { x: 0, y: 0 }
  },
})

export default router