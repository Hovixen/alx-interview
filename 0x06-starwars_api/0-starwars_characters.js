#!/usr/bin/node

const request = require('request');

const [,, arg] = process.argv;

const movieId = `https://swapi.dev/api/films/${arg}/`;

request(movieId, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movie = JSON.parse(body);

  movie.characters.forEach((charUrl) => {
    request(charUrl, (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }
      const actor = JSON.parse(charBody);
      console.log(actor.name);
    });
  });
});
