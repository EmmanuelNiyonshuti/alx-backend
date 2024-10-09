#!/usr/bin/node

import redis from 'redis';
import util from 'util';

const client = redis.createClient();

const asyncGet = util.promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`))

function setNewSchool(schoolName, value){
    client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName){
    try {
        const value = await asyncGet(schoolName);
        console.log(value);
    }catch (err){
        console.error(err);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

module.exports = redis;
