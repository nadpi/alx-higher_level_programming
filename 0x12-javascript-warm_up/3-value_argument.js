#!/usr/bin/node
const { argv } = require('node:process');
let cnt = 0;
argv.forEach((index) => {
  cnt = cnt + 1;
});
if (cnt === 2) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
