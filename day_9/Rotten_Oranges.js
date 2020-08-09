/** Find min minutes needed to rotten a grid of oranges
 * @param {number[][]} grid
 * @return {number}
 */
let orangesRotting = function (grid) {
    let rotten_queue = [], tot_fresh = 0, min_mins = 0,
        rows = grid.length, cols = grid[0].length,
        new_rotten = false;

    let makeRotten = (i, j) => {
        grid[i][j] = 2;
        tot_fresh--;
        new_rotten = true;
        return [i, j]
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] === 2) rotten_queue.push([i, j]);
            else if (grid[i][j] === 1) tot_fresh++;
        }
    }

    while (rotten_queue.length) {
        const ln = rotten_queue.length;
        new_rotten = false;
        for (let _ = 0; _ < ln; _++) {
            let [i, j] = rotten_queue.shift();
            if (i - 1 >= 0 && grid[i - 1][j] === 1) rotten_queue.push(makeRotten(i - 1, j));
            if (i + 1 < rows && grid[i + 1][j] === 1) rotten_queue.push(makeRotten(i + 1, j));
            if (j - 1 >= 0 && grid[i][j - 1] === 1) rotten_queue.push(makeRotten(i, j - 1));
            if (j + 1 < cols && grid[i][j + 1] === 1) rotten_queue.push(makeRotten(i, j + 1));
        }
        if (new_rotten) min_mins++;
    }
    return tot_fresh ? -1 : min_mins;
};