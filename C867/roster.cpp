#include <string>
#include <array>
#include <vector>
#include <iostream>

#include "roster.h"
#include "degree.h"

using namespace std;

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
    // loop through each student & print the details
    classRosterArray[i].print();
  }
}
