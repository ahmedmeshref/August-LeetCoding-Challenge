from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if numCourses < 1:
            return True

        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)

        self.seen = set()
        for course in graph:
            if course in self.seen:
                continue
            if not self.dfs(graph, [course]):
                return False
        return True

    def dfs(self, graph, stack):
        while stack:
            course = stack.pop()
            for pre in graph[course]:
                if pre not in graph:
                    self.seen.add(pre)
                    continue
                if pre in self.seen:
                    if course in self.seen:
                        return False
                    continue
                stack.append(pre)
                self.dfs(graph, stack)
            self.seen.add(course)
        return True


g = Solution()
print(g.canFinish(8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))
