<template lang="pug">
  q-page(flex, flex-center)
    q-btn(@click="sendMessage") send test
</template>

<script>
import { socket } from '../boot/socket';

export default {
  name: 'PageIndex',
  methods: {
    sendMessage() {
      console.log('emitting test');
      socket.emit('test', 'xxxxxx', '');
    },
  },
};
</script>
