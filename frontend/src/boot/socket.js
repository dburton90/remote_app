import io from 'socket.io-client';

// "async" is optional;
// more info on params: https://quasar.dev/quasar-cli/cli-documentation/boot-files#Anatomy-of-a-boot-file
export const socket = io();

export default async (/* { app, router, Vue ... } */) => {
  // something to do

  socket.on('connect', () => {
    console.log('connected');
  });

  socket.on('disconnect', () => {
    console.log('disconnected');
  });

  socket.on('bravo test', () => console.log('bravo test called'));
  socket.on('bravo connected', () => console.log('bravo connected called'));
};
