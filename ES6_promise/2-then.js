const isSuccessful = {
  status: '200',
  body: 'success',
};

export default function handleResponseFromAPI(promise) {
  console.log('Got a response from the API');
  return promise
    .then(isSuccessful)
    .catch(() => new Error());
}
