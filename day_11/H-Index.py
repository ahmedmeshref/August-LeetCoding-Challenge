# time comp: O(n*log(n))
# def hIndex(citations) -> int:
#     citations.sort()
#     ln = len(citations)
#     start = 0
#     end = ln - 1
#     while start <= end:
#         mid = (start + end) // 2
#         greater_n = ln - mid
#         if citations[mid] == greater_n:
#             return greater_n
#         elif citations[mid] > greater_n:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return ln - start

# time comp: O(n)
def hIndex(citations) -> int:
    n = len(citations)
    occ = [0] * (n+1)
    for cit in citations:
        if cit > n:
            occ[-1] += 1
        else:
            occ[cit] += 1

    h_ind, ans = n, 0
    for i in range(len(occ)):
        if h_ind == i:
            return h_ind
        elif h_ind > i:
            ans = i
        h_ind -= occ[i]
    return ans


print(hIndex([100]))
