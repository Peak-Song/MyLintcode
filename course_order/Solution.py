from typing import List


class Solution:
    # @example 2, [[1,0]] 总共有 2 门课程。要学习课程 1，你需要先完成课程 0
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return list(range(numCourses))

        dep_map = {}  # k, v 要学习k，要先学习v
        course_set = set()

        for c, d in prerequisites:
            course_set.add(c)
            course_set.add(d)

            if c in dep_map:
                dep_map[c].add(d)
            else:
                dep_map[c] = {d}

            if d not in dep_map:
                dep_map[d] = set()
            else:
                if c in dep_map[d]:
                    return []

        res = list(set(range(numCourses)) - course_set)

        for c, deps in dep_map.items():
            if len(deps) == 0:
                res.append(c)

        # print(dep_map)
        visited_set = set(res)
        course_set -= visited_set

        while len(course_set):
            for c in course_set:
                if not dep_map[c].issubset(visited_set):
                    continue
                visited_set.add(c)
                res.append(c)
            course_set -= visited_set

        return res


if __name__ == '__main__':
    print(Solution().findOrder(5, []))
    print(Solution().findOrder(5, [[0, 1]]))
    print(Solution().findOrder(2, [[0, 1], [1, 0]]))
    print(Solution().findOrder(2, [[1, 0]]))
    print(Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
