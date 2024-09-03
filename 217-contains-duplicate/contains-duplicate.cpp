class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n;
        sort(nums.begin(),nums.end());
        n = nums.size();
        for (int i = 1; i<n; i++) {
                if (nums[i] == nums[i-1]) {
                    return true;
            }
        }
        return false;
    }
};