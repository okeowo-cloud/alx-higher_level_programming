#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) [this.width, this.height] = [w, h];
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let a = '';
      for (let j = 0; j < this.width; j++) a += 'X';
      console.log(a);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
