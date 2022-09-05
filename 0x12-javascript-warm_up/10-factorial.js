#!/usr/bin/node
function factorial (number) {
  if (isNaN(number) || number === 1) return 1;
  return number * factorial(number - 1);
}

console.log(factorial(Math.floor(Number(process.argv[2]))));
