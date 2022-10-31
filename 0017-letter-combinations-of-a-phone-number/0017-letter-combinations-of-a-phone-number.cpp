class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> answer;
        if(digits.size()==0){
            return answer;
        }
        unordered_map<char, string> buttons = {
            {'2', "abc"},
            {'3', "def"},
            {'4', "ghi"},
            {'5', "jkl"},
            {'6', "mno"},
            {'7', "pqrs"},
            {'8', "tuv"},
            {'9', "wxyz"}
        };
        // for(auto &data: buttons){
        //     cout<<data.first<<" "<<data.second<<"\n";
        // }
        createCombinations(0, "", buttons, answer, digits);
        return answer;
    }
    void createCombinations(int i, string current, unordered_map<char, string> buttons, vector<string> &answer, string &digits){
        if(current.size()==digits.size()){
            answer.push_back(current);
            return;
        }
        for(auto c: buttons[digits[i]]){
            createCombinations(i+1, current+c, buttons, answer, digits);
        }
    }
};