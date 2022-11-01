class Solution {
public:
    int maxPower(string s) {
        int answer = 0;
        int i=0;
        int count = 0;
        char current = '1';
        while(i<s.size()){
            if(current==s[i]){
                i++;
                count = 1;
                while(i<s.size() and s[i]==current){
                    count++;
                    i++;
                }
                answer = max(answer, count);
                current = s[i];
            } else {
                current=s[i];
            }
        }
        return answer;
    }
};