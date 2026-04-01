class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = defaultdict(list) # Course : [prereqs]
        visited = set()
        visiting = set()
        res = []
        for course1, course2 in prerequisites:
            courseMap[course1].append(course2)

        def dfs(courseA):
            if courseA in visiting:
                return True
            if courseA in visited:
                return False
            
            visiting.add(courseA)
            for prereqs in courseMap[courseA]:
                if dfs(prereqs):
                    return True
            visited.add(courseA)
            visiting.remove(courseA)
            res.append(courseA)

            return False
        
        for course in range(numCourses):
            dfs(course)
        
        return res if len(res) == numCourses else []