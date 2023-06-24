#!/usr/bin/node
const argv = process.argv;
const arglength = process.argv.length;
if (arglength < 4) {
  console.log(0);
} else {
  const array = argv.slice(2).sort((a, b) => a - b).reverse();
  console.log(array[1]);
}
