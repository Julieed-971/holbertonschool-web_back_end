const isSuccessful = {
  status: '200',
  body: 'success',
};

export default function handleResponseFromAPI(promise) {
  return promise
    .then(isSuccessful)
    .catch(() => new Error())
    .then(console.log('Got a response from the API'));
}
