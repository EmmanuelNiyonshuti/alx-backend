#!/usr/bin/node

import redis from 'redis';
const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))

function createHash(){
    const schoolData = {
        Portland:50,
        Seattle:80,
        'New York':20,
        Bogota:20,
        Cali:40,
        Paris:2
    }
    for (const [k, v] of Object.entries(schoolData)){ 
        client.hset('HolbertonSchools', k, v, redis.print);
    }
}

function displayHash(){
    client.hgetall('HolbertonSchools', (err, res) => {
        if (err){
            console.error(err);
        }else{
            console.log(res);
        }
    });
}

createHash();
displayHash();

