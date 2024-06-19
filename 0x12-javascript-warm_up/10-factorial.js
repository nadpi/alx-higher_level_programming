#!/usr/bin/node
const { argv } = require('node:process');
let num = Number(argv[2]);
function fact (num) {
  let factorial = 1;
  for (num; num > 0; num--) {
    factorial *= num;
 }
  return factorial;
}
console.log(fact(num));
