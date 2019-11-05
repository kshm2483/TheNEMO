import axios from 'axios'
import session from './modules/session'
import swal from 'sweetalert';

const apiUrl = '/api'

export default {
  searchMovies(params) {
    return axios.get(`${apiUrl}/movies/`, {
      params
    })
  },
  searchProfile(params) {
    if (typeof(params) === "number") {
      return axios.get(`${ apiUrl }/profile/${params}`)
    } else {
      return axios.get(`${ apiUrl }/profile/`, { params })  
    }
  },
  signUp(profiles) {
    return axios.post(`${ apiUrl }/auth/signup/`, profiles)
      .then(res => {
        if (res.status === 201) {
          return true
        } else {
          return false
        }
      })
  },
  logIn(form) {
    const data = JSON.stringify({
      username: form.id,
      password: form.pw
    })
    return axios.post(`${ apiUrl }/auth/login`, data, {
      // request headers에 데이터를 json type으로 보냄
      headers: {
        'Content-Type': 'application/json',
      }
    }).then(res => {
      if (res.data.data && res.data.status === true) {
        session.set('drf', res.data.data)
        swal({
          title : res.data.data.username + "님 반갑습니다!",
          text : "로그인에 성공 하였습니다.",
          icon: "success",
          button: false,
          timer: 2000,
        });
        return res.data.data.username
      }
      if (res.data.status === false) {
        swal({
          title : "아이디 혹은 비밀번호를 확인하세요.",
          text : "로그인에 실패했습니다.",
          icon: "error",
          button: false,
          timer: 2000,
          });
        return false
      }
    })
  },
  logOut() {
    return axios.post(`${ apiUrl }/auth/logout`)
      .then(res => {
        if (res.status === 200) {
          const data = JSON.parse(sessionStorage.getItem("drf"))
          swal({
            title : data.username + "님 안녕히 가십시오!",
            text : "로그아웃에 성공 하였습니다.",
            icon: "info",
            button: false,
            timer: 2000,
          });
          session.destroy()
          return true
        } else {
          alert('error')
          return false
        }
      })
  },
  goClusterUser(data) {
    const datas =JSON.stringify({
      method: data.method,
      params: data.params
    })
    return axios.post(`${apiUrl}/cluster/user/`,
      datas,{
        // request headers에 데이터를 json type으로 보냄
        headers: {
          'Content-Type': 'application/json',
        }

    }).then(res => {
      swal({
        title : "클러스터 완료",
        text : "아무튼 완료",
        icon: "success",
        button: false,
        timer: 2000,
      });
    })
  },
  goClusterMovie(data) {
    const datas =JSON.stringify({
      method: data.method,
      params: data.params
    })
    return axios.post(`${apiUrl}/cluster/movie/`,
      datas,{
        // request headers에 데이터를 json type으로 보냄
        headers: {
          'Content-Type': 'application/json',
        }
    }).then(res=> {
          swal({
            title : "클러스터 완료",
            text : "아무튼 완료",
            icon: "success",
            button: false,
            timer: 2000,
          });
        }
      )
  },
  goUserCustomizedRecommendation(data) {
    const datas =JSON.stringify({
      method: data.method
      })
    return axios.post(`${apiUrl}/cluster/custom`,
      datas,{
        // request headers에 데이터를 json type으로 보냄
        headers: {
          'Content-Type': 'application/json',
        }
    }).then(res=> {
          swal({
            title : "유서 추천 영화 알고리즘",
            text : "아무튼 완료",
            icon: "success",
            button: false,
            timer: 2000,
          });
        }
      )
  },
  patchProfileData(data) {
    const datas = JSON.stringify({
      occupation: data.occupation,
      age: data.age,
      description : data.description
    })
    return axios.patch(`${apiUrl}/profile/${data.id}`,
      datas,{
        // request headers에 데이터를 json type으로 보냄
        headers: {
          'Content-Type': 'application/json',
        }
    })
  },
  playSubscription(data) {
    return axios.post(`${apiUrl}/subscription/${data.id}`,{
        // request headers에 데이터를 json type으로 보냄
        headers: {
          'Content-Type': 'application/json',
        }
      }).then(res => {
          if (res.data.data && res.status === 200) {
            session.set('drf', res.data.data)
            return true
          }
          if (res.data.status === false) {
            return false
          }
        })
    },
  newUserRating(data) {
    const datas = JSON.stringify({
      movie: data.movie,
      user: data.user,
      rating : data.rating,
      rating_date : data.rating_date
    })
    return axios.patch(`${apiUrl}/rating/`, datas, {
        // request headers에 데이터를 json type으로 보냄
        headers: {
          'Content-Type': 'application/json',
        }
      }).then(res => {
          if (res.status === 200) {
            return true
          }
          if (res.status !== 200) {
            return false
          }
        })
    },
}
