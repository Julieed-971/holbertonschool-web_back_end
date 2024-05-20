export default function getListStudentIds(array) {
  if (Array.isArray(array)) {
    const idList = array.map((item) => item.id);
    return idList;
  }
  return [];
}
