class Solution:
    def helper(self, s, start, path, ans):
        rem_len = len(s) - start
        rem_parts = 4 - len(path)

        # pruning
        if rem_len > 3 * rem_parts or rem_len < rem_parts:
            return

        # end condition
        if len(path) == 4:
            if start == len(s):
                ans.append(".".join(path))
            return

        num = 0
        for i in range(3):  # max 3 digits
            if start + i >= len(s):
                break

            # leading zero check
            if i > 0 and s[start] == '0':
                break

            num = num * 10 + int(s[start + i])

            if num > 255:
                break

            path.append(str(num))
            self.helper(s, start + i + 1, path, ans)
            path.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.helper(s, 0, [], ans)
        return ans
