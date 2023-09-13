class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int answer = 0;
        int l=0, r=0;
        unordered_set<char> letters;
        while(r<s.size()){
            if(!letters.contains(s[r])){
                letters.insert(s[r]);
            } else{
                while(letters.contains(s[r]) and r!=l){
                    letters.erase(s[l]);
                    l++;
                }
                letters.insert(s[r]);
            }
            int let = letters.size();
            answer = max(answer, let);
            r++;
        }
        return answer;
    }
};