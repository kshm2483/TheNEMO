<template>
    <div class="newImg">
        <img style="cursor:default width:260px;height:373px; min-width:250px; max-width: 250px;" :src="imgData.imgSrc" alt="moviePoster" onerror="this.onerror=null; this.src='http://kaverisias.com/wp-content/uploads/2018/01/catalog-default-img.gif'">
        <div class="testRatings__detail">
            <div class="testRatings__detail-head">
              {{imgData.title}}
              <br>
              {{imgData.genres}}
            </div>
            <div class="separater"></div>
            <div class="testRatings__detail-body">
                <fieldset class="rating" @change="newRating">
                  <input type="radio" :id="imgData.title+'5'" :name="imgData.title+'5'" value="5" v-model="editScore" /><label class = "full" :for="imgData.title+'5'" title="Awesome - 5 stars"></label>
                  <!-- <input type="radio" :id="imgData.title+'4.5'" :name="imgData.title+'4.5'" value="4.5" v-model="imgData.rating" /><label class="half" :for="imgData.title+'4.5'" title="Pretty good - 4.5 stars" @click="newRating()"></label> -->
                  <input type="radio" :id="imgData.title+'4'" :name="imgData.title+'4'" value="4" v-model="editScore"/><label class = "full" :for="imgData.title+'4'" title="Pretty good - 4 stars"></label>
                  <!-- <input type="radio" :id="imgData.title+'3.5'" :name="imgData.title+'3.5'" value="3.5" v-model="imgData.rating" /><label class="half" :for="imgData.title+'3.5'" title="Meh - 3.5 stars" @click="newRating()"></label> -->
                  <input type="radio" :id="imgData.title+'3'" :name="imgData.title+'3'" value="3" v-model="editScore"/><label class = "full" :for="imgData.title+'3'" title="Meh - 3 stars"></label>
                  <!-- <input type="radio" :id="imgData.title+'2.5'" :name="imgData.title+'2.5'" value="2.5" v-model="imgData.rating" /><label class="half" :for="imgData.title+'2.5'" title="Kinda bad - 2.5 stars" @click="newRating()"></label> -->
                  <input type="radio" :id="imgData.title+'2'" :name="imgData.title+'2'" value="2" v-model="editScore" /><label class = "full" :for="imgData.title+'2'" title="Kinda bad - 2 stars"></label>
                  <!-- <input type="radio" :id="imgData.title+'1.5'" :name="imgData.title+'1.5'" value="1.5" v-model="imgData.rating" /><label class="half" :for="imgData.title+'1.5'" title="Meh - 1.5 stars" @click="newRating()"></label> -->
                  <input type="radio" :id="imgData.title+'1'" :name="imgData.title+'1'" value="1"  v-model="editScore"/><label class = "full" :for="imgData.title+'1'" title="Sucks big time - 1 star"></label>
                  <!-- <input type="radio" :id="imgData.title+'0.5'" :name="imgData.title+'0.5'" value="0.5" v-model="imgData.rating"/><label class="half" :for="imgData.title+'0.5'" title="Sucks big time - 0.5 stars" @click="newRating()"></label> -->
              </fieldset>
            </div>
          </div>
    </div>
</template>

<script>
import api from '@/api'
export default {
  props: {
    imgData: {
      type: Object,
      required: true
    },
  },
  data: () => ({
    checkHover : false,
    editScore: 0,
  }),
  computed: {
  },
  methods: {
    async newRating() {
        let currentDateWithFormat = new Date().toJSON().slice(0,10).replace(/-/g,'');
        const data = JSON.parse(sessionStorage.getItem("drf"))
        let form = {
            "user" : data.id,
            "movie" : this.imgData.id,
            "rating" : this.editScore,
            "rating_date" : currentDateWithFormat
            }
        await api.newUserRating(form)

        if (this.imgData.chkRated === false) {
          this.imgData.chkRated = true
           this.$EventBus.$emit('increment', 1);
        }
    }
  }
}
</script>

<style lang="scss" scoped>
.separater {
  background: rgb(141,141,141) !important;
}
</style>
