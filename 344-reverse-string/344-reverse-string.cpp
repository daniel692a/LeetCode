class Solution {
public:
    void reverseString(vector<char>& s) {
        int i  =0; // -> O(1)
        int j = s.size()-1; //-> O(1)
        while(i<=j){ // -> O(n)
            swap(s[i], s[j]);
            i++; j--;
        }
    }
};