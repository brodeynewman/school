#include <string>
#include <array>
#include <iostream>

using namespace std;

#include "degree.h"
#include "student.h"

void Student::setStudentId(string sId) {
  studentId = sId;
}

void Student::setFirstName(string fName) {
  firstName = fName;
}

void Student::setLastName(string lName) {
  lastName = lName;
}

void Student::setEmailAddress(string email) {
  emailAddress = email;
}

void Student::setAge(int studentAge) {
  age = studentAge;
}

void Student::setCourseDays(array<int, 3> courseArray) {
  courseDays = courseArray;
}

void Student::setDegreeProgram(DegreeProgram program) {
  degreeProgram = program;
}

DegreeProgram Student::getDegreeProgram() {
  return degreeProgram;
}

string Student::getStudentId() {
  return studentId;
}
