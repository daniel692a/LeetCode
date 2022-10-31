class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> answer;
        this->createCom(n*2, answer, 0, 0, "");
        return answer;
    }
    void createCom(int length, vector<string> &answer, int open, int close, string combination){
        if(combination.size()==length){
            answer.push_back(combination);
            return;
        }
        if(open<(length/2)){
            createCom(length, answer, open+1, close, combination+"(");
        }
        if(close<open){
            createCom(length, answer, open, close+1, combination+")");
        }
    }
};