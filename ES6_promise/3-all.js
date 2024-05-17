/* eslint-disable-next-line import/extensions */
import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const utils = [uploadPhoto(), createUser()];
  // Collectively resolve all promises
  return Promise.all(utils)
    // Log message to the console
    .then(([photoData, userData]) => {
      const { body } = photoData;
      const { firstName, lastName } = userData;
      console.log(body, firstName, lastName);
    })
    // In case of error, log error message
    .catch(() => new Error('Signup system offline'));
}
