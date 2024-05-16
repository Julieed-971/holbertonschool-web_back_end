const isSuccessful = {
  status: 200,
  body: 'Success',
};

const isNotSuccessfull = ('The fake API is not working currently');

function getFullResponseFromAPI(success) {
  return new Promise((resolve) => {
    if (success === true) {
      resolve(isSuccessful);
    } else {
      throw new Error(isNotSuccessfull);
    }
  });
}
export default getFullResponseFromAPI;
