class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        b=[]
        d=""
        cc=[]
        f=[]
        for i in range(len(paths)):
            c=list(paths[i].split(" "))
            d=c[0]
            for y in range(1,len(c),+1):
                c[y]=list(c[y].split("("))
                if c[y][1] not in cc:
                    cc.append(c[y][1])
                    d+="/"+c[y][0]
                    f.append(d)
                    b.append(f)
                    f=[]
                    d=c[0]
                else:
                    d+="/"+c[y][0]
                    b[cc.index(c[y][1])].append(d)
                    d=c[0]
        z=0
        w=0
        while(z==0):
            if len(b[w])==1:
                b.pop(w)
            else:
                w+=1
            if w==len(b):
                z=1
        return b
