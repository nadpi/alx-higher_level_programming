#!/usr/bin/node
const { argv } = require('node:process');
let cnt = 0;
argv.forEach((index) => {
  cnt = cnt + 1;
});
if (cnt === 2) {
  console.log('No argument');
} else {
  let i = 0;
  for (i = 2; i < cnt; i++) {
    console.log(argv[i]);
  }
}
