//#include <cmath>
//#include <iostream>
//
//using namespace std;
//
//int main()
//{
//    int n;
//    cin >> n;
//    int a[105];
//    for(int i = 0;i < n; ++i)
//    {
//        cin >> a[i];
//    }
//
//    int sum = 0;
//    for(int i =0;i < n; ++i)
//    {
//        sum += a[i];
//    }
//
//    if(sum % n !=0)
//    {
//        cout << -1 << endl;
//        return 0;
//    }
//
//    int avg = sum / n;
//
//    int all_ = 0;
//    for(int i =0; i<n; ++i)
//    {
//        int tmp = abs(a[i]-avg);
//        all_ += tmp;
//        if (tmp % 2 != 0)
//        {
//            cout << -1 << endl;
//            return 0;
//        }
//
//    }
//
//    cout << all_/4 << endl;
//    return 0;
//}


//#include <cmath>
//#include <iostream>
//#include <cstdlib>
//#include<cstdio>
//using namespace std;
//
//int main()
//{
////freopen("/home/user/Disk1.8T/unicoe_notebook/c++_learn/dododo/in.txt","r", stdin);
//
//long long in;
//cin >> in;
//
//for(long long i = sqrt(in)+1; i >= 0; --i)
//{
//    if(i*i+i <= in)
//    {
////        cout << i*i+i<< endl;
////        cout << in << endl;
//        cout << i;
//        break;
//    }
//}
//
//return 0;
//}


///用dfs列举所有子串，来查找结果。

//#include <cmath>
//#include <iostream>
//#include <cstdlib>
//#include<cstdio>
//#include <cstring>
//using namespace std;
//
//char str1[15];
//char str2[15];
//int vis[15];
//
//int cnt = 0;
//int flag = 0;
//
//void dfs(int idx, int cur, char* tmp)
//{
//    if(idx == strlen(str1))
//        return;
//
//    vis[idx] = 1;
//    tmp[cur] = str1[idx];
//    tmp[cur+1] = '\0';
//    cnt += 1;
//
//    if (strcmp(tmp, str2) == 0)
//    {
//        flag = 1;
//        return;
//    }
//    vis[idx] = 0;
//
//    for(int i = idx+1; i < strlen(str1); ++i)
//    {
//        if(!vis[i])
//        {
//            vis[i] = 1;
//            dfs(i, cur+1, tmp);
//            vis[i] = 0;
//        }
//    }
//}
//
//
//int main()
//{
////freopen("/home/user/Disk1.8T/unicoe_notebook/c++_learn/dododo/in.txt","r", stdin);
////freopen("/home/user/Disk1.8T/unicoe_notebook/c++_learn/dododo/out.txt","w", stdout);
//
//
//cin >> str1 >> str2;
////cout << str1 << endl << str2;
//int len1 = strlen(str1);
//int len2 = strlen(str2);
//
//for(int i = 0; i < len1; ++i)
//{
//    char tmp[15] = "";
//    memset(vis, 0, sizeof(vis));
//    dfs(i, 0, tmp);
//}
//
//
//if(flag == 1)
//    cout << "Yes" << endl;
//else
//    cout << "No" << endl;
//return 0;
//}


#include<iostream>
#include<string>
#include <cstdlib>
#include<cstdio>
using namespace std;

int main()
{
freopen("/home/user/Disk1.8T/unicoe_notebook/c++_learn/dododo/in.txt","r", stdin);
freopen("/home/user/Disk1.8T/unicoe_notebook/c++_learn/dododo/out.txt","w", stdout);
//
string str;

while(cin >> str)
{
    string str1;
    cin >> str1;

    int a = 0, b = 0;


while(a < str.length())
{
    if(str[a] == str1[b])
        a++,b++;
}

if(b == str1.length())
    cout << "Yes" << endl;
else
    cout << "No" << endl;
}
return 0;
}


