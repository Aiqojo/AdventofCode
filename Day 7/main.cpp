#include <iostream>
#include <fstream>
#include <string>
#include <vector>

//will clean later, this only solves part 2
int main() {

    std::ifstream fIn;
    fIn.open("../aoc_day7.txt");

    char comma;
    int curr;
    int mid = 472;

    //using long long for everything cause numbers get REAL big
    std::vector<int> list;

    //reading in
    while(fIn && fIn.peek() != EOF){
        fIn >> curr;
        list.push_back(curr);
        fIn >> comma;
    }

    long long sum = 0;
    long long fuel = 0;
    long long avg = 0;

    for(int i = 0; i < list.size(); i++){
        sum += list[i];
    }

    int max = 0;
    for(int i = 0; i < list.size(); i++){
        if(list[i] > max){
            max = list[i];
        }
    }

    std::cout << "MAX: " << max << "\n";

    long long bestFuel = -1;
    long long bestAvg = 0;

    for(int i = 0; i < 1940; i++){
        for(int h = 0; h < list.size(); h++){
            int k = 0;
            if(list[h] > i){
                while(k < list[h] - i){
                    k++;
                    fuel += k;
                }
                //fuel += list[h] - i;
            }else{
                while(k < i - list[h]){
                    k++;
                    fuel += k;
                }
                //fuel += i - list[h];
            }
        }
        std::cout << fuel << " i: " << i << "\n";

        if(bestFuel == -1){
            bestFuel = fuel;
        }else if(fuel != -1 && bestFuel > fuel){
            bestFuel = fuel;
            bestAvg = i;
        }
        fuel = 0;
    }

//    for(int h = 0; h < list.size(); h++){
//        if(list[i] > h){
//            fuel += list[h] - i;
//        }else{
//            fuel += i - list[h];
//        }
//    }


    std::cout << bestFuel;
    std::cout << "BEST AVG: " << bestAvg << "\n";

    //std::cout << sum/list.size() << "\n";

    return 0;
}
