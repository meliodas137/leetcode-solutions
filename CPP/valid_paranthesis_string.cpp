class Solution {
public:
    bool checkValidString(string s) {
        int star = 0;
        int open = 0;
        int close = 0;
        for(auto &ch:s){
            if(ch == '(') open++;
            if(ch == ')') {
                if(open>0) open--;
                else if(star>0) star--;
                else return false;
            }
            if(ch == '*') star++;
        }
        star = 0;
        for(int i = s.size() -1; i>=0; i--){
            auto ch = s[i];
            if(ch == '('){
                if(close>0) close--;
                else if(star>0) star--;
                else return false;
            }
            if(ch == ')') close++;
            if(ch == '*') star++;
        }
        return true;
    }
};
