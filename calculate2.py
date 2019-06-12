from fractions import Fraction
import random
import cProfile
import time
def newint():
    sym=['+','-','×','÷']  
    fh=random.randint(0,3) #随机产生所需运算符号
    #随机产生运算数
    n1=random.randint(1,20)  
    n2=random.randint(1,20)
    result=0
    if fh == 0:   #产生的随机数对应四则运算，下同
        result=n1+n2
    elif fh == 1:
        n1,n2=max(n1,n2),min(n1,n2)  #避免出现负数，将n1设为更大值
        result=n1-n2
    elif fh == 2:
        result=n1*n2
    elif fh == 3:
        n1,n2=max(n1,n2),min(n1,n2) #避免除数为分数，将n1设为更大值
        while n1%n2 !=0:  #避免除数为0，运算不符合规则
            n1=random.randint(1,10)
            n2=random.randint(1,10)
            n1,n2=max(n1,n2),min(n1,n2)
        result=int(n1/n2)
    print(n1,sym[fh],n2,'=',end=' ')  #显示结果
    return result

def newfra():
    sym=['+','-','×','÷']
    fh=random.randint(0,3)
    t1=random.randint(1,10)
    t2=random.randint(t1,10)  #由t2开始产生随机数，确保t1比t2小，得到分数，下同
    n1=Fraction(t1,t2)
    t1=random.randint(1,10)
    t2=random.randint(t1,10)
    n2=Fraction(t1,t2)
    result=0
    if fh == 0:
        result=n1+n2
    elif fh == 1:
        n1,n2=max(n1,n2),min(n1,n2) #避免出现负数，将n1设为更大值
        result=n1-n2
    elif fh == 2:
        result=n1*n2
    elif fh == 3:
        n1,n2=max(n1,n2),min(n1,n2) 
        result=n1/n2
    print(n1,sym[fh],n2,'=',end=' ')    #显示结果
    return result

def newtest():
    sym=['+','-','×','÷']
    n=int(input())  #输入题目总数量
    result=[]   #寄存结果
    m=0
    while m<=(n-1):
        fh = random.randint(0,5)
        if fh ==0:  #随机数由0到5，计算分数和整数出现的比例1:5
            print(m+1,end='、')
            result.append(newfra())
            print(' ')
        else:
            print(m+1,end='、')
            result.append(newint())
            print(' ')
        m = m + 1   #标记题目数量，达到题目设置量时退出循环
    m=0
    print('答案:')
    while m <=(n-1):
          print(m+1,'、',result[m])  #此时的m为标记第几题
          m = m + 1


def main():
    print('1、四则运算')
    print('2、制作题库')
    n=int(input())
    if n == 1:      
        print('input"0000"to Quit')
        while True:
            fh = random.randint(0,5)   
            if fh == 0: #随机数由0到5，计算分数和整数出现的比例1:5
                result=newfra()
                jg=input()
                if jg == '0000':
                    break;
                ans = Fraction(jg)  #结果显示为分数
                if ans == result:
                    print('right')  #显示结果是否正确，下同
                else:
                    print('error,the right answer is',result)   
            else:
                result= newint()
                jg = input()
                if jg == '0000':
                    break;
                ans = Fraction(jg)
                if ans == result:
                    print('right')
                else:
                    print('error,the right answer is',result)
    if n==2:
        print('需要制作多少道题目：')
        newtest()

if __name__=='__main__':
    main()
          
