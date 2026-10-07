#include<iostream>
using namespace std;
 
int main()
{
    int n;
    cin>>n;
    cout<<((n%2==0 && n>2) ?  "Yes" : "No")<<endl;
    return 0;
}