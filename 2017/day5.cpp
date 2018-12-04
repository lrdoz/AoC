#include <iostream>
#include <string>
#include <iterator>
#include <fstream>
#include <sstream>
#include <vector>

auto get_data(str puzzle){
  vector <int> offsets;
  ifstream file(puzzle);
  copy(istream_iterator<int>(file), istream_iterator<int>(), back_inserter(puzzles));
  return offsets;
}
auto trampoline(vector <int> offsets){
  int i = 0;
  int jump = 0;
  while (i < offsets.size()){
    int elem =  offsets[i];
    jump++;
    i += elem;
    offsets[i]++;
  }
  return jump;
}
```

int main(){
  string puzzles = '/inputs/input5.txt'
  vector <int> offsets = get_data('/inputs/input5.txt')
  cout << trampoline(offsets);
}