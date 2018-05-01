#ifndef __UTILITIES_H__
#define __UTILITIES_H__

#include <string>

std::string quoted(std::string str){
  return ("\"" + str + "\"");
}

std::string indent(uint32_t level){
  std::string retString (level * 2, ' ');
  return retString;
}

#endif
