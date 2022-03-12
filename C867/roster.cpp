#include <string>
#include <array>
#include <vector>
#include <iostream>
#include <regex>
#include <stdexcept>

#include "roster.h"
#include "degree.h"

using namespace std;

const regex pattern ("(\\w+)(\\.|_)?(\\w*)@(\\w+)(\\.(\\w+))+");

bool checkValidEmail(string email) {
  return regex_match(email, pattern);
}

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

void Roster::printAll() {
  for(std::vector<Student*>::size_type i = 0; i != classRosterArray.size(); i++) {
    // loop through each student & print the details
    classRosterArray[i].print();
  }
}

void Roster::printInvalidEmails() {
  vector<string> invalidEmails;

  for(std::vector<Student*>::size_type i = 0; i != classRosterArray.size(); i++) {
    string email = classRosterArray[i].getEmailAddress();

    if (!checkValidEmail(email)) {
      invalidEmails.push_back(email);
    }
  }

  for(std::vector<string>::size_type i = 0; i != invalidEmails.size(); i++) {
    string invalidEmail = invalidEmails[i];

    cout << "Invalid email: ";
    cout << invalidEmail;
    cout << endl;
  }
}

void Roster::printAverageDaysInCourse(string studentId) {
  Student student;
  bool found = false;

  for(std::vector<Student*>::size_type i = 0; i != classRosterArray.size(); i++) {
    if (classRosterArray[i].getStudentId() == studentId) {
      student = classRosterArray[i];
      found = true;
      break;
    }
  }

  // throw exception if user does not exist.
  if (found == false) {
    throw invalid_argument("Student with id: " + studentId + " does not exist");
  } else {
    // at this point, we can print average course length.

    array<int, 3> classes = student.getCourseDays();
    
    int c1 = classes[0];
    int c2 = classes[1];
    int c3 = classes[2];

    int avg = (c1 + c2 + c3) / 3;

    cout << "Average days in course for student id " + studentId + ": ";
    cout << to_string(avg);
    cout << endl;
  }
}

void Roster::forEach(void (*callback)(Roster*, Student)){
  for(std::vector<Student*>::size_type i = 0; i != classRosterArray.size(); i++) {
    callback(this, classRosterArray[i]);
  }
}

void Roster::remove(string studentId) {
  Student student;
  bool found = false;
  int foundInd;

  for(std::vector<Student*>::size_type i = 0; i != classRosterArray.size(); i++) {
    if (classRosterArray[i].getStudentId() == studentId) {
      student = classRosterArray[i];
      found = true;
      foundInd = i;
      break;
    }
  }

  if (found == false) {
    throw invalid_argument("Student with id: " + studentId + " does not exist");
  } else {
    // remove our student from the vector

    classRosterArray.erase(classRosterArray.begin() + foundInd);

    cout << "Student with id: " + studentId + " successfully removed";
    cout << endl;
  }
}
