#!/usr/bin/node
/* A script that computes the number of tasks completed by user id */

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          ++completedTasks[task.userId];
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });

    console.log(completedTasks);
  } else {
    console.log('Error:', res.statusCode);
  }
});
