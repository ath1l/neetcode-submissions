class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

       vector<unordered_set<char>> rows(9);
       vector<unordered_set<char>> cols(9);
       vector<unordered_set<char>> box(9);

        
       for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
                {
                    if(board[i][j] == '.') continue;

                    //row check
                    if(rows[i].count(board[i][j])) return false;
                    rows[i].insert(board[i][j]);
                    
                    //checking column
                    if(cols[j].count(board[i][j])) return false;
                    cols[j].insert(board[i][j]);

                    //box check
                    int boxIndex = (i / 3) * 3 + (j / 3);
                    if (box[boxIndex].count(board[i][j])) return false;
                    box[boxIndex].insert(board[i][j]);


                }
        }
        
    
        
        return true;
    }

};