class Solution:

    def __init__(self):
        self.memo = [-1]*1024;


    def findDistance(worker: List[int], bike: List[int]) -> int:
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

    def minimumDistanceSum(workers: List[List[int]], bikes: List[List[int]], worker_index: int, mask: int):
        if worker_index >= len(workers):
            return 0

        # if result is already calculated, return it no recursion is needed
        if self.memo[mask] != -1:
            return self.memo[mask]

        smallest_distance_sum = sys.maxsize
        for bike_index in range(len(bikes)):
            # check if the bike at bike_index is available
            if mask & (1 << bike_index) == 0:
                # adding the current distance and repeat the process for next worker
                # also changing the bit at index bike_index to 1 to show the bike there is assigned 
                smallest_distance_sum = min(smallest_distance_sum,
                                            self.findDistance(workers[worker_index], bikes[bike_index]) +
                                            self.minimumDistanceSum(workers, bikes, 
                                                                    worker_index + 1,
                                                                    mask | (1 << bike_index)
                                                                    )
                                            )


        # memoizing the result corresponding to mask
        self.memo[mask] = smallest_distance_sum
        return self.memo[mask]

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        return minimumDistanceSum(workers, bikes, 0, 0)

