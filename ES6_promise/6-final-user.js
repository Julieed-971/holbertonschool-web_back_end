/* eslint-disable-next-line import/extensions */
import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  return Promise.any([uploadPhoto(filename), signUpUser(firstName, lastName)]);
}
