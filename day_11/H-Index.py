def hIndex(citations) -> int:
    citations.sort()
    ln = len(citations)
    start = 0
    end = ln - 1
    while start <= end:
        mid = (start + end) // 2
        greater_n = ln - mid
        if citations[mid] == greater_n:
            return greater_n
        elif citations[mid] > greater_n:
            end = mid - 1
        else:
            start = mid + 1
    return ln - start

