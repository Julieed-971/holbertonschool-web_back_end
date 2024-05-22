export default function cleanSet(set, startString) {
  // Checks if startsString is an empty string
  if (!startString) return '';

  // Convert set to array
  const arrayFromSet = [...set];

  // Filter array with element that starts with startString
  const filteredArray = arrayFromSet.filter((element) => element.startsWith(startString));

  // Trim element of the array of startString length
  const trimmedArray = filteredArray.map((element) => element.slice(startString.length));

  // Return converted array to string
  return trimmedArray.join('-');
}
