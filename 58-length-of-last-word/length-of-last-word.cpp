class Solution {
public:
    int lengthOfLastWord(string s) {
        int n;
        n = s.length();
        int i;
        i = n-1;
        int x;
        x = 0;
        while(s[i] == ' ') {
            i--;
        }
        while(i>=0 && s[i] != ' ' ) {
            x++;
            i--;
        }    
        return x;
    }
};