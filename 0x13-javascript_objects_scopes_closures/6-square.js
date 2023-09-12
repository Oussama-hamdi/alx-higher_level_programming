#!/usr/bin/node

const Sq = require('./5-square');

class Square extends Sq {
  charPrint (c) {
    for (let i = 0; i < this.width; ++i) {
      console.log((c || 'X').repeat(this.width));
    }
  }
}

module.exports = Square;
