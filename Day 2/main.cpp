#include <iostream>
#include <fstream>
#include <string>

int main() {

    std::ifstream fIn;

    fIn.open("../aoc_day2.txt");

    long long curr = 0;
    long long horiz = 0;
    long long depth = 0;
    long long aim = 0;
    std::string action;

    while (fIn && fIn.peek() != EOF) {
        //reads in current
        fIn >> action >> curr;

        if(action.compare("forward") == 0){
            std::cout << "Horiz: " << horiz << " + " << curr << "\n";
            horiz += curr;
            depth += aim * curr;
        } else if (action.compare("down") == 0){
            std::cout << "Depth: " << depth << " + " << curr << "\n";
            aim += curr;
        } else {
            std::cout << "Depth: " << depth << " - " << curr << "\n";
            aim -= curr;
        }
        fIn.clear();
        std::cout << "--------" << "\n";
        std::cout << "Horiz: " << horiz << "\n";
        std::cout << "Depth: " << depth << "\n";
        std::cout << "--------" << "\n";
    }

    std::cout << horiz*depth;


//
//    //Part 1
//    std::ifstream fIn;
//
//    fIn.open("../aoc_day2.txt");
//
//    long curr = 0;
//    long horiz = 0;
//    long depth = 0;
//    std::string action;
//
//    while (fIn && fIn.peek() != EOF) {
//        //reads in current
//        fIn >> action >> curr;
//
//        if(action.compare("forward") == 0){
//            std::cout << "Horiz: " << horiz << " + " << curr << "\n";
//            horiz += curr;
//        } else if (action.compare("down") == 0){
//            std::cout << "Depth: " << depth << " + " << curr << "\n";
//            depth += curr;
//        } else {
//            std::cout << "Depth: " << depth << " - " << curr << "\n";
//            depth -= curr;
//        }
//        fIn.clear();
//        std::cout << "--------" << "\n";
//        std::cout << "Horiz: " << horiz << "\n";
//        std::cout << "Depth: " << depth << "\n";
//        std::cout << "--------" << "\n";
//    }
//
//    std::cout << horiz*depth;

    return 0;

}
