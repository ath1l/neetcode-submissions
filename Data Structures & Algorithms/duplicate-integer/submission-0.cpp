class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        unordered_map <int,int> hMap;
        
        for(int i=0;i<nums.size();i++)
            {
                if(hMap.find(nums[i]) != hMap.end())
                    {
                        return true;
                    }
                hMap[nums[i]] = i;
            }
            return false;
    }
};