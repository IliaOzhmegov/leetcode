

class Solution:

    def __init__(self):
        self.smallest_distance_sum = sys.maxsize
        self.visited = [False]*10

    @staticmethod
    def findDistance(worker, bike) -> int:
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

    def minimumDistanceSum(self,
                           workers, worker_index,
                           bikes,   curr_distance_sum):
        if worker_index >= len(workers):
            self.smallest_distance_sum = min(self.smallest_distance_sum, curr_distance_sum)
            return None

        if curr_distance_sum >= self.smallest_distance_sum:
            return None

        for bike_index in range(len(bikes)):
            if not self.visited[bike_index]:
                self.visited[bike_index] = True
                self.minimumDistanceSum(workers, 
                                        worker_index + 1,
                                        bikes,
                                        curr_distance_sum + self.findDistance(workers[worker_index],
                                                                              bikes[bike_index])
                                        )
                self.visited[bike_index] = False

    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.minimumDistanceSum(workers, 0, bikes, 0)
        return self.smallest_distance_sum

