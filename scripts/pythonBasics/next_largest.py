class Solution:
    def next_larger_element(self, arr):
        arr_updated = []
        for i in range(0, len(arr)):
            count = 0
            for j in range(i+1, len(arr)):
                if arr[i] < arr[j]:
                    arr[i] = arr[j]
                    arr_updated.insert(i, arr[i])
                    count += 1
                    break
            if count == 0:
                arr_updated.insert(i, -1)
        return arr_updated
