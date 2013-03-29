#include "euler.h"
#include "xint.h"
using namespace std;
int main()
{
	xint b(8);
	if(b.isPrime())
		cout<<"b is prime"<<endl;
	else
		cout<<"b is not prime"<<endl;
	/*problem_1_25 a;
	cout<<a.problem_3()<<endl;*/
	return 0;
}