#!/usr/bin/node
const num = process.argv[2];
if (!parseInt(num)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < num; x++) {
    console.log('X'.repeat(num));
  }
}
