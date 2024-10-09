#!/usr/bin/node
//listens for new jobs in the queue
// When a job is added to the queue,
// the processor picks it up and executes the task using the data in the job.

import kue from 'kue';

const queue = kue.createQueue();

function sendNotification(phoneNumber, message){
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

}

queue.process('push_notification_code', (job, done) => {
    const {phoneNumber, message} = job.data; 
    sendNotification(phoneNumber, message);
    done();
});