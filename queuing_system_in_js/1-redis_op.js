import redis from 'redis';

const client = redis.createClient({
  host: '127.0.0.1',
  port: 6379
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, redis.print);
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, reply) => {
        if (err) {
            console.log(err);
            return;
        }
        console.log(reply);
    });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
