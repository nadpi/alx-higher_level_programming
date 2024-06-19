#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length < 4) {
  console.log(0);
} else {
  let big = Number(argv[2]);
  for (let i = 3; i < argv.length; i++) {
    if (Number(argv[i]) > big) {
      big = argv[i];
    }
  }
  let secbig = 0;
  for (let i = 2; i < argv.length; i++) {
    if (Number(argv[i]) > secbig && Number(argv[i]) !== big) {
      secbig = argv[i];
    }
  }
  console.log(secbig);
}
