<template>
  <div>
    <div class="mainPage" v-for="item in sectionImg" :key="item.name">
        <img :src="item.url" :alt="item.name" class="mainPage__image" :id="item.name">
        <div class="mainPage-body">
          <div class="mainPage-body__text">
            {{item.text}}
          </div>
          <div class="mainPage-body__sub">
            {{item.sub}}
          </div>
          <div class="btn btn--primary btn--md" @click="go()">회원가입</div>
        </div>
        <div>
          
        </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return{
      sectionImg: [
        {url:require("@/assets/image/breaking.jpg"), name:'breaking', text: '1,346,874개 평가 기반 최고의 추천 엔진', sub:'5가지 방식의 다양한 알고리즘 적용'},
        {url:require('@/assets/image/gump.jpg'), name:'gump', text: '당신만을 위한 추천 영화', sub:'지금까지 이런 추천 서비스는 없었다!'},
        {url:require('@/assets/image/Lisbon.jpg'), name:'lisbon', text: '어멋! 이건 구독해야 해!', sub:'지금 바로 구독하세요.'},
      ]
    }
  },
  methods: {
    go() {
      this.$router.push(
        { name: 'Sign', params: { directSignup: true }}
      )
    },
  },
}
</script>

<style lang="scss" scoped>
.mainPage {
  margin: 0px;
  width: 100%;
  height: 100vh;
  &__image {
    width:100%; 
    height:100%; 
    background-color: black; 
    opacity: 0.6;
  }

  &-body {
    position: relative; 
    top: -60vh;
    z-index: 100;
    color: white;
    font-weight: 400;
    user-select: none;
    
    &__text {
      letter-spacing: -3px;
      font-size: 60px;
    }

    &__sub {
      padding-top: var(--space-md);
      padding-bottom: var(--space-md);
      color: rgba(240,240,240,0.7);
      font-size: 20px;
    }
    
  } 
  
}
</style>
