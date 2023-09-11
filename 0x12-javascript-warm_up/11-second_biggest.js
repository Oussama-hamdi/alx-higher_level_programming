#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const newArr = args.map(Number);
  newArr.sort((a, b) => b - a);
  console.log(newArr[1] || newArr[0]);
}
