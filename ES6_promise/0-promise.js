function getResponseFromAPI() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(true);
    }, 0);
  });
}
export default getResponseFromAPI;
