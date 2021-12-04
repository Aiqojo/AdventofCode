#include <iostream>
#include <fstream>
#include <string>
#include <math.h>
#include <vector>

int main() {

    std::ifstream fIn;

    fIn.open("../aoc_day3.txt");

    std::vector<long long> list;
    long long curr = 0;

    while(fIn && fIn.peek() != EOF){
        fIn >> curr;
        list.push_back(curr);
        fIn.clear();
    }

    long long moving = 1;
    int onecount = 0;
    long long final = 0;
    std::vector<long long> safelist;
    std::vector<long long> lastKeys;

    for(int i = 0; i < 12; i++){
        for(int j = 0; j < list.size(); j++){
            if((list[j] / moving) % 10 == 1){
                onecount++;
            }
            std::cout << list[j] << " " << (list[j] / moving) % 10 << " Onecount: " << onecount << "\n";
        }
        std::cout << "ONECOUNT: " << onecount << " | LIST SIZE: " << list.size() << "\n";
        std::cout << "Percentage: " << (double)onecount / (double)list.size() << "\n";
        if((double)onecount / (double)list.size() >= .5){
            final += moving;
            for(int k = 0; k < list.size(); k++){
                if((list[k] / moving) % 10 == 1){
                    safelist.push_back(list[k]);
                    //std::cout << "Adding: " << list[k] << " for moving: " << moving << "\n";
                }else{
                    //std::cout << "Didn't add: " << list[k] << " for moving: " << moving << "\n";
                }
            }
            std::cout << "FINAL: " << final << " (+" << moving << ")" << "\n";
        }else{

            for(int k = 0; k < list.size(); k++){
                if((list[k] / moving) % 10 == 0){
                    safelist.push_back(list[k]);
                }
            }
            std::cout << "FINAL: " << final << " (+0)" << "\n";
        }
        moving *= 10;
        list.clear();
        list = safelist;
        safelist.clear();
        onecount = 0;
        lastKeys.push_back(list[0]);
        std::cout << "------------------------------------------" << "\n";
    }

    for(int i = 0; i < lastKeys.size(); i++){
        std::cout << lastKeys[i] << "\n";
    }
    std::cout << list[0] << " " << list.size() << "\n";

//2239
//690 - 178

//1161
//3621


    //oxygen number: 111011111110


//
//    long long curr = 0;
//    long long one = 0;
//    long long two = 0;
//    long long three = 0;
//    long long four = 0;
//    long long five = 0;
//    long long six = 0;
//    long long seven = 0;
//    long long eight = 0;
//    long long nine = 0;
//    long long ten = 0;
//    long long eleven = 0;
//    long long twelve = 0;
//
//    int counter = 0;
//    long long test;
//
//    while (fIn && fIn.peek() != EOF) {
//        //reads in current
//        fIn >> curr;
//
//        std::cout << curr << "\n";
//
//
//        if(curr % 10 == 1){
//            std::cout << " in one" << one << "\n";
//            one++;
//            std::cout << " in one" << one << "\n";
//        }
//        test = curr % 100;
//        if(curr / 10 % 10 == 1){
//            std::cout << " in two" << two << "\n";
//            two++;
//            std::cout << " in two" << two << "\n";
//        }
//        if(curr / 100 % 10 == 1){
//            std::cout << " in three" << three << "\n";
//            three++;
//            std::cout << " in three" << three << "\n";
//        }
//        if(curr / 1000 % 10 == 1){
//            four++;
//        }
//        if(curr / 10000 % 10 == 1){
//            five++;
//        }
//        if(curr / 100000 % 10 == 1){
//            std::cout << " in six" << six << "\n";
//            six++;
//            std::cout << " in six" << six << "\n";
//        }
//        if(curr / 1000000 % 10 == 1){
//            seven++;
//        }
//        if(curr / 10000000 % 10 == 1){
//            eight++;
//        }
//        if(curr / 100000000 % 10 == 1){
//            nine++;
//        }
//        if(curr / 1000000000 % 10 == 1){
//            ten++;
//        }
//        if(curr / 10000000000 % 10 == 1){
//            eleven++;
//        }
//        if(curr / 100000000000 % 10 == 1){
//            std::cout << " in twelve" << twelve << "\n";
//            twelve++;
//            std::cout << " in twelve" << twelve << "\n";
//        }
//
//
//
//        fIn.clear();
//
//    }
//
//    std::cout << one << "\n";
//    std::cout << two << "\n";
//    std::cout << three << "\n";
//    std::cout << four << "\n";
//    std::cout << five << "\n";
//    std::cout << six << "\n";
//    std::cout << seven << "\n";
//    std::cout << eight << "\n";
//    std::cout << nine << "\n";
//    std::cout << ten << "\n";
//    std::cout << eleven << "\n";
//    std::cout << twelve << "\n";
//
//
//    //result
//    std::cout << counter;

    return 0;

}