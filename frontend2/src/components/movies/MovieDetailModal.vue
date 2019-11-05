<template>
    <transition name="modal" v-if="showModal">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="modal-container">

            <img :src="imgData.imgSrc" alt="moviePoster" style="height:500px; min-width:300px;" onerror="this.onerror=null; this.src='http://kaverisias.com/wp-content/uploads/2018/01/catalog-default-img.gif'">
            <div class="modal-detail">
              <div class="modal-header">
                <div>
                  <slot name="header">
                    <h2>{{ imgData.title }}</h2>
                      <div class="testRatings__detail-body" style="display: inline-block;">
                        <fieldset class="rating" @change="newRating()">
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
                  </slot>
                </div>
              </div>

              <div class="modal-body">
                <slot name="body">
                  <h3>Genres</h3>
                  <li v-for="genre in imgData.genres.slice(0, imgData.genres.length-1)" :key="genre" style="display:inline;" > {{genre}} |</li>
                  <li v-for="genre in imgData.genres.slice(imgData.genres.length-1, imgData.genres.length)" :key="genre" style="display:inline;" > {{genre}} </li>
                </slot>
              </div>

              <div class="modal-footer">
                <slot name="footer">
                  <h3>Overview</h3>
                  {{ imgData.overview }}
                </slot>
              </div>
              <!--rating 준 user-->
              <h3>User Rating</h3>
              <div class="modal-rating">
                <div v-for="info in scoredData" :key="info.id">
                    <ul class="rating">
                      <span> {{ info.user }}</span>
                      <input type="radio" :id="info.user+'5'" :name="info.user+'5'" value="5" v-model="info.rating" /><label class = "full" :for="info.user+'5'" title="Awesome - 5 stars"></label>
                      <!-- <input type="radio" :id="imgData.title+'4.5'" :name="imgData.title+'4.5'" value="4.5" v-model="imgData.rating" /><label class="half" :for="imgData.title+'4.5'" title="Pretty good - 4.5 stars" @click="newRating()"></label> -->
                      <input type="radio" :id="info.user+'4'" :name="info.user+'4'" value="4" v-model="info.rating"/><label class = "full" :for="info.user+'4'" title="Pretty good - 4 stars" ></label>
                      <!-- <input type="radio" :id="imgData.title+'3.5'" :name="imgData.title+'3.5'" value="3.5" v-model="imgData.rating" /><label class="half" :for="imgData.title+'3.5'" title="Meh - 3.5 stars" @click="newRating()"></label> -->
                      <input type="radio" :id="info.user+'3'" :name="info.user+'3'" value="3" v-model="info.rating"/><label class = "full" :for="info.user+'3'" title="Meh - 3 stars" ></label>
                      <!-- <input type="radio" :id="imgData.title+'2.5'" :name="imgData.title+'2.5'" value="2.5" v-model="imgData.rating" /><label class="half" :for="imgData.title+'2.5'" title="Kinda bad - 2.5 stars" @click="newRating()"></label> -->
                      <input type="radio" :id="info.user+'2'" :name="info.user+'2'" value="2" v-model="info.rating" /><label class = "full" :for="info.user+'2'" title="Kinda bad - 2 stars" ></label>
                      <!-- <input type="radio" :id="imgData.title+'1.5'" :name="imgData.title+'1.5'" value="1.5" v-model="imgData.rating" /><label class="half" :for="imgData.title+'1.5'" title="Meh - 1.5 stars" @click="newRating()"></label> -->
                      <input type="radio" :id="info.user+'1'" :name="info.user+'1'" value="1"  v-model="info.rating"/><label class = "full" :for="info.user+'1'" title="Sucks big time - 1 star" ></label>
                      <!-- <input type="radio" :id="imgData.title+'0.5'" :name="imgData.title+'0.5'" value="0.5" v-model="imgData.rating"/><label class="half" :for="imgData.title+'0.5'" title="Sucks big time - 0.5 stars" @click="newRating()"></label> -->
                  </ul>
                </div>
              </div>


              <div class="btn btn--primary modal-default-button" @click="change()">
                    OK
              </div>
              </div>
            </div>
          </div>
        </div>
    </transition>
</template>

<script>
  import api from '@/api'
  import session from '@/api/modules/session'
  import swal from 'sweetalert';
  export default {
  props: {
    movieInfo: {
      type: Object,
      required: true
    },
    imgData: {
      type: Object,
      required: true
    },
    showModal: {
      type: Boolean
    }
  },

  data: function() {
      return {
          changeModal: true,
          editScore: 0,
          callValue: false
      }
  },

  computed: {
    scoredData () {
      return this.movieInfo.rating
    }
  },
  watch: {
    scoredData() {
      if (!this.callValue) {
        this.editScore = this.movieInfo.rating.filter(rate => rate.user === session.get())[0].rating
        this.callValue = true
      }
    }
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
    else {
        swal({
          title : `${this.editScore}점 줬다`,
          text: "\n",
          icon: "success",
          button: false,
          timer: 1000})
    }
    },
    change() {
      this.$emit('close', false)
    }
    }
  }

</script>

<style lang="scss" scope>
/*modal*/
ul {
  padding: 0px;
  width: 80%;

  span{
    font-weight: 700;
    font-size: 20px;
    line-height: 40px;
  }
}

.modal-detail{
  padding-left: 20px;
  text-align: start;
}
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  display: flex;
  width: 850px;
  height: auto;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
.modal-rating {
  height: 250px;
  overflow: auto;
}

.rating > input:checked ~ label/* show gold star when clicked */
{color: red !important;}/* hover previous stars in list */

.rating:not(:checked) > label:hover, /* hover current star */
.rating:not(:checked) > label:hover ~ label { color: lightgrey !important;}

.rating > input:checked + label:hover, /* hover current star when changing rating */
.rating > input:checked ~ label:hover
{ color: red !important;  }
.rating > label:hover ~ input:checked ~ label, /* lighten current selection */
.rating > input:checked ~ label:hover ~ label {
  color: red !important;
}
</style>
