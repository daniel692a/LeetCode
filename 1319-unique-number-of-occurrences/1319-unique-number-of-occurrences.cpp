class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
       unordered_map<int, int> occurrences;
       for(int i=0; i<arr.size(); i++){
           if(occurrences[arr[i]]){
               occurrences[arr[i]] += 1;
           } else {
               occurrences[arr[i]] = 1;
           }
       }
       unordered_set<int> times;
       for(auto el: occurrences){
           if(times.count(el.second)){
               return false;
           }
           times.insert(el.second);
       }
       return true;
    }
};