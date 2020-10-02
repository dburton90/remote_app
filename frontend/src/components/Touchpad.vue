<template lang="pug">
  q-card.custom-area.cursor-pointer.bg-blue( v-touch-pan.prevent.mouse="handlePan")
</template>

<script>
// import { debounce } from 'quasar';
import { socket } from 'boot/socket';

export default {
  methods: {
    handlePan({ evt, ...info }) {
      // native Javascript event
      // console.log(evt)
      socket.emit('mouse move', info.delta);
    },
  },
};

</script>

<style scoped lang="sass">
.custom-area
   width: 100%
   height: 480px

</style>
