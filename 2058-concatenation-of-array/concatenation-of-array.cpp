class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n;
        n = nums.size();
        //create ans of length 2n
        //ans[i] == nums[i]
        //ans[i+n] == nums[i]
        //0<=i<n
        //ans = concentation of 2 nums arrays
        //return ans
        for(int i = 0; i<2*n; i++) {
            if(i<n) {
                nums.insert(nums.begin() + i + n, nums[i]);
            }
        }
        vector<int> ans;
        ans = nums;
        return ans;
    }
};