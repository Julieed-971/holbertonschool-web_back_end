export default function cleanSet(set, startString) {
  if (!startString) {
    return '';
  }

  const result = [];
  for (const element of set) {
    if (element.startsWith(startString)) {
      result.push(element.slice(startString.length));
    }
  }
  return result.join('-');
}
