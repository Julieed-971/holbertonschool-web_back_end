export default function getStudentIdsSum(studentsList) {
  const idSum = studentsList.reduce((accumulator, student) => accumulator + student.id, 0);
  return idSum;
}
