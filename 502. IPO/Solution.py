from bisect import bisect_left
from collections import defaultdict
from typing import List
import heapq


class CostProfit:
    def __init__(self, profits: List[int], capital: List[int], w: int) -> None:
        self.current_cost = -1
        self.profit = []
        self.cost_profit = defaultdict(list)
        for profit, cost in zip(profits, capital):
            if cost <= w:
                self.profit.append(-profit)
                self.current_cost = max(self.current_cost, cost)
            else:
                self.cost_profit[cost].append(profit)

        self.costs = sorted(self.cost_profit.keys())

        if len(self.profit) >= 0: heapq.heapify(self.profit)

    def __len__(self) -> int:
        return max(len(self.profit), len(self.costs))

    def pop_max_profit_for(self, cost):
        if cost < self.current_cost: return -1  # such value does not exist
        if self.__len__() == 0: return -1  # no more values

        # if cost == self.cost:
        # return -heapq.heappop(self.heaped_profit)

        # expanding pool
        while len(self.costs) and self.costs[0] <= cost:
            self.profit.extend([-a for a in self.cost_profit.pop(self.costs[0])])
            self.cost = self.costs.pop(0)
        heapq.heapify(self.profit)

        return -heapq.heappop(self.profit) if len(self.profit) > 0 else -1


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cost_profit = CostProfit(profits, capital, w)

        while k and len(cost_profit):
            profit = cost_profit.pop_max_profit_for(w)
            if profit == -1: break
            w += profit  ## now sure, weird thou
            k -= 1

        return w
