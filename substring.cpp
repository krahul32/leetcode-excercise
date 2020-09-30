#include <iostream>
#include <functional>
#include <string>
#include <vector>
#include <list>
#include <cmath>
using namespace std;

int charhash(char c)
{
    hash<char> hash_val;
    return hash_val(c);
}

int main()
{
    string s = "abcde";
    string t = "aec";
    while(t.length() != 0)
    {
        cout << '\n' << "Hash Value: "<< charhash(t.back());
        t.pop_back();
    }
}
