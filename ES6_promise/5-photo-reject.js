export default function uploadPhoto(filename) {
  return new Promise(() => {
    throw new Error(`${filename} cannot be processed`);
  });
}
