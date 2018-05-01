#ifndef __MULTILEVELPERFVIZ_HPP__ 
#define __MULTILEVELPERFVIZ_HPP__ 

#include <vector>
#include <string>
#include <cassert>

#include "utilities.hpp"

/// Creates 2 level counters which are used for displaying 
/// visualization using multilevel bar graphs. Eg. First 
/// level could be different groups of a model and 
/// second level being the different tile sizes
template <typename T>
class MultiLevelCounters{

public:
  MultiLevelCounters (std::string name,
                    std::vector <std::string> level0Names, 
                    std::vector <std::string> level1Names):
      data_(),
      level0Names_(level0Names),
      level1Names_(level1Names),
      name_(name){

        data_.resize(level0Names.size());
        for (uint32_t i = 0; i < level0Names_.size(); i++){
          data_[i].resize (level1Names.size());
        }
  }
    
  // Set a counter directly
  void setCounter (uint32_t level0, uint32_t level1, T count){
    assert (level0 < level0Names_.size());
    assert (level1 < level1Names_.size());

    data_[level0][level1] = count;
  } 

  // Increment a counter
  void setCounter (uint32_t level0, uint32_t level1){
    assert (level0 < level0Names_.size());
    assert (level1 < level1Names_.size());

    data_[level0][level1] += 1;
  } 

  // Convert the counter to JSON structure
  std::string toJson (){
    std::string retString = indent(1);
    retString += quoted(name_) + ":\n";
    retString += indent(2) + "{\n";
    
    // Add Level 0 names
    retString += indent(3);
    retString += quoted("level0Names") +": [";
    for (auto& x: level0Names_){
      retString += (quoted(x) + ",");
    }
    retString.pop_back(); // Detele last delimiter
    retString += "],\n";

    // Add Level 1 names
    retString += indent(3);
    retString += quoted("level1Names") +": [";
    for (auto& x: level1Names_){
      retString += (quoted(x) + ",");
    }
    retString.pop_back(); // Detele last delimiter
    retString += "],\n";

    // Add Data
    retString += indent(3);
    retString += quoted("data") +": [";
    for (uint32_t i = 0; i < level0Names_.size(); i++){
      for (uint32_t j = 0; j < level0Names_.size(); j++){
        retString += (quoted(std::to_string(data_[i][j])) + ",");
      }
    }
    retString.pop_back(); // Detele last delimiter
    retString += "]\n";
    
    retString += indent(2) + "}";

    return retString;
  }


private:
  std::vector< std::vector<T> > data_; // Raw 2D data
  std::vector< std::string >    level0Names_; // Level0 titles
  std::vector< std::string >    level1Names_; // Level1 titles
  std::string                   name_;        // Counter Name
};


#endif
