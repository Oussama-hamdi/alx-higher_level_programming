#!/usr/bin/node
/* A script that writes a string to a file */

const fs = require('fs');
const filePath = process.argv[2];
const str = process.argv[3];

fs.writeFile(filePath, str, err => {
  if (err) {
    console.log(err);
  }
});
