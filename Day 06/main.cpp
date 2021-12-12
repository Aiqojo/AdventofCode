#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {

    //this day made me hate longs

    std::ifstream fIn;
    fIn.open("../aoc_day6.txt");

    char comma;
    int curr;

    //using long long for everything cause numbers get REAL big
    std::vector<long long>list(9);

    //reading in
    while(fIn && fIn.peek() != EOF){
        fIn >> curr;
        list[curr] += 1;
        fIn >> comma;
    }

    long long temp;
    int day = 80;

    for(int j = 0; j < 2; j++) {
        std::vector<long long>listt = list;
        for (int i = 0; i < day; i++) {
            //swapping days here
            //0 go to 6 and 8
            //others move down by one
            temp = listt[0];
            listt[0] = listt[1];
            listt[1] = listt[2];
            listt[2] = listt[3];
            listt[3] = listt[4];
            listt[4] = listt[5];
            listt[5] = listt[6];
            listt[6] = listt[7] + temp;
            listt[7] = listt[8];
            listt[8] = temp;
        }

        long long s = 0;
        unsigned long long t = 0;

        for (int i = 0; i < 9; i++) {
            s += listt[i];
        }

        //printing out and resetting
        std::cout << "DAY " << day << ": " << s << "\n";
        s = 0;
        t = 0;
        temp = 0;
        day = 256;
    }

    return 0;
}