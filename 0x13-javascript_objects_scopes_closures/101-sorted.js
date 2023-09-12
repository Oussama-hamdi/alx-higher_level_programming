#!/usr/bin/node

const dict = require('./101-data').dict;

const list = Object.entries(dict);
const myDict = {};

for (let i = 0; i < list.length; ++i) {
  const key = list[i][1];
  const value = list[i][0];

  if (!myDict[list[i][1]]) {
    myDict[list[i][1]] = [];
  }
  myDict[key].push(value);
}

console.log(myDict);
