#include "roster.h"
#include "degree.h"
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

// we are heavily asserting on this format...
const string studentData[] = {
  "A1,John,Smith,John1989@gm ail.com,20,30,35,40,SECURITY",
  "A2,Suzan,Erickson,Erickson_1990@gmailcom,19,50,30,40,NETWORK",
  "A3,Jack,Napoli,The_lawyer99yahoo.com,19,20,40,33,SOFTWARE",
  "A4,Erin,Black,Erin.black@comcast.net,22,50,58,40,SECURITY",
  "A5,Brodey,Newman,bnewm57@wgu.edu,26,21,25,50,SOFTWARE",
};

const char separator = ',';

void printClassDetails() {
  string hr("-----------\n");
  string details("Course Title: C867 \nProgramming Language: C++ \nStudent ID: 009462905 \nName: Brodey Newman\n");

  cout << hr;
  cout << details;
  cout << hr;
}

DegreeProgram degreeStringToEnum(string degreeProgram) {
  if (degreeProgram == "SECURITY") {
    return SECURITY;
  } else if (degreeProgram == "NETWORK") {
    return NETWORK;
  } else if (degreeProgram == "SOFTWARE") {
    return SOFTWARE;
  } else {
    return NOTAPPLICABLE;
  }
}

void buildRoster(Roster* roster) {
  // Hardcoding 5 here since the program requirements indicate a static array length of 5.
  for (int i = 0; i < 5; i++) {
    string studentDetails = studentData[i];

    vector<string> result;
    stringstream data(studentDetails);
    string line;

    while(getline(data, line, separator)) {
      result.push_back(line);
    }

    string studentId = result[0];
    string firstName = result[1];
    string lastName = result[2];
    string email = result[3];
    int age = stoi(result[4]);
    int courseOne = stoi(result[5]);
    int courseTwo = stoi(result[6]);
    int courseThree = stoi(result[7]);
    string program = result[8];
    DegreeProgram degreeProgram = degreeStringToEnum(program);

    roster->add(studentId, firstName, lastName, email, age, courseOne, courseTwo, courseThree, degreeProgram);
  }
}

int main() {
  printClassDetails();

  Roster classRoster;
  buildRoster(&classRoster);

  // classRoster.printAll();
  classRoster.printInvalidEmails();
  
  return 0;
}