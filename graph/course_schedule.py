"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

Difficulty: Medium
Completed: 5/24/2022

"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = [[]]*numCourses
        for course, prereq in prerequisites:
            prereqs[course] = prereqs[course] + [prereq]                    # build connected graph
        
        checked = []
        def recursion(flag_nums, courses):
            if len(set(courses) & set(flag_nums)):                          # check if there is a banned course in courses
                return False                                                # problem if course is a prereq to itself
            for course in courses:                                          
                if not course in checked:                                   # avoid checking same course twice
                    if not recursion(flag_nums+[course], prereqs[course]):  # recursion step: check that course's prereqs
                        return False
                    checked.append(course)
            return True
        return recursion([],range(numCourses))                              # perform recursion on all the courses in the class
  
  
"""
Explanation:

There will be a problem if a course is it's own prerequisite, or the course is a prerequisite to its prerequisite,
or a prerequisite to its prerequisite to its prerequisite, and so on.

We first build a connected graph where prereq[i] contains the prerequisites to course i.

Then we recursively check each course's prerequisites, and the prerequisites to the prerequisites, and so on.
"flag_nums" contains a running list of courses that would cause an loop if is a prerequisite. If a flagged course
appears as a prerequisite, then we know there is a loop in the courses, so we immediately return False

The list "checked" gets updated every time we check a new course. This avoids checking the same course more than once.

Time Complexity: O(N)
"""
