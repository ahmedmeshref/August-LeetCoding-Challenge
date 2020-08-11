/**
 * @param {number[]} citations
 * @return {number}
 */
let hIndex = function (citations) {
    citations.sort((x, y) => x - y);
    const ln = citations.length;
    let start = 0, end = ln - 1;
    while (start <= end) {
        let mid = Math.floor((end + start) / 2),
            h_ind = ln - mid;
        if (citations[mid] === h_ind) return h_ind;
        else if (citations[mid] > h_ind) end = mid - 1;
        else start = mid + 1;
    }
    return ln - start;
};

