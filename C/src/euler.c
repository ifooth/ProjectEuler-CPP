#include <stdio.h>
#include "euler.h"

int main()
{
    problem3();
    printf("\n");
    return 0;
}

int problem1()
{
    int sum=0,i;
    for(i=3;i<1000;i++)
    {
        if(i%3==0||i%5==0)
            sum+=i;
    }
    printf("sum=%d",sum);
    return 0;
}
int problem2()
{
    int fib=3,a=1,b=2;
    int sum=2;
    //printf("1,2,3");
    while(fib<=4000000)
    {        
        a=b;
        b=fib;
        fib=a+b;        
        //printf(",%d",fib);
        if(fib%2==0)
            sum+=fib;
    }
    printf("sum=%d",sum);
    return 0;
}
int problem3()
{
    long long n=60085147514378,factor=2,temp;
    printf("%lld=",n);
    while(n!=1)
    {
        temp=0;
        while(n%factor==0)
        {
            temp++;
            n/=factor;
        }
        if(temp>0)
            printf("%lld^%lld * ",factor,temp);
        factor+=1;
    }    
    return 0;    
}

int isPrime(long long int num)
{
    if(num%2==0||num%3==0||num%5==0)
        return 0;
    for(int i=7;i*i<num;i+=5)
    {
        if(num%i==0)
        {
            return 0;
        }
    }
    return 1;
}

        
