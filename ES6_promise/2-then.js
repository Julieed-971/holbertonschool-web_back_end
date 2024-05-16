const isSuccessful = {
  status: '200',
  body: 'success',
};

export default function handleResponseFromAPI(promise) {
  promise.then(isSuccessful);
  promise.catch(() => new Error());
  promise.then(console.log('Got a response from the API'));
}
