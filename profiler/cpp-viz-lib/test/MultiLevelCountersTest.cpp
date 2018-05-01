#include "MultiLevelCounters.hpp"

#include <iostream>


main(){
  

  std::vector <std::string> level0 = {"Grp0", "Grp1", "Grp2"};
  std::vector <std::string> level1 = {"Tile4x4", "Tile8x8", "Tile16x16"};

  MultiLevelCounters<uint32_t> cnt("Tiling", level0, level1);

  cnt.setCounter(0,1,100);

  std::cout << cnt.toJson() << std::endl;
}
