

#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.


a = int(input())
nums = list(map(int,input().strip().split()))[:a]
# print(nums)
w = max(nums)
# print(w)
while max(nums) == w:
    nums.remove(max(nums))

print(max(nums))