''' Problem description: https://leetcode.com/problems/longest-common-prefix/description/ '''


class Solution:
	def longestCommonPrefix(self, strs: list[str]) -> str:

		if len(strs) == 0:
			return ''

		strs.sort()

		answer = ''
		for i in range(min(len(strs[0]), len(strs[len(strs) - 1]))):
			if strs[0][i] == strs[len(strs) - 1][i]:
				answer += strs[0][i]
			else:
				break

		return answer
