class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map <string,vector<string>> hMap;
        for(string &s:strs)
            {
                string key = s;
                sort(key.begin(),key.end());
                hMap[key].push_back(s);
            }
        vector<vector <string>> result;
        for(auto &entry :hMap)
            {
                //string key = entry.first;
                //vector<string> group = entry.second;
                result.push_back(entry.second);
            }
        return result;
    }
};