<template>
      <div>
        <transition name="fade" mode="out-in">
          <ProfileView v-if="isProfile === true" @transForm="isProfile = !isProfile"/>
        </transition>
        <transition name="fade" mode="out-in" >
          <ProfileEdit v-if="isProfile === false" @transForm="isProfile = !isProfile"/>
        </transition>
      </div>
</template>

<script>
import ProfileView from '@/components/profile/ProfileView'
import ProfileEdit from '@/components/profile/ProfileEdit'

export default {
components: {
    ProfileView,
    ProfileEdit
  },
  data() {
    return{
      isProfile : true
    }
  }
}
</script>

<style scoped lang="scss">

</style>
