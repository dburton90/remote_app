<template>
  <div :class="keyboardClass"></div>
</template>

<script>
import Keyboard from 'simple-keyboard';
import 'simple-keyboard/build/css/index.css';
import { debounce } from 'quasar';
import { socket } from '../boot/socket';

const TRANSLATOR = {
  '{tab}': 'tab',
  '{lock}': 'capslock',
  '{bksp}': 'backspace',
  '{enter}': 'enter',
  '{space}': 'space',
  '{shift}': 'shift',
};

export default {
  name: 'SimpleKeyboard',
  props: {
    keyboardClass: {
      default: 'simple-keyboard',
      type: String,
    },
  },
  data: () => ({
    keyboard: null,
    keys: [],
  }),
  mounted() {
    this.keyboard = new Keyboard({
      onChange: this.onChange,
      onKeyPress: this.onKeyPress,
    });
  },
  methods: {
    onKeyPress(button) {
      console.log(button);
      this.keys.push(TRANSLATOR[button] || button);
      this.emitKey();
      this.keyboard.setInput('');

      /**
       * If you want to handle the shift and caps lock buttons
       */
      if (button === '{shift}' || button === '{lock}') this.handleShift();
    },
    handleShift() {
      const currentLayout = this.keyboard.options.layoutName;
      const shiftToggle = currentLayout === 'default' ? 'shift' : 'default';

      this.keyboard.setOptions({
        layoutName: shiftToggle,
      });
    },
    emitKey() {
      socket.emit('key', this.keys);
      this.keys = [];
    },
  },
  created() {
    this.emitKey = debounce(this.emitKey, 500);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
