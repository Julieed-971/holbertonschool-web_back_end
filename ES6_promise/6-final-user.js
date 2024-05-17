/* eslint-disable-next-line import/extensions */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  return new Promise((resolve, reject) => {
    Promise.allSettled([uploadPhoto(filename), signUpUser(firstName, lastName)])
      .then((results) => {
        const promiseStatuses = results.map((result) => {
          if (result.status === 'fulfilled') {
            return { status: 'fulfilled', value: result.value };
          }
          return { status: 'rejected', value: result.reason };
        });
        resolve(promiseStatuses);
      })
      .catch((error) => {
        reject(error);
      });
  });
}
