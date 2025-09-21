import kue from 'kue';
const queue = kue.createQueue();

const blacklistedPhoneNumber = [
    '4153518780',
    '4153518781',
]

const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100);
    if (blacklistedPhoneNumber.includes(phoneNumber)) {
        return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
        const {phoneNumber, message} = job.data;
        sendNotification(phoneNumber, message, job, done);
    });
