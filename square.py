## 直接使用函式
import math
def is_square(n):
    if n < 0:
        return False
    sqrt_n = math.sqrt(n)
    return sqrt_n.is_integer()

## 使用遍歷
# def is_square(n):
#     # 4 = 2x2
#     # 36 = 6x6
#     # 48 < 7x7
#     if n < 0:
#         return False
#     for i in range(n+1):
#         if i*i == n:
#             return True
#         elif i*i > n:
#             return False
#             break
#     return False

## 優化遍歷的缺點
# n數值越大，i就會遍歷越久，
# 嘗試使用binary search方式
# def is_square(n):
#     if n < 0:
#         return False
#     low = 0
#     High = n
#     while low <= High:
#         mid = (High+low)//2
#         square = mid*mid
#         if square == n:
#             return True
#         elif square > n:
#             High = mid - 1
#         else:
#             low = mid + 1
#     return False
