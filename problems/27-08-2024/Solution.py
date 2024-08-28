class Solution:
    def sortByFreq(self,arr):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        sorted_arr = sorted(arr, key=lambda x: (-freq[x], x))
        return sorted_arr     

sol=Solution()

arr=[5,5,4,6,4]
result=sol.sortByFreq(arr)
print(result)