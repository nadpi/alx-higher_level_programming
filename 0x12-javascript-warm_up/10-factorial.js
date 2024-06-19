#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length === 2) {
  console.log(1);
} else {
  let num = Number(argv[2]);
  let factorial = 1;
  for (num; num > 0; num--) {
    factorial *= num;
  }
  console.log(factorial);
}
