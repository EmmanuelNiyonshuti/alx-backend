#!/usr/bin/node
import kue from 'kue';


const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue){
    if (!Array.isArray(jobs)){
        throw Error('Jobs is not an array');
    }
    for (const j of jobs){
        const job = queue.create('push_notification_code_3', j)
            .save((err) => {
                if (!err){ 
                    console.log(`Notification job created: ${job.id}`);
                }
            });
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        }).on('failed', (error) => {
            console.log(`Notification job ${job.id} failed: ${error}`);
        }).on('progress', (progress) => {
            console.log(`Notification job ${job.id} ${progress} complete`);
        })
    }
 }

export default createPushNotificationsJobs;
