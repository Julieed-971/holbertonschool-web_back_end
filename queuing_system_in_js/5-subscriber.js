import redis from 'redis';

const subscriber = redis.createClient({
    host: '127.0.0.1',
    port: 6379
});

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
    if (message === "KILL_SERVER") {
        subscriber.unsubscribe;
        subscriber.quit();

    }
    console.log(message);
});
