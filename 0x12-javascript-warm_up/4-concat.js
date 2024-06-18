#!/usr/bin/node
const { argv } = require('node:process');
let cnt = 0;
argv.forEach((index) => {
  cnt = cnt + 1;
});
if (cnt === 2) {
  console.log('undefined is undefined');
} else if (cnt === 3) {
  console.log(argv[2] + ' is undefined');
} else {
  console.log(argv[2] + ' is ' + argv[3]);
}
