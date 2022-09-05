#!/usr/bin/node
function add (a, b) {
  console.log(isNaN(Number(a)) || isNaN(Number(b)) ? 'NaN' : Number(a) + Number(b));
}

add(process.argv[2], process.argv[3]);
