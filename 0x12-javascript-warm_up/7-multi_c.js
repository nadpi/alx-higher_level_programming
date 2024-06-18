#!/usr/bin/node
const { argv } = require('node:process');
if (argv.length === 2 ) {
  console.log('Missing number of occurrences');
}
let i = 0;
for(i; i < argv[2]; i++) {
  console.log('C is fun');
}
