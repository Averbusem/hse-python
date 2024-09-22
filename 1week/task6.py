"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=string&difficulty=MEDIUM
"""


class Solution(object):
    def simplifyPath(self, path):
        path_list = path.split("/")
        stack = []
        for s in path_list:
            if s == "." or s == "":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        res = "/" + "/".join(stack)
        return res


sol = Solution()
print(sol.simplifyPath("/.../a/../b/c/../d/./"))
#                      /.../b/d
print(sol.simplifyPath("/../"))
