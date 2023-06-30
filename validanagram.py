class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            f=list(s)
            g=list(t)
            while len(f)>0:
                if (f[0] in g):
                    g.remove(f[0])
                    f.pop(0)
                else:
                    return False
            return True
        else:
            return False
        
