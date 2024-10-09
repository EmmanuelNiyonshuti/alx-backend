#!/usr/bin/node
// Script to manage notification jobs using Kue.
// Processes jobs, checks for blacklisted numbers, and tracks progress.

import kue from 'kue';

const queue = kue.createQueue();

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done){
    job.progress(0);
    if (blacklist.includes(phoneNumber)){
     const error = new Error(`Phone number ${phoneNumber} is blacklisted`);
     console.error(`Notification job #${job.id} failed: ${error.message}`);
     return done(error);  
    }
    job.progress(50);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

// process jobs in the queue

queue.process('push_notification_code_2', 2, (job, done) => {
    const {phoneNumber, message} = job.data;
    sendNotification(phoneNumber, message, job, done);
});

queue.on('job failed', (id, err) => {
    console.log(`Notification job #${id} completed`);
});
queue.on('job complete', (id) => {
    console.log(`Notification job #${id} completed`);
});