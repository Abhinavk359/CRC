#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cin>>n;
  int a[n];
  for(int i=0;i<n;i++)
  {
    cin>>a[i];
  }
  vector<int> prefix_sum(a.begin(),a.end());
  long long sum=0;
  for(int i=1;i<n;i++)
  {
    sum+=(i*a[i]-prefix_sum[i-1]);
  }
  cout<<sum<<endl;
