#include <string>
#include <array>
#include <vector>
#include <iostream>

#include "utils.h"
#include "roster.h"
#include "degree.h"

using namespace std;
using namespace util;

void Roster::printAll() {
  cout << "HELLO MATE";
};

void Roster::add(string studentId, string firstName, string lastName, string email, int age, int courseOne, int courseTwo, int courseThree, DegreeProgram degreeProgram) {
  Student student;

  array<int, 3> courses = {courseOne, courseTwo, courseThree};

  student.setStudentId(studentId);
  student.setFirstName(firstName);
  student.setLastName(lastName);
  student.setEmailAddress(email);
  student.setAge(age);
  student.setCourseDays(courses);
  student.setDegreeProgram(degreeProgram);

  classRosterArray.push_back(student);
}

void Roster::printInvalidEmails() {
  for(std::vector<Student*>::size_type i = 0; i != classRosterArray.size(); i++) {
    array<int, 3> courses = classRosterArray[i].getCourseDays();
    string degree = enumToDegreeString(classRosterArray[i].getDegreeProgram());

    string stringAge = to_string(classRosterArray[i].getAge());
    string courseOne = to_string(courses[0]);
    string courseTwo = to_string(courses[1]);
    string courseThree = to_string(courses[2]);

    std::string output = classRosterArray[i].getStudentId()
      + " First Name: "
      + classRosterArray[i].getFirstName()
      + " Last Name: "
      + classRosterArray[i].getLastName()
      + " Age "
      + stringAge
      + " Days In Course: "
      + "(" + courseOne + ", " + courseTwo + ", " + courseThree + ")"
      + " Degree Program: "
      + degree;

    cout << output;
  }
}
