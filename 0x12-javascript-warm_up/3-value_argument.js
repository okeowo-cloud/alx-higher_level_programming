#!/usr/bin/node
const argv = process.argv;
const argc = argv.length;
console.log(argc === 2 ? 'No argument' : argv[2]);
