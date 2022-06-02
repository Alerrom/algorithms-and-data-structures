#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int h(long long int x) 
{
	return x % 100000;
}

int main() 
{
	freopen("set.in", "r", stdin);
	freopen("set.out", "w", stdout);

	string command;
	vector <long long int> array[100000];

	while (cin >> command)
	{

		long long int value;
		cin >> value;

		if (command == "insert")
		{
			int flag;
			for (int i = 0; i < sizeof(array[h(value)]); i++)
			{
				if (array[h(value)][i] == value)
				{
					flag = 1;
					break;
				}
				else
				{
					flag = 0;
				}
			}
			if (flag == 0)
			{
				array[h(value)].push_back(value);
			}
		}

		if (command == "exists")
		{
			int flag;
			for (int i = 0; i < sizeof(array[h(value)]); i++)
			{
				if (array[h(value)][i] == value)
				{
					flag = 1;
					break;
				}
				else
				{
					flag = 0;
				}
			}
			if (flag == 1)
			{
				cout << "true";
			}
			else
			{
				cout << "false";
			}
		}

		if (command == "delete")
		{
			for (int i = 0; i < sizeof(array[h(value)]); i++)
			{
				if (array[h(value)][i] == value)
				{
					array[h(value)][i] = NULL;
					break;
				}
			}
		}
	}

	return 0;
}