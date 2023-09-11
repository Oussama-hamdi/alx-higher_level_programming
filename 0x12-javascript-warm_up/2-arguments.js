#!/usr/bin/node

const argCount = process.argv.length - 2;
const arr = ['No argument', 'Argument found', 'Arguments found'];
console.log(argCount === 0 ? arr[0] : argCount === 1 ? arr[1] : arr[2]);
