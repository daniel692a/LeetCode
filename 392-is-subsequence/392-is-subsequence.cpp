class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i = 0, j = 0;
        while((j<t.size()) and (i<s.size())){
            if(t[j]==s[i]){
                i++;
            }
            j++;
        }
        return (i==s.size())?true:false;
    }
};