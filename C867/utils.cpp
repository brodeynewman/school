#include "utils.h"

DegreeProgram util::degreeStringToEnum(string program) {
  if (program == "SECURITY") {
    return SECURITY;
  } else if (program == "NETWORK") {
    return NETWORK;
  } else if (program == "SOFTWARE") {
    return SOFTWARE;
  } else {
    return NOTAPPLICABLE;
  }
}

string util::enumToDegreeString(DegreeProgram program) {
  if (program == SECURITY) {
    return "SECURITY";
  } else if (program == NETWORK) {
    return "NETWORK";
  } else if (program == SOFTWARE) {
    return "SOFTWARE";
  } else {
    return "NOTAPPLICABLE";
  }
}