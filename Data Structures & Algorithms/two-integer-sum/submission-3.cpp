
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int,int> hMap;

        for(int i=0;i<nums.size();i++)
            {
                int complement = target - nums[i];
                if(hMap.find(complement) != hMap.end())
                    {
                        return {hMap[complement],i};
                    }
                hMap[nums[i]] = i;
            }
        return {};
    }
};