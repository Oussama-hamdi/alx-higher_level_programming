#!/usr/bin/node

const arg = process.argv[2];

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
if (isNaN(arg)) {
  console.log(1);
  process.exit();
} else {
  console.log(factorial(+arg));
}
