#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cond1(vector <int> &, int);
bool cond2(vector <int> &, int);

bool cond1(vector<int> &list1, int i){
    if(i == 0)
        return cond2(list1,i);
    int cur = list1[i];
    for (int j = 0; j < i; j++)
        if(cur <= list1[j])
        return false;
    return true;
}

bool cond2(vector<int> &list1, int i){
    if(i == list1.size()-1)
        return cond1(list1,i);
    if(list1[i] <= list1[i+1])
        return false;
    return true;
}


int main(){
    vector<int> l1;
    int caseno = 1, res = 0;
    int tc;
    cin >> tc;
    while(tc){
        int N,data;
        cin >> N;
        for(int i = 0; i < N; i++){
            cin >> data;
            l1.push_back(data);
        }
        for(int i = 0; i < l1.size(); i++){
            if(cond1(l1,i) && cond2(l1,i))
                res++;
        }
        cout << "Case #" << caseno << ": " << res << endl;
        caseno++;
        tc--;
    }

}
