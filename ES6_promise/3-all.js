/* eslint-disable-next-line import/extensions */
import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  // Collectively resolve all promises
  return Promise.all([uploadPhoto(), createUser()])
    // Use then callback to access promises properties values
    .then(([uploadPhoto, createUser]) => {
      // Log values to the console
      console.log(`${uploadPhoto.body} ${createUser.firstName} ${createUser.lastName}`);
    })
    // In case of error, log error message
    .catch(() => new Error('Signup system offline'));
}
