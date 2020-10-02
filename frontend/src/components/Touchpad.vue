<template lang="pug">
  .custom-area(@click="click")
    q-card.cursor-pointer.bg-blue(style="height: 100%", v-touch-pan.mouse="handlePan")
</template>

<script>
import { debounce } from 'quasar';
import { socket } from 'boot/socket';

export default {
  data() {
    return {
      clicks: 0,
      timer: undefined,
    };
  },
  methods: {
    handlePan({ evt, ...info }) {
      // native Javascript event
      // console.log(evt)
      socket.emit('mouse move', info.delta);
      this.clicks = 0;
    },
    click() {
      this.clicks += 1;
      if (this.clicks === 1) {
        const self = this;
        this.timer = setTimeout(() => {
          socket.emit('mouse click', 1);
          self.clicks = 0;
        }, 500);
      } else {
        clearTimeout(this.timer);
        socket.emit('mouse click', 2);
        this.clicks = 0;
      }
    },
  },
};

</script>

<style scoped lang="sass">
.custom-area
   width: 100%
   height: 480px

</style>
