#!/usr/bin/node
// creates a job queue

import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: '123-456-7890',
    message: 'Hello, this is a notification!',  
}

const job = queue.create('push_notification_code', jobData)
    .save((err) => {
        if (!err){
            console.log(`Notification job created: ${job.id}`);
        }
    });

job.on('complete', () => {
    console.log('Notification job completed');
}).on('failed', () => {
    console.log('Notification job failled');
})
