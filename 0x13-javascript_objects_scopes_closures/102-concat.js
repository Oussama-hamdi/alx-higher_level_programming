#!/usr/bin/node

const fs = require('fs');

const [f1, f2, destinationFile] = process.argv.slice(2);

const fileData1 = fs.readFileSync(f1, 'utf-8');
const fileData2 = fs.readFileSync(f2, 'utf-8');

fs.writeFileSync(destinationFile, `${fileData1}${fileData2}`);
