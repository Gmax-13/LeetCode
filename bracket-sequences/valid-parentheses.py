class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:  # If it's an opening bracket
                stack.append(char)

        return not stack  # Stack should be empty if all brackets are matched

# Example usage:
solution = Solution()
print(solution.isValid("()"))       # True
print(solution.isValid("()[]{}"))   # True
print(solution.isValid("(]"))       # False
print(solution.isValid("([])"))     # True
