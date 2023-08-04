/*
 * // This is the custom function interface.
 * // You should not implement it, or speculate about its implementation
 * class CustomFunction {
 * public:
 *     // Returns f(x, y) for any given positive integers x and y.
 *     // Note that f(x, y) is increasing with respect to both x and y.
 *     // i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
 *     int f(int x, int y);
 * };
 */

class Solution {
public:
    vector<vector<int>> findSolution(CustomFunction& customfunction, int z) {
        if(customfunction.f(1,1) == z) return {{1,1}};        
        if(customfunction.f(1000,1000) == z) return {{1000,1000}}; 
        vector<vector<int>> res;
        for(int i = 1; i<=1000;i++){
            auto temp = customfunction.f(i,1);
            if(temp>z) {
                    break;
            }
            for(int j = 1; j<=1000; j++){
                temp = customfunction.f(i,j);

                if(temp==z) {
                    res.push_back({i,j});
                    break;
                } else if(temp > z) break;
            }
        }
        return res;
    }
};