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

        //this stuff is really straight forward but for the sake of commenting:
        //if fIn reads action in as "forward"
        if(action.compare("forward") == 0){
            //std::cout << "Horiz: " << horiz << " + " << curr << "\n";
            //add curr to horizontal value
            horiz += curr;
            //add aim * curr to depth
            depth += aim * curr;
        } else if (action.compare("down") == 0){
            //std::cout << "Depth: " << depth << " + " << curr << "\n";
            //if action is "down" add curr to aim
            aim += curr;
        } else {
            //std::cout << "Depth: " << depth << " - " << curr << "\n";
            //if action is "up" subtract curr to aim
            aim -= curr;
        }
        //clearing fIn
        fIn.clear();
        //printing stuff
        std::cout << "--------" << "\n";
        std::cout << "Horiz: " << horiz << "\n";
        std::cout << "Depth: " << depth << "\n";
        std::cout << "--------" << "\n";
    }
    //result
    std::cout << horiz*depth;





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
