import math
from scipy.special import digamma

def Matrix(y,time_slices,T,lines):
    for i in range(0,len(lines)):
        sum=0
        t=0
        for a in range(0, T):
            sum = sum + time_slices[a]
            if (sum > i):
                t = a
                if (t == 0):
                    n = i
                else:
                    b = sum - time_slices[a]
                    n = i - b
                break
        for m in range(0,len(lines[i])-1):
            y[t,n,m]=lines[i][m]
    return y

def Iteration1(x1,x2,y,time_slices,T,lines):
    for t in range(0,T):
        for n in range(0,time_slices[t]):
            sum=0
            sum1=0
            sum2=0
            if(t==0):
                i=n
            else:
                for t1 in range(0, t):
                    sum = sum + time_slices[t1]
                i=sum+n
            for m in range(0,len(lines[i])-1):
                sum1=sum1+int(y[t,n,m])
                sum2=sum2+(1-int(y[t,n,m]))
            x1[t,n]=sum1/(m+1)
            x2[t,n]=sum2/(m+1)
    return x1,x2

def Iteration2(x1,x2,e1,a,b,c,d,time_slices,T):
    suma=0
    sumb=0
    sumc=0
    sumd=0
    for t in range(0,T):
        for n in range(0,time_slices[t]):
            suma=suma+e1[t,n]
            sumb=sumb+(1-e1[t,n])
            sumc=sumc+x1[t,n]*(1-e1[t,n])
            sumd=sumd+(1-e1[t,n])
    hat_a=a+suma
    hat_b=b+sumb
    hat_c=c+sumc
    hat_d=d+sumd
    return hat_a,hat_b,hat_c,hat_d
def Iteration3(x1,x2,hat_a,hat_b,hat_c,hat_d,time_slices,T):
    for t in range(0,T):
        for n in range(0,time_slices[t]):
            g = digamma(hat_b) - digamma(hat_a + hat_b) + x2[t, n] * (digamma(hat_c) - digamma(hat_c + hat_d))
            e1[t,n]=1-math.exp(g)
    return e1

def update_v(v,hat_v,T,variance_1,variance_2):
    for t in range(1,T):
        v[t]=(variance_2/(v[t-1]+variance_1+variance_2))*(v[t-1]+variance_1)
    hat_v[T-1]=v[T-1]
    for t in range(T-2,-1,-1):
        hat_v[t]=v[t]+pow(v[t]/(v[t]+variance_1),2)*(hat_v[t+1]-v[t]-variance_1)
    return v,hat_v

def update_m(m,hat_m,v,T,variance_1,variance_2):
    for t in range(1,T):
        m[t]=(variance_2/(v[t-1]+variance_1+variance_2))*m[t-1]+(1-(variance_2/(v[t-1]+variance_1+variance_2)))
    hat_m[T-1]=m[T-1]
    for t in range(T-2,-1,-1):
        hat_m[t]=(variance_1/(v[t]+variance_1))*m[t]+(1-(variance_1/(v[t]+variance_1)))*hat_m[t+1]
    return m,hat_m

def update_a0(a0,e0,hat_m,time_slices,x1,T):
    a0[0]=0.5
    for t in range(1,T):
        sum_e=0
        sum_ey=0
        for n in range(0,time_slices[t]):
            sum_e=sum_e+e0[t,n]
            sum_ey=sum_ey+e0[t,n]*x1[t,n]
        a0[t]=(variance_1*sum_ey)/pow(hat_m[t]-hat_m[t-1],2)
    return a0

def update_a1(a1,e0,hat_m,time_slices,x2,T):
    a1[0]=0.5
    for t in range(1,T):
        sum_e=0
        sum_ey=0
        for n in range(0,time_slices[t]):
            sum_e=sum_e+e0[t,n]
            sum_ey=sum_ey+e0[t,n]*x2[t,n]
        a1[t]=(variance_1*sum_ey)/pow(hat_m[t]-hat_m[t-1],2)
    return a1



if __name__ == "__main__":
    x1 = {}
    x2 = {}
    y = {}
    a0={}
    a1={}
    alpha={}
    e0 = {}
    e1 = {}
    e_0={}
    e_old={}
    T = 6
    time_slices = [1,1,1,1,1,1]
    lines = open('E:\SIGIR/01文件\魏则西事件.txt', 'r').readlines()
    a=b=c=d=0.5
    hat_a=a
    hat_b=b
    hat_c=c
    hat_d=d
    variance_1 = 0.005
    variance_2 = 0.5
    m = {}
    hat_m = {}
    v = {}
    hat_v = {}
    m[0] = 0
    v[0] = 5
    v, hat_v = update_v(v, hat_v, T, variance_1, variance_2)
    m, hat_m = update_m(m, hat_m, v, T, variance_1, variance_2)
    y=Matrix(y,time_slices,T,lines)
    x1,x2=Iteration1(x1,x2,y,time_slices,T,lines)
    MAX_ITERATION=100000
    for j in range(0,MAX_ITERATION):
        e1=Iteration3(x1,x2,hat_a,hat_b,hat_c,hat_d,time_slices,T)
        hat_a1,hat_b1,hat_c1,hat_d1=Iteration2(x1,x2,e1,a,b,c,d,time_slices,T)
        if(abs(hat_a1-hat_a)<=1e-6 and abs(hat_b1-hat_b)<=1e-6 and abs(hat_c1-hat_c)<=1e-6 and abs(hat_d1-hat_d)<=1e-6):
            break
        else:
            hat_a=hat_a1
            hat_b=hat_b1
            hat_c=hat_c1
            hat_d=hat_d1
        if(j==MAX_ITERATION-1):
            print('最大迭代次数！')
            break;
    r = []
    for t in range(0, T):
        for n in range(0,time_slices[t]):
            r.append(e1[t,n])
    min_e = min(r)
    max_e = max(r)
    distance = max_e - min_e
    e1_success = {}
    print('e:')
    for t in range(0, T):
        for n in range(0,time_slices[t]):
            e1_success[t,n] = ((e1[t,n] - min_e)/distance)*0.8+0.1
            print(1-e1_success[t,n])