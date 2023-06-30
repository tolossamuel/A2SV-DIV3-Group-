import textwrap

def wrap(string, max_width):
    p=""
    
    while(len(string)>0):
        try:
            p+=string[:max_width]+"\n"
            string=string[max_width:]
        except:
            
            p+=(string)
            p+="\n"
            print(p)
            string =""
            
    return p

if __name__ == '__main__':
