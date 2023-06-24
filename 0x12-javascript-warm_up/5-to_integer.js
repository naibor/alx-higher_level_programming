#!/usr/bin/node
const convertedInteger = parseInt(process.argv[2]);
if (convertedInteger) {
  console.log('My number: ' + convertedInteger);
} else {
  console.log('Not a number');
}
