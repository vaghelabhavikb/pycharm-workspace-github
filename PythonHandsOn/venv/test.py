
class Solution(object):
    def isValid(self, s):
        l = len(s)
        d = {}
        for i in range(0,l,1):
            if (s[i] != " "):
                if d.get(s[i])==None:
                    d[s[i]] = 1
                else:
                    d[s[i]] = d.get(s[i]) + 1
        return d


if __name__ == '__main__':
    print(Solution().isValid("ABHISHEK BAHADUR SINGH"))
