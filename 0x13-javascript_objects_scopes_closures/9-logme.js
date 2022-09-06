#!/usr/bin/node
let b = 0;
exports.logMe = function (item) {
  console.log(`${b}: ${item}`);
  b++;
};
