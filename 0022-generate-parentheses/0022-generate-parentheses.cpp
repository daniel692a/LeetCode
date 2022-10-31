class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> answer;
        this->createCom(n, answer, 0, 0, "");
        return answer;
    }
    void createCom(int n, vector<string> &answer, int open, int close, string combination){
        if(open==n and close==n){
            answer.push_back(combination);
            return;
        }
        if(open<n){
            createCom(n, answer, open+1, close, combination+"(");
        }
        if(close<open){
            createCom(n, answer, open, close+1, combination+")");
        }
    }
};