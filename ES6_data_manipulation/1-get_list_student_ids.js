export default function getListStudentIds(array) {
  if (Array.isArray(array)) {
    const idList = array.map((student) => student.id);
    return idList;
  }
  return [];
}
