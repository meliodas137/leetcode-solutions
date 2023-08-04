class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        if(numCourses == 1) return true;

        //Khan's Algo
        vector<int> indegree(numCourses, 0);
        vector<int> temp;
        vector<vector<int>> adj(numCourses, temp);
        for(auto vec:prerequisites){
            indegree[vec.front()]++; 
            adj[vec.back()].push_back(vec.front());
        }
        
        vector<int> queue = {};
        for(int i =0;i<numCourses;i++){
            if(indegree[i]==0) queue.push_back(i);
        }
        
        int count = 0;
        while(!queue.empty()){
            int node = queue.back();
            queue.pop_back();
            count++;
            for(auto i:adj[node]){
                indegree[i]-=1;
                if(indegree[i]==0) queue.push_back(i);
            }
        }
        if(count==numCourses) return true;
        return false;
    }
};