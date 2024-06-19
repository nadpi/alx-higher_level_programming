#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      const arr = [];
      for (let j = 0; j < this.width; j++) {
        if (c) {
          arr.push(c);
        } else {
          arr.push('X');
        }
      }
      console.log(arr.join(''));
    }
  }
};
