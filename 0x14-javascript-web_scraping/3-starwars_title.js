#!/usr/bin/node
/* A script that prints the title of a Star Wars movie where
 * the episode number matches a given integer */

const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  } else {
    console.log('Error:', res.statusCode);
  }
});
