export default function updateStudentGradeByCity(students, city, newGrades) {
  // Look for student object matching the city in the students list
  const studentByCity = students.filter((student) => student.location === city)
    // For each student in the filtered list
    .map((student) => {
      // Find the corresponding grade object in the newGrades array
      const gradeObj = newGrades.find((gradeInfo) => gradeInfo.studentId === student.id);
      // If a matching grade object is found
      if (gradeObj) {
        // Update the student's grade with the new grade
        // eslint-disable-next-line no-param-reassign
        student.grade = gradeObj.grade;
      } else {
        // If no matching grade object is found, set the student's grade to 'N/A'
        // eslint-disable-next-line no-param-reassign
        student.grade = 'N/A';
      }
      // Return the updated student object
      return student;
    });
  // Return the array of updated student objects
  return studentByCity;
}
