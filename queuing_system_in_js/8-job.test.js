import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  const queue = kue.createQueue();

  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs({}, queue))
      .to.throw('Jobs is not an array');
    expect(queue.testMode.jobs.length).to.equal(0);
  });

  it('should create a single job in the queue', () => {
    const singleJob = [
      {
        phoneNumber: '4151234567',
        message: 'Test single job'
      }
    ];

    createPushNotificationsJobs(singleJob, queue);

    expect(queue.testMode.jobs.length).to.equal(1);
    const job = queue.testMode.jobs[0];
    expect(job.data.phoneNumber).to.equal('4151234567');
    expect(job.data.message).to.equal('Test single job');
  });

  it('should create multiple jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    const job1 = queue.testMode.jobs[0];
    expect(job1.data.phoneNumber).to.equal('4153518780');
    expect(job1.data.message).to.equal('This is the code 1234 to verify your account');

    const job2 = queue.testMode.jobs[1];
    expect(job2.data.phoneNumber).to.equal('4153518781');
    expect(job2.data.message).to.equal('This is the code 4562 to verify your account');
  });
});
