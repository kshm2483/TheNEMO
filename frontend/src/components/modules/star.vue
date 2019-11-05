<template>
  <div class="testRatings__detail-body">
    <fieldset class="rating">
      <input type="radio" :id="score.user+10" :name="score.user+10" value="5" v-model="score.rating"/><label class = "full" for="star5" title="Awesome - 5 stars"></label>
      <input type="radio" :id="score.user+9" :name="score.user+9" value="4.5" v-model="score.rating"/><label class="half" for="star4half" title="Pretty good - 4.5 stars"></label>
      <input type="radio" :id="score.user+8" :name="score.user+8" value="4" v-model="score.rating"/><label class = "full" for="star4" title="Pretty good - 4 stars"></label>
      <input type="radio" :id="score.user+7" :name="score.user+7" value="3.5" v-model="score.rating"/><label class="half" for="star3half" title="Meh - 3.5 stars"></label>
      <input type="radio" :id="score.user+6" :name="score.user+6" value="3" v-model="score.rating"/><label class = "full" for="star3" title="Meh - 3 stars"></label>
      <input type="radio" :id="score.user+5" :name="score.user+5" value="2.5" v-model="score.rating"/><label class="half" for="star2half" title="Kinda bad - 2.5 stars"></label>
      <input type="radio" :id="score.user+4" :name="score.user+4" value="2" v-model="score.rating"/><label class = "full" for="star2" title="Kinda bad - 2 stars"></label>
      <input type="radio" :id="score.user+3" :name="score.user+2" value="1" v-model="score.rating"/><label class = "full" for="star1" title="Sucks big time - 1 star"></label>
      <input type="radio" :id="score.user+2" :name="score.user+1" value="0.5" v-model="score.rating"/><label class="half" for="starhalf" title="Sucks big time - 0.5 stars"></label>
      <input type="radio" :id="score.user+1" :name="score.user+3" value="1.5" v-model="score.rating"/><label class="half" for="star1half" title="Meh - 1.5 stars"></label>
    </fieldset>
  </div>
</template>

<script>
export default {
  props: {
    score: {
      type: Object,
      required: true
    },
  }
}
</script>

<style scoped lang="scss">
</style>
