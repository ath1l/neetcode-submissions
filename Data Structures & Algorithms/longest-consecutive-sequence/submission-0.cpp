class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) return 0;
        sort(nums.begin(),nums.end());

        vector<vector<int>> grpd;
        grpd.push_back({nums[0]});

        for(int i=1;i<nums.size();i++)
            {
                if(nums[i] == grpd.back().back())
                    {
                        continue;
                    }
                if(nums[i] - grpd.back().back() == 1) {
                    grpd.back().push_back(nums[i]);
                } else {
                    grpd.push_back({nums[i]});
                }
            }
        int ans = 0;
        for (auto &g :grpd) ans = max(ans, (int)g.size());
        return ans;
    }
};