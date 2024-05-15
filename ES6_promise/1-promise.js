const isSuccessful = {
  status: 200,
  body: 'Success',
};

const isNotSuccessfull = 'The fake API is not working currently';

function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) {
      resolve(isSuccessful);
    } else {
      reject(isNotSuccessfull);
    }
  });
}
export default getFullResponseFromAPI;
