class Solution {
public:
    // Maximum value of mask will be 2^(Number of bikes)
    // and number of bikes can be 10 at max
    int memo[1024];
    
    // Manhattan distance
    int findDistance(vector<int>& worker, vector<int>& bike) {
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1]);
    }
    
    int minimumDistanceSum(vector<vector<int>>& workers, vector<vector<int>>& bikes, int workerIndex, int mask) {
        if (workerIndex >= workers.size()) {
            return 0;
        }
        
        // If result is already calculated, return it no recursion needed
        if (memo[mask] != -1)
            return memo[mask];
        
        int smallestDistanceSum = INT_MAX;
        for (int bikeIndex = 0; bikeIndex < bikes.size(); bikeIndex++) {
            // Check if the bike at bikeIndex is available
            if ((mask & (1 << bikeIndex)) == 0) {
                // Adding the current distance and repeat the process for next worker
                // also changing the bit at index bikeIndex to 1 to show the bike there is assigned
                smallestDistanceSum = min(smallestDistanceSum, 
                             findDistance(workers[workerIndex], bikes[bikeIndex]) + 
                                          minimumDistanceSum(workers, bikes, workerIndex + 1, 
                                                             mask | (1 << bikeIndex)));
            }
        }
        
        // Memoizing the result corresponding to mask
        return memo[mask] = smallestDistanceSum;
    }
    
    int assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) { 
        // Marking all positions to -1 that signifies result 
        // has not been calculated yet for this mask
        memset(memo, -1, sizeof(memo));
        return minimumDistanceSum(workers, bikes, 0, 0);
    }
};
