#include <iostream>
#include <fstream>
#include <string>
#include <vector>

bool winCheck(std::vector<std::vector<int>> vector1);

std::vector<std::vector<int>> numCheck(std::vector<std::vector<int>> vector1, int i);

void calcAnswer(std::vector<std::vector<int>> vector1, int &i);

void printBoard(std::vector<std::vector<int>> list){
    //prints board out in a format easy to read
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            std::cout << list[i][j] << " ";
        }
        std::cout << "\n";
    }
}

//go through each five lines and find how many turns it takes for that board to win
std::vector<int> turnCalc(std::vector<std::vector<int>> list, bool final){
    //list of answers
    std::vector<int> answers = {63,23,2,65,55,94,38,20,22,39,5,98,9,60,80,45,99,68,12,3,6,34,64,10,70,69,95,96,83,81,32,30,42,73,52,48,92,28,37,35,54,7,50,21,74,36,91,97,13,71,86,53,46,58,76,77,14,88,78,1,33,51,89,26,27,31,82,44,61,62,75,66,11,93,49,43,85,0,87,40,24,29,15,59,16,67,19,72,57,41,8,79,56,4,18,17,84,90,47,25};
    int turns = 0;
    //goes through each answer until the board wins
    for(int i = 0; i < answers.size(); i++){
        int currAnswer = answers[i];
        //checks to see if the answer is in the board
        //if so, makes it negative
        list = numCheck(list, currAnswer);
        //after it flips the number negative, checks to see if the board won
        bool win = winCheck(list);
        //adds a turn
        turns += 1;
        //std::cout << "CURRENT TURNS: " << turns << "\n";
        if(win){
            std::cout << "WIN AT: " << turns << " LAST: " << answers[i] << "\n";
            //very messy way of returning stuff
            //turns is in vecReturn[0], last answer is in vecReturn[i]
            std::vector<int> vecReturn;
            if(final){
                calcAnswer(list, currAnswer);
            }else{
                printBoard(list);
            }
            vecReturn.push_back(turns);
            vecReturn.push_back(answers[i]);
            return vecReturn;
        }
    }
    //idk just returning back obviously false stuff
    std::vector<int> vecReturnBad;
    vecReturnBad.push_back(-47);
    vecReturnBad.push_back(-47);
    return vecReturnBad;
}

//checks to see if the num is in the list
std::vector<std::vector<int>> numCheck(std::vector<std::vector<int>> list, int num){
    //goes through each axis
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            //std::cout << list[i][j] << " " << i << " " << j << "\n";
            //if the num is in the board, set it negative
            if(list[i][j] == num){
                list[i][j] *= -1;
                //std::cout << num << " found at location: list[" << i << "][" << j << "]" << "\n";
            }
        }
    }
    return list;
}

//checks to see if the board has won yet
bool winCheck(std::vector<std::vector<int>> list){
    //checking rows
    for(int i = 0; i < 5; i++){
        //if all are negative, board wins
        if(list[i][0] < 0 && list[i][1] < 0 && list[i][2] < 0 && list[i][3] < 0 && list[i][4] < 0){
            //std::cout << list[i][0] << list[i][0] <<list[i][0] <<list[i][0] <<list[i][0] << "\n";
            //printBoard(list);
            return true;
        }
    }
    //checking columns
    for(int i = 0; i < 5; i++){
        //if all are negative, board wins
        if(list[0][i] < 0 && list[1][i] < 0 && list[2][i] < 0 && list[3][i] < 0 && list[4][i] < 0){
            //std::cout << list[i][0] << list[i][0] <<list[i][0] <<list[i][0] <<list[i][0] << "\n";
            //printBoard(list);
            return true;
        }
    }
    //board didn't win, return back false
    return false;
}


void calcAnswer(std::vector<std::vector<int>> board, int &winInt){
    int sumTotal = 0;
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            if(board[i][j] > 0){
                sumTotal += board[i][j];
            }
        }
    }
    std::cout << sumTotal * winInt;
}


int main() {

    //CHANGE LINE 169 TO GET ANSWER TO DIFFERENT PART

    //boilerplate
    std::ifstream fIn;
    fIn.open("../aoc_day4.txt");

    //VARIABLES
    //---------
    //created to hold the current lowest turn board
    std::vector<std::vector<int>> lowestBoard;
    //holds the value that the board won on
    int winInt;
    //holding all of the data for all boards
    std::vector<std::vector<int>> list;
    //holds the current line that is being read in
    std::vector<int> currLine;
    //holds the current int being read in
    int curr;
    //list of answers as given from AdventofCode
    std::vector<int> answers = {63,23,2,65,55,94,38,20,22,39,5,98,9,60,80,45,99,68,12,3,6,34,64,10,70,69,95,96,83,81,32,30,42,73,52,48,92,28,37,35,54,7,50,21,74,36,91,97,13,71,86,53,46,58,76,77,14,88,78,1,33,51,89,26,27,31,82,44,61,62,75,66,11,93,49,43,85,0,87,40,24,29,15,59,16,67,19,72,57,41,8,79,56,4,18,17,84,90,47,25};
    //sentinel value of -1;
    int lowestTurns = -1;
    //holds the turns -> [0] and what will be the winInt -> [1]
    std::vector<int> turns;

    while(fIn && fIn.peek() != EOF){

        //reads in X in list[X][...]
        for(int i = 0; i < 5; i++){
            //reads in X in list[...][X]
            for(int k = 0; k < 5; k++){
                fIn >> curr;
                currLine.push_back(curr);
                //std::cout << currLine[k] << "\n";
                fIn.clear();
            }
            list.push_back(currLine);
            //clears stuff
            currLine.clear();
            fIn.clear();
        }
        //printBoard(list);

        turns = turnCalc(list, false);

        std::cout << "TURNS: " << turns[0] << "\n";

        //this is for the first one
        if(lowestTurns == -1){
            lowestTurns = turns[0];
            lowestBoard = list;
            winInt = turns[1];
        }else{
            //-----------------------------------------
            //JUST CHANGE < FOR PART 1 AND > FOR PART 2
            //-----------------------------------------
            //i dont care if there is an easier way to do this its 2 am

            //this updates if there is new lowest
            if(turns[0] < lowestTurns){
                lowestTurns = turns[0];
                lowestBoard = list;
                winInt = turns[1];
            }
        }
        list.clear();
    }

    std::cout << "------------------------------------------------------" << "\n";
    std::cout << "WINNING BOARD" << "\n";
    printBoard(lowestBoard);
    std::cout << "\n" << "ANSWER:" "\n";

    turnCalc(lowestBoard, true);

    //63424 part 1
    //23541 part 2

    //59 35 52 -60 91
    //75 86 13 -39 21
    //33 -99 11 -64 50
    //37 58 71 -22 54
    //-6 72 88 -3 85

//    int sumStuff = 0;
//    sumStuff = 59 + 35 + 52 + 91 + 75 + 86 + 13 + 21 + 33 + 11 + 50 + 37 + 58 + 71 + 54 + 72 + 88 + 85;
//    std::cout << sumStuff * 64 << "\n";

    //-52 -83 84 -21 -59
    //-30 -64 -85 90 -91
    //-24 -32 57 0 -81
    //17 47 -1 25 -27
    //-10 -51 -65 79 -34

//    int sumStuff2 = 0;
//    sumStuff2 = 84 + 90 + 57 + 0 + 17 + 47 + 25 + 79;
//    std:: cout << sumStuff2 * 59 << "\n";

//    int i = 5;
//    std::cout << list[i][0] << list[i][1] << list[i][2] << list[i][3] << list[i][4] << "\n";
//    std::cout << list.size();

    //go through each five lines and find how many turns it takes for that board to win

//    for(int i = 0; i < list.size(); i){
//
//        //std::vector<std::vector<int>> currentBoard;
//        i++;
//    }



    return 0;
}
