#include "problem_1_25.h"


int problem_1_25::problem_1()
{
	int i_sum=0;
	for(int i=1;i<1000;i++)
	{
		if(i%3==0||i%5==0)
			i_sum+=i;
	}
	return i_sum;
}
int problem_1_25::problem_2()
{
	int i_sum=0;
	int fib=1;
	int a=1;
	int b=2;
	while(fib<4000000)
	{
		fib=a+b;
		a=b;
		b=fib;
		if(fib%2==0)
			i_sum+=fib;
	}
	return i_sum;
}
__int64 problem_1_25::problem_3()
{
	__int64 a=600851475143;
	int i=3;
	while(i<a)
	{
		while(a%i==0)
			a/=i;
		i+=2;
	}
	return i;
}