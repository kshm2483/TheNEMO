<template>
  <v-sheet class="mx-auto" max-width="800">
    <v-slide-group
      v-model="model" class="pa-4"
      active-class="transparent" show-arrows
    >
      <v-slide-item
        v-for="item in itemList"
        :key="item"
        v-slot:default="{ active, toggle }"
      >
        <v-card
          class="ma-4"
          height="300"
          width="210"
          @click="toggle"
        >
          {{item}}
        </v-card>
      </v-slide-item>
    </v-slide-group>
  </v-sheet>
</template>

<script>
export default {
  props: ['itemList'],
  data: () => ({
    model: null,
  }),
}
</script>