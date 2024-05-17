/* eslint-disable-next-line import/extensions */
import { uploadPhoto, createUser } from './utils';

export default async function handleProfileSignup() {
  try {
    const [photoData, userData] = await Promise.all([uploadPhoto(), createUser()]);
    console.log(photoData.body, userData.firstName, userData.lastName);
  } catch (error) {
    throw new Error('Signup system offline');
  }
}
  // // Collectively resolve all promises
  // return Promise.all([uploadPhoto(), createUser()])
  //   // Use then callback to access promises properties values
  //   .then(([photoData, userData]) => {
  //     // Log values to the console
  //   })
  //   // In case of error, log error message
  //   .catch(() => new Error('Signup system offline'));
