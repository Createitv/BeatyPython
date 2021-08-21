#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 遍历一遍数组，计算每次到当天为止的最小股票价格保证当天卖一定是利润最大
        # 不断调整maxprofit，保证遍历数组之后为最大值
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit

        
# @lc code=end
