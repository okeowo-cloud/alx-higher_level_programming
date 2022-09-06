#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let a = '';
      for (let j = 0; j < this.width; j++) a += (c === undefined) ? 'X' : c;
      console.log(a);
    }
  }
};
