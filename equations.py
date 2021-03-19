def power(x,n):
    answer=1.0
    for i in range(int(n)):
        answer=answer*x
    return answer

def azeret(n):
    answer3=1.0
    for i in range(1, int(n)+1):
        answer3=answer3*i
    return answer3

def exponent(marih):
    answer2=0.0
    for i in range (0,100):
        answer2=answer2+(power(marih,i))/(azeret(i))
    return answer2

def Ln(x):
    try:
        if (x<=0):
            return (0.0)
        else:
            yn=0
            result=x-1.0
            while ((yn-result)>0.001 or (result-yn)>0.001):
                yn=result
                result=result+2*((x-exponent(result))/(x+exponent(result)))
            return result
    except:
        return(0.0)
    
def XtimesY(x:float,y:float) -> float:
    try:
        if(x<=0):
            return (0.0)
        else:
           a=exponent(Ln(x)*y)
           return float('%0.6f' %a)
    except:
        return(0.0)

def sqrt(x:float,y:float) -> float:
    try:
        if (y>0 and x!=0):
            x=1/x
            a=(XtimesY(y,x))
            return float('%0.6f' %a)
        else:
            return(0.0)
    except:
        return (0.0)
        
def calculate(x):
    try:
        if(x<=0):
            return(0.0)
        answer4=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
        b=float('%0.6f' %answer4)
        return b
    except:
        return (0.0)
#try:
    #num1=input ('enter a num1: ')
    #num2=input ('enter a num2: ')
    #x=float(num1)
    #y=float(num2)
    #print(calculate(x))
    #print(XtimesY(x,y))
    #print(sqrt(x,y))
#except:
    #print(0.0)