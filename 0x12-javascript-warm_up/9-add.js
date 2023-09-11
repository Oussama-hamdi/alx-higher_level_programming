#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  return !isNaN(a) && !isNaN(b) ? +a + +b : NaN;
}
console.log(add(args[2], args[3]));
