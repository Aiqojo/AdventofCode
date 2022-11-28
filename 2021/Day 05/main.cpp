#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main() {

    std::ifstream fIn;
    fIn.open("../aoc_day5.txt");

    std::vector<std::vector<int>> list(1000, std::vector<int>(1000));

    int x1, x2, y1, y2;
    std::string etc;
    char comma;

    while(fIn && fIn.peek() != EOF) {

        fIn >> x1;
        //std::cout << x1 << " ";
        fIn >> comma;
        //std::cout << comma << "\n";;
        fIn >> y1;
        //std::cout << y1 << " ";;

        fIn >> etc;
        fIn >> x2;
        //std::cout << x2 << " ";;

        fIn >> comma;
        fIn >> y2;
        //std::cout << y2 << "\n";;
        etc.clear();

        if(x1 == x2){
            int max = std::max(y1, y2);
            int min = std::min(y1, y2);
            for(int i = min; i <= max; i++){
                list[x1][i] += 1;
                //std::cout << "HORIZONTAL: " << x1 << " " << i << " " << list[x1][i] << "\n";
            }
        }else if(y1 == y2){
            std::cout << "ENTERED Y" << "\n";
            int max = std::max(x1, x2);
            int min = std::min(x1, x2);
            for(int i = min; i <= max; i++){
                list[i][y1] += 1;
                //std::cout << "VERTICAL: " << y1 << " " << i << " " << list[i][y1] << "\n";
            }
        }else{
            int length = abs(x1 - x2) + 1;
            int x = x1;
            int y = y1;
            for(int i = 0; i < length; i++){
                list[x][y] += 1;
                if(x2 > x1){
                    x++;
                }else{
                    x--;
                }
                if(y2 > y1){
                    y++;
                }else{
                    y--;
                }
            }
        }

        //list = addLines(x1, y1, x2, y2, list, true);

    }

    int counter = 0;

    for(int i = 0; i < 1000; i++){
        for(int j = 0; j < 1000; j++){
            if(list[i][j] >= 2){
                counter++;
            }
        }
    }

    std::cout << counter;

    //std::vector<std::vector<int>> list1 = part1Filter(list);


    return 0;
}
