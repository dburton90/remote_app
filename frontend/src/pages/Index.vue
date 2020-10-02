<template lang="pug">
  q-page(flex, flex-center)
    q-btn(@click="open(p)", v-for="p in programs") {{p}}
    touchpad
</template>

<script>
import Touchpad from 'components/Touchpad';
import { socket } from '../boot/socket';

const PROGRAMS = ['firefox', 'spotify'];

export default {
  name: 'PageIndex',
  components: { Touchpad },
  methods: {
    open(program) {
      socket.emit('program', { name: program, action: 'focus' });
    },
  },
  created() {
    this.programs = PROGRAMS;
  },
};
</script>
