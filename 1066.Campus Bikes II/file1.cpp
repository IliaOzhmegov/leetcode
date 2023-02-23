class Solution {
public:
    // Maximum number of bikes is 10
    int smallestDistanceSum = INT_MAX;
    int visited[10];
    
    // Manhattan distance
    int findDistance(vector<int>& worker, vector<int>& bike) {
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]);
    }
    
    void minimumDistanceSum(vector<vector<int>>& workers, int workerIndex, 
                            vector<vector<int>>& bikes,   int currDistanceSum) {
        if (workerIndex >= workers.size()) {
            smallestDistanceSum = min(smallestDistanceSum, currDistanceSum);
            return;
        }
        // If the current distance sum is greater than the smallest result 
        // found then stop exploring this combination of workers and bikes
        if (currDistanceSum >= smallestDistanceSum) {
            return;
        }
        
        for (int bikeIndex = 0; bikeIndex < bikes.size(); bikeIndex++) {
            // If bike is available
            if (!visited[bikeIndex]) {
                visited[bikeIndex] = true;
                minimumDistanceSum(workers, workerIndex + 1, 
                        bikes, currDistanceSum + findDistance(workers[workerIndex], bikes[bikeIndex]));
                visited[bikeIndex] = false;
            }
        }
        
    }
    
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        minimumDistanceSum(workers, 0, bikes, 0);
        return smallestDistanceSum;
    }
};
