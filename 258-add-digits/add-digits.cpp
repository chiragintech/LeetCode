class Solution {
public:
    int addDigits(int num) {
        int sum = 0;
        int last = 0;
        while(num>0) {
            last = num % 10;
            sum +=last;
            num = num/10;
            if(num == 0 && sum>9) {
                num = sum;
                sum = 0;
            }
        }
        return sum;
    }
};