<template lang="pug">
  q-page(flex, flex-center)
    q-btn(@click="sendMessage") send test
    touchpad
</template>

<script>
import Touchpad from 'components/Touchpad';
import { socket } from '../boot/socket';

export default {
  name: 'PageIndex',
  components: { Touchpad },
  methods: {
    sendMessage() {
      console.log('emitting test');
      socket.emit('test', 'xxxxxx', '');
    },
  },
};
</script>
