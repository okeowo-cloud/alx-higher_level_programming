#!/usr/bin/node
const arg1 = process.argv[2] === 'undefined' ? 'undefined' : process.argv[2];
const arg2 = process.argv[3] === 'undefined' ? 'undefined' : process.argv[3];
console.log(arg1 + ' is ' + arg2);
