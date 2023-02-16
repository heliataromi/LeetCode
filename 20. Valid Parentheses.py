''' Problem description: https://leetcode.com/problems/valid-parentheses/description/ '''


class Solution:
	def isValid(self, s: str) -> bool:
		brackets = {
			')': '(',
			']': '[',
			'}': '{'
		}
		temp = []

		for bracket in s:

			if bracket in brackets.keys():
				if len(temp) == 0:
					return False

				if temp[-1] != brackets[bracket]:
					return False

				temp = temp[:-1]

			if bracket in brackets.values():

				temp.append(bracket)

		if len(temp) != 0:
			return False

		return True
