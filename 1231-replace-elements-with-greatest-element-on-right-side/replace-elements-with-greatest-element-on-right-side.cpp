class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        //replace every element with greatest among elements to the right, last replace as -1
        int n,x;
        n = arr.size();
        for(int i = 0; i<n; i++) {
            if (i != (n-1)) {
                x = arr[i+1];
                for (int j = i+1; j<n; j++) {
                    if (arr[j] > x) {
                        x = arr[j];
                    }
                }
                arr[i] = x;
            }
            else{
                arr[i] = -1;
            }
        }
        return arr;
    }
};