export default function appendToEachArrayValue(array, appendString) {
  const appendedArray = [];
  for (const value of array) {
    appendedArray.push(`${appendString}${value}`);
  }

  return appendedArray;
}
