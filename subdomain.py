class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        p=[]
        num=[]
        for i in range(len(cpdomains)):
            li=cpdomains[i]
            li=list(li.split(" "))
            if li[1] not in p:
                p.append(li[1])
                num.append(int(li[0]))
            else:
                num[p.index(li[1])]+=int(li[0])
                
            while("." in li[1]):
                sub=li[1][li[1].index(".")+1:]
                li[1]=list(li[1])
                li[1].remove(".")
                li[1]="".join(li[1])
                if sub not in p:
                    p.append(sub)
                    num.append(int(li[0]))
                else:
                    num[p.index(sub)]+=int(li[0])
        for i in range(len(p)):
            p[i]=str(num[i])+ ' ' + p[i]
        return p
