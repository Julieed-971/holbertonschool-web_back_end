export default function updateStudentGradeByCity(students, city, newGrades) {
  const studentByCity = students.filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find((gradeInfo) => gradeInfo.studentId === student.id);
      if (gradeObj) {
        // eslint-disable-next-line no-param-reassign
        student.grade = gradeObj.grade;
      } else {
        // eslint-disable-next-line no-param-reassign
        student.grade = 'N/A';
      }
      return student;
    });
  return studentByCity;
}
