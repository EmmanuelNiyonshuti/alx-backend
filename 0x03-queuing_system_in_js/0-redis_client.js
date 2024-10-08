// connects to local redis server.

import redis from 'redis';

const client = redis.createClient();
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));


/*newer versions 3.x and above 
import { createClient } from 'redis';

const client = createClient();

client.on('error', err => console.log(`Redis client not connected to the server: ${err}`));

client.connect().then(() => {
    console.log('Redis client connected to the server');
}).catch((err) => {
    console.log(`Redis client not connected to the server: ${err}`)
});*/
