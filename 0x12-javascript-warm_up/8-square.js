#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length === 2 || isNaN(Number(argv[2]))) {
  console.log('Missing size');
}
let i = 0;
let j = 0;
let arr = [];
for (i; i < argv[2]; i++) {
  arr = [];
  for (j = 0; j < argv[2]; j++) {
    arr.push('X');
  }
  console.log(arr.join(''));
}
