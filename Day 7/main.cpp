#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

//hardcore bruteforce
//may take a bit to run, was very fast on my 5900x tho
int main() {

    std::ifstream fIn;
    fIn.open("../aoc_day7.txt");

    char comma;
    int curr;
    std::vector<int> list;

    //reading in
    while(fIn && fIn.peek() != EOF){
        fIn >> curr;
        list.push_back(curr);
        fIn >> comma;
    }

    //part 1
    //finding median in list and getting values from that
    int part1 = 0;
    std::sort (list.begin(), list.end());
    int len = list[list.size()/2];
    for(int i : list){
        part1 += abs(len - i);
    }
    std::cout << "Part 1: " << part1 << "\n";

    long long sum = 0;
    long long fuel = 0;

    for(int i : list){
        sum += i;
    }

    int max = 0;
    for(int i : list){
        if(i > max){
            max = i;
        }
    }
    //std::cout << "MAX: " << max << "\n";

    long long bestFuel = -1;
    long long bestAvg = 0;

    //cycles through every horizontal location from 0 to the max position (1940)
    for(int i = 0; i < max; i++){
        //for every submarine, get its distance
        for(int h : list){
            int k = 0;
            //everytime this loops, k gets closer to actual distance traveled
            while(abs(h - i) > k){
                //fuel consumed increases by one each time, so k doubles up as fuel consumed for each move
                k++;
                fuel+= k;
            }
        }
        //std::cout << fuel << " i: " << i << "\n";

        //if first fuel value, its best one
        if(bestFuel == -1){
            bestFuel = fuel;
            //if fuel is lower than best fuel, replace it
        }else if(fuel != -1 && bestFuel > fuel){
            bestFuel = fuel;
            bestAvg = i;
        }
        //reset
        fuel = 0;
    }

    std::cout << "----PART 2----" << "\n";
    std::cout << "BEST FUEL: " << bestFuel << "\n";
    std::cout << "BEST AVG: " << bestAvg << "\n";

    return 0;
}
