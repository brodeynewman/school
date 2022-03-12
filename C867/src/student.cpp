#include <string>
#include <array>
#include <iostream>

#include "utils.h"
#include "degree.h"
#include "student.h"

using namespace std;
using namespace util;

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

string Student::getFirstName() {
  return firstName;
}

string Student::getLastName() {
  return lastName;
}

string Student::getEmailAddress() {
  return emailAddress;
}

int Student::getAge() {
  return age;
}

array<int, 3> Student::getCourseDays() {
  return courseDays;
}

void Student::print() {
  array<int, 3> courses = this->getCourseDays();
  string degree = enumToDegreeString(this->getDegreeProgram());

  string stringAge = to_string(this->getAge());
  string courseOne = to_string(courses[0]);
  string courseTwo = to_string(courses[1]);
  string courseThree = to_string(courses[2]);

  std::string output = this->getStudentId()
    + "   First Name:   "
    + this->getFirstName()
    + "   Last Name:  "
    + this->getLastName()
    + "   Age   "
    + stringAge
    + "   daysInCourse:   "
    + "(" + courseOne + ", " + courseTwo + ", " + courseThree + ")"
    + "  Degree Program:  "
    + degree;

  cout << output;
  cout << endl;
}
