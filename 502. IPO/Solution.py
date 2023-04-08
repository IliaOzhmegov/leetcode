from bisect import bisect_left
from collections import defaultdict
from collections import Counter
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


class CostProfit:
    def __init__(self, profits: List[int], capital: List[int], w: int) -> None:
        self.profits_counter = Counter(profits)
        self.capital_counter = Counter(capital)
        self.cost_profit = defaultdict(int)

        for profit, cost in zip(profits, capital):
            cost_to_save = max(cost, w)
            self.cost_profit[cost_to_save] = max(self.cost_profit[cost_to_save], profit)

        self.costs = sorted(self.cost_profit.keys())
        self.profits = sorted(self.profits_counter.keys())

    def __len__(self) -> int:
        return len(self.profits_counter)

    def pop_max_profit_for(self, cost):
        while len(self.costs) and cost >= self.costs[0]:
            self.cost_profit[cost] = max(self.cost_profit[cost], self.cost_profit.pop(self.costs.pop(0)))

        if self.cost_profit[cost] == 0: return -1
        i = bisect_left(self.profits, self.cost_profit[cost])
        profit = self.profits[i]
        self.profits_counter[profit] -= 1
        if self.profits_counter[profit] == 0:
            self.profits_counter.pop(profit)
            self.profits.pop(i)
        self.cost_profit[cost+profit] = self.cost_profit[cost]
        return profit

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cost_profit = CostProfit2(profits, capital, w)

        while k and len(cost_profit):
            profit = cost_profit.pop_max_profit_for(w)
            if profit == -1: break
            w += profit  ## now sure, weird thou
            k -= 1

        return w
