
class Solution:
    def frequencySort(self, s: str) -> str:

        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        arr = []

        for ch in freq:
            arr.append([ch, freq[ch]])

        def merge_sort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            res = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):

                if left[i][1] >= right[j][1]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1

            while i < len(left):
                res.append(left[i])
                i += 1

            while j < len(right):
                res.append(right[j])
                j += 1

            return res

        arr = merge_sort(arr)

        ans = ""

        for ch, count in arr:
            ans += ch * count

        return ans

        