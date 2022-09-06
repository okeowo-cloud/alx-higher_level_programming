#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const item of list) {
    if (item === searchElement) occurences++;
  }
  return occurences;
};
