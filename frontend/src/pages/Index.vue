<template lang="pug">
  q-page(flex, flex-center)
    .q-pa-md.q-gutter-sm
      q-btn(v-for="k in defaultKeys", :key="k.name", @click="clickKey(k)") {{k.name}}
    .q-pa-md.q-gutter-sm
      q-btn(v-for="k in keys", :key="k.name", @click="clickKey(k)") {{k.name}}
    .q-pa-md.q-gutter-sm
      q-btn(@click="open(p)", v-for="p in programs", :key="p") {{p}}
    simple-keyboard()
    touchpad
</template>

<script>
import Touchpad from 'components/Touchpad';
import SimpleKeyboard from 'components/SimpleKeyboard';
import { mapActions, mapGetters } from 'vuex';
import { socket } from '../boot/socket';

const PROGRAMS = ['firefox', 'spotify'];

export default {
  name: 'PageIndex',
  components: { SimpleKeyboard, Touchpad },
  computed: {
    ...mapGetters({
      keys: 'programs/currentKeys',
      defaultKeys: 'programs/defaultKeys',
    }),
  },
  methods: {
    ...mapActions({
      setProgram: 'programs/programFocus',
      loadPrograms: 'programs/load',
    }),
    open(program) {
      this.setProgram({ name: program });
    },
    clickKey(key) {
      socket.emit('hotKey', key.keys);
    },
  },
  created() {
    this.loadPrograms();
    this.programs = PROGRAMS;
  },
};
</script>
