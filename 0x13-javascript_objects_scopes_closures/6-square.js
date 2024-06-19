#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
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
