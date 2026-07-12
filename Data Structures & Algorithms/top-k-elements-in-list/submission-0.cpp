class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int,int> hMap;
        for(int i=0;i<nums.size();i++)
            {
                        hMap[nums[i]]++;
            }
        vector<pair<int,int>> temp;
        for(auto& entry :hMap) //moving into vector of pairs
            {
                temp.push_back({entry.second,entry.first});//flipping so ezz sorting 
            }
        sort(temp.begin(),temp.end(),greater<pair<int,int>>());
     //sort(temp.begin(), temp.end(), [](pair<int,int>& a, pair<int,int>& b) {
     // return a.first > b.first; // sort by frequency descending
     //});

        vector <int> ans;
        for(int i=0;i<k;i++)
            {
                ans.push_back(temp[i].second);
            }
        return ans;
    }
};