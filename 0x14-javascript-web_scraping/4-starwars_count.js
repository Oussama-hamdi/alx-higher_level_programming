#!/usr/bin/node
/* A script that prints the number of movies
 * where the character “Wedge Antilles” is present */

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const movieData = JSON.parse(body).results;
    const count = movieData.reduce((total, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? ++total
        : total;
    }, 0);
    console.log(count);
  } else {
    console.log('Error:', res.statusCode);
  }
});
