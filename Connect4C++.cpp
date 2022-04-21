/*Connect 4 game
This game is played by 2 players
Players choose a symbol, either X or O. 
Each player in his turn drop his symbol from top of the board to the bottom
The first player to connect 4 symbols horizontally, vertically or diagonally wins.
Author:Habiba Alaa Mohamed Ali El-Behairy
Date:28-2-2022
version:1.0
*/
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int rows=6;
int columns=7;
string player1="X";
string player2="O";
string board[6][7];
int player = 1;


void bodyshape( string board[6][7])//build board
    {
        for (int x=0;x<7;x++) //each element in columns
            {
                cout<<x+1<<setw(1);//#Number of columns
            }

        cout<<'\n';
        for (int i=0;i<6;i++)//each element in rows
            {
                for(int j=0;j<7;j++)//each element in columns
                {
                    cout<<board[i][j];//print rows and columns "board"
                }
                cout<<'\n';
            }
    }

bool horizontalwinning(string player1,string player2)//check for horizontal win
    {
        bool iswin = false;
        for (int j=0;j<rows;j++)//in each row
            {
            for (int i=0; i<(columns-3);i++)//check each element in row if there is 4 connected horizontally
            {
                if ((board[j][i]== player1) && (board[j][i+1]== player1) && (board[j][i+2]==player1) && (board[j][i+3]==player1))
                       {
                        cout <<"X wins in horizontal way";
                        iswin = true;
                       }
                if ((board[j][i]== player2) && (board[j][i+1]== player2) && (board[j][i+2]==player2) && (board[j][i+3]==player2))
                    {
                        cout<<"O wins in horizontal way";
                        iswin = true;
                    }
                }
            }
            return iswin;
    }
bool verticalwinning(string player1,string player2)//check vertical win
    {
        bool iswin = false;
        for (int i=0;i<columns;i++)//in each columns
            {
            for (int j=0; j<(rows-3);j++)//check each element in column if there is 4 connected vertically
            {
                if (board[j][i]== player1 && board[j+1][i]== player1 && board[j+2][i]==player1 && board[j+3][i]==player1)
                       {
                        cout <<"X wins in vertical way";
                       iswin = true;
                       }
                if (board[j][i]== player2 && board[j+1][i]== player2 && board[j+2][i]==player2 && board[j+3][i]==player2)
                    {
                        cout<<"O wins in vertical way";
                        iswin = true;
                    }
                }
            }
            return iswin;
    }
bool diagonalwinning(string piece)//check diagonal win
    {
        bool iswin = false;
        for (int i=0;i<(columns-3);i++)//in each 4 columns
            {
            for (int j=0; j<(rows-3);j++)//check each elements in the 4 rows of columns if there is 4 connected in diagonal way
            {
                if (board[j][i]== piece && board[j+1][i+1]== piece && board[j+2][i+2]==piece && board[j+3][i+3]==piece)
                       {
                        cout <<piece<<" wins in diagonal way";
                        iswin = true;

                       }
            }
            }
            for (int i=0;i<(columns-3);i++)//in each 4 columns
            {
            for (int j=0; j<rows;j++)//check each elements starting from third row of columns if there is 4 connected in diagonal way
            {
                if (board[j][i]== piece && board[j-1][i+1]== piece && board[j-2][i+2]==piece && board[j-3][i+3]==piece)
                       {
                        cout <<piece<<" wins in diagonal way";
                        iswin = true;

                       }
                    }
                }
                return iswin;

    }
bool gamedraw()// check if game draw
{
    int i=0;

    for(int x=0; x<rows; x++)//each row in board
        {
        for (int eachelement=0; eachelement<columns; eachelement++)
            {                                                       //check each element and if its empty(*) or not
                if (board[x][eachelement]=="" "*")
                {
                    i+=1;
                }
            }
        }
    if (i==0)
        {
        cout<<"The game draw";//if all elements are full and there is no winner ther game draw
        return true;
        }

            return false;

}
bool checkwinner()//check winner
{
    if (
    horizontalwinning(player1,player2) ||
    verticalwinning (player1,player2)
     || diagonalwinning (player1)
     || diagonalwinning (player2)
     || gamedraw()
     )
            {
            return true;
            }
            else{
            return false;
            }
}

void methodofplaying()//how to play
{
   int chosencolumn=0;
   bodyshape(board);
    while(true)
    {
        cout <<"Please enter number from 1 to 7:"<<endl;
        cin >>chosencolumn;//Column which player choose to drop his piece

        if (chosencolumn<0 || chosencolumn>7)
            {
            while (true)
                {
                if (chosencolumn<0 || chosencolumn>7)
                    {
                        cout <<"Please enter number from 1 to 7:"<<endl;
                        cin >>chosencolumn;
                        }

                else {
                    break;

                }
              }
            }
                
        for (int i=(rows-1);i>=0;i--)//to start from the bottom and let the pieces droped to bottom 
        { 
            if (player==1)
                {
                if (board[i][chosencolumn-1]=="" "*")//#to see which index of the chosen column is empty(*)
                    { 
                    board[i][chosencolumn-1]="X"; //fill the empty index with the piece of player 1
                    player=2;
                    break;
                    }
                }
            else
                {
                if (board[i][chosencolumn-1]=="" "*")//#to see which index of the chosen column is empty(*)
                    { 
                    board[i][chosencolumn-1]="O" ;//fill the empty index with the piece of player 2
                    player=1;
                    break;
                }
            }
          }
        bodyshape(board);
        if (checkwinner()){
            break;
        }
    }


}
int main()
{

    for (int i=0;i<6;i++)//each element in rows
        {
            for(int j=0;j<7;j++)//each element in columns
             {
                board[i][j]="" "*";//put * in the each element of the board (indexes of rows and colums)
             }
        }
    methodofplaying( );


}
