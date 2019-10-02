<template>
  <div class="moviePage">
      <span class="newRatingTitle">영화 평점 주세요</span>
      <newRatingCategory :movieItems="movieItems"/>
      <div class="lds-bg">
        <div v-if="loadScroll" class="lds-dual-ring"></div>
      </div>
    </div>
</template>

<script>
import axios from 'axios'
import newRatingCategory from '@/components/newrating/newRatingCategory'

export default {
  components: {
    newRatingCategory
  },
  data: () => ({
    movieItems: [{genre:'action', items: [1,2,3,4,5,6,7,8,9,10,11,12]}],
    loadCall: false,
    loadScroll: false,
    persons: []
  }),
  mounted() {
    // MovieImg.vue => 영화 정보 오픈 시 스크롤
    this.$EventBus.$on('movieInfoActive', (payload) => {
      this.scrollCard(payload.varified)
    })
    this.scroll(this.person)
  },
  beforeMount() {
    this.getInitialUsers()
  },
  methods: {
    scrollCard(locationId) {
      const element = document.getElementById(locationId)
      const elemRect = element.getBoundingClientRect()
      const offset = elemRect.bottom + window.pageYOffset - 100
      window.scrollTo({top: offset, behavior: 'smooth'})
    },
    getInitialUsers () {
      for (var i = 0; i < 5; i++) {
        axios.get(`https://randomuser.me/api/`)
          .then(response => {
            this.persons.push(response.data.results[0])
          })
      }
    },
    scroll(person) {
      window.onscroll = () => {
        let bOfW = Math.round(document.documentElement.scrollTop + window.innerHeight) >= document.documentElement.offsetHeight
        if (bOfW && this.loadCall === false) {
          this.loadCall = true
          this.loadScroll = true
          axios.get(`https://randomuser.me/api/`)
            .then(response => {
              let i = this.movieItems[0].items.length+1
              let a = i
              for (a; a < i+12; a++) {
                this.movieItems[0].items.push(a)
              }
              this.loadScroll = false
              this.loadCall = false
            })

        }
      }
    }
  }
}
</script>
<style lang="scss">
.lds-bg {
  position: relative;
  height: 20vh;
  width: 100%;
  background: linear-gradient(to bottom, rgba(70, 70, 70, 0), rgb(18, 18, 18));
}
.lds-dual-ring {
  display: inline-block;
  position: absolute;
  bottom: 5vh;
  width: 64px;
  height: 64px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 46px;
  height: 46px;
  margin: 1px;
  border-radius: 50%;
  border: 5px solid #fff;
  border-color: #fff transparent #fff transparent;
  animation: lds-dual-ring 0.5s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
