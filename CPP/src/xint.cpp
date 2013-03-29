#include "xint.h"
#include <cmath>
#include <iostream>
xint::xint(__int64 x_int)
{
	x_integer=x_int;
}
bool xint::isPrime()
{	
	if(x_integer<=0)
		return false;
	else if(x_integer==2)
		return true;
	else if(x_integer%2==0)
		return false;
	else
	{
		__int64 i=3;
		while(i<sqrt(x_integer))
		{
			if(x_integer%i==0)
				return false;
			i+=2;
		}
		return true;
	}
}