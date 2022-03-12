#include <string>
#include <array>
#include <vector>
#include "student.h"
#include "degree.h"

using namespace std;

class Roster {
  public:
    void add(string, string, string, string, int, int, int, int, DegreeProgram);
    void remove(string);
    void printAll();
    void printAverageDaysInCourse(string);
    void printInvalidEmails();
    void printByDegreeProgram(DegreeProgram);

    // destructor
    ~Roster();

    void forEach(void (*f) (Roster*, Student*));

  private:
    vector<Student*> classRosterArray;
};
