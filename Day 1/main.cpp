#include <iostream>
#include <fstream>
#include <string>


int main() {

//Part two

    std::ifstream fIn;

    fIn.open("../aoc_day1.txt");

    int curr, counter = 0;
    int past1, past2, past3 = -1;

    while (fIn && fIn.peek() != EOF) {
        //reads in current
        fIn >> curr;
        //prints it out just to see what it is
        std::cout << curr << "\n";
        //making sure i only pass stuff in when each has a value
        if (past1 != -1 && past2 != -1 && past3 != -1) {
            //when the first section is more than the second section it enters loop
            if (curr + past1 + past2 - (past1 + past2 + past3) > 0) {
                //prints
                std::cout << curr + past1 + past2 << " > " << past1 + past2 + past3 << "\n";
                //adds to counter
                counter++;
            }
        }
        //updates values
        past3 = past2;
        past2 = past1;
        past1 = curr;
        //clears the read in
        fIn.clear();
    }
    //prints answer
    std::cout << counter;
    return 0;

//
// Part one
//    std::ifstream fIn;
//
//    fIn.open("../aoc_day1.txt");
//
//    int curr, counter = 0;
//    int past = -1;
//
//    while(fIn && fIn.peek() != EOF){
//        fIn >> curr;
//        std::cout << curr << "\n";
//        //if curr > past, adds to counter
//        if(past != -1){
//            if(curr - past > 0){
//                counter++;
//            }
//        }
//        past = curr;
//        fIn.clear();
//    }
//    std::cout << counter;
//    return 0;
}
