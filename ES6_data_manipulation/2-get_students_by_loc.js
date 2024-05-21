export default function getStudentsByLocation(studentsList, city) {
  const studentsInCity = studentsList.filter((student) => student.location === city);
  return studentsInCity;
}
