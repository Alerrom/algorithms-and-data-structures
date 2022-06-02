#include <stdio.h>

void k_statistic(int* array, int left, int right, int k) {
    if (left >= right) {
        return;
    }

    int flag = 0;
    for (int i = left + 1; i <= right; i++) {
        if (array[i] != array[i - 1]) {
            flag = 1;
            break;
        }
    }

    if (flag == 0) {
        return;
    }

    int pivot = array[right];

    int j = left;
    for (int i = left; i < right; i++) {
        if (array[i] < pivot) {
            int tmp = array[i];
            array[i] = array[j];
            array[j] = tmp;
            j++;
        }
    }

    array[right] = array[j];
    array[j] = pivot;

    int pivot_index = j;
    j++;

    while (j <= right && array[j] == array[j - 1]) {
        j++;
    }  

    if (k >= pivot_index && k <= j - 1) {
        return;
    }

    if (k < pivot_index) {
		k_statistic(array, left, pivot_index - 1, k);
    }
    else {
		k_statistic(array, j, right, k);
    }
}

int main() {
    FILE* in = fopen("kth.in", "r");
    FILE* out = fopen("kth.out", "w");

    int n, k, A, B, C, a_1, a_2;
    fscanf(in, "%d %d", &n, &k);
    fscanf(in, "%d %d %d %d %d", &A, &B, &C, &a_1, &a_2);

    int* array = (int*)malloc(n * sizeof(int));
    array[0] = a_1;
    array[1] = a_2;

    for (int i = 2; i < n; i++) {
        array[i] = array[i - 2] * A + array[i - 1] * B + C;
    }

	k_statistic(array, 0, n - 1, k - 1);

    fprintf(out, "%d", array[k - 1]);
    fclose(in);
    fclose(in);

	return 0;
}