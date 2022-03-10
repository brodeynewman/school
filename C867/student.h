#include <string>
#include <array>
#include "degree.h"

using namespace std;

class Student {
  public:
    string getStudentId();
    string getFirstName();
    string getLastName();
    string getEmailAddress();
    int getAge();
    array<int, 3> getCourseDays();
    DegreeProgram getDegreeProgram();

    void setStudentId(string);
    void setFirstName(string);
    void setLastName(string);
    void setEmailAddress(string);
    void setAge(int);
    void setCourseDays(array<int, 3>);
    void setDegreeProgram(DegreeProgram);

  private:
    string studentId;
    string lastName;
    string firstName;
    string emailAddress;
    int age;
    array<int, 3> courseDays;
    DegreeProgram degreeProgram;
};
