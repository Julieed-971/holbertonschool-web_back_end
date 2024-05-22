export default function cleanSet(set, startString) {
  // Return an empty string if startString is empty
  if (startString === '') {
    return '';
  }
  // Convert the Set object to an array
  const arrayFromSet = [...set];

  // Filter the array to only include elements that start with startString
  const filteredArray = arrayFromSet.filter((element) => element.startsWith(startString));

  // Remove the startString from the beginning of each element in the array
  const trimmedArray = filteredArray.map((element) => element.slice(startString.length));

  // Join the elements of the array into a string, separated by '-'
  return trimmedArray.join('-');
}
