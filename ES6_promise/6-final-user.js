import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  return Promise.allSettled([uploadPhoto(filename), signUpUser(firstName, lastName)])
    .then((results) => results.map((result) => {
      const promiseStatus = {
        status: result.status,
      };
      if (result.status === 'fulfilled') {
        promiseStatus.value = result.value;
      } else {
        promiseStatus.value = result.reason;
      }
      return promiseStatus;
    }));
}
