#include <fstream>
#include <vector>
using namespace std;

struct Tree {
	long long k;
	int l;
	int r;
};

bool Flag = true;
vector<Tree> my_tree;

void check(int v, long long min, long long max) {
	if (my_tree[v].k <= min || my_tree[v].k >= max) {
		Flag = false;
	}

	if (my_tree[v].l != 0) {
		check(my_tree[v].l, min, my_tree[v].k);
	}

	if (my_tree[v].r != 0) {
		check(my_tree[v].r, my_tree[v].k, max);
	}
}

int main() {
	ifstream fin("check.in");
	ofstream fout("check.out");

	int n;
	fin >> n;

	if (n == 0){
		fout << "YES";
	}
	else {
		my_tree.resize(n + 1);/*чтобы нумерация шла от 1 до n, 
		а не от 0 до n-1*/

		for (int i = 1; i <= n; i++) {
			fin >> my_tree[i].k >> my_tree[i].l >> my_tree[i].r;
		}

		check(1, -1000000001, 1000000001);

		if (Flag) {
			fout << "YES";
		}
		else {
			fout << "NO";
		}
	}
}