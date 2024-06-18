#!/usr/bin/node
const { argv } = require('node:process');
let cnt = 0;
argv.forEach((val, index) => {
  cnt = cnt + 1;
});
if (cnt === 2) {
  console.log('No argument');
} else if (cnt === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
