class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if stack:
                if char == "*":
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        return "".join(stack)

if __name__ == '__main__':
    string = "leet**cod*e"
    solution = Solution()
    print(solution.removeStars(string))
