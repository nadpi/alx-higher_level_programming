#!/usr/bin/node
const { argv } = require('node:process');
let cnt = 0;
argv.forEach((index) => {
  cnt = cnt + 1;
});
if (cnt === 2 || isNaN(Number(argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argv[2]);
}
