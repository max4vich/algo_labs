def andrewCounts(arr, P):
    length = len(arr)
    arr.sort()
    for i in range(len(arr)):
        l = i + 1
        r = length - 1
        while l <= r:
            mid = (r + l) // 2
            if arr[mid] == P - arr[i] - arr[l]:
                return True
            elif arr[mid] < P - arr[l] - arr[i]:
                l = mid + 1
            elif arr[mid] > P - arr[l] - arr[i]:
                r = mid - 1

        return False


if __name__ == '__main__':
    print(andrewCounts([3,7,9,13,21], 23))
