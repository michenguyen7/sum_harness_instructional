#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>



int64_t result;

void setup(int64_t N, uint64_t A[]) {
    printf(" inside vector_sum problem_setup, N=%lld \n", N);
    result = 0;
    for (int64_t i = 0; i < N; i++) {
        A[i] = i;
    }
}

int64_t sum(int64_t N, uint64_t A[]) {
    printf(" inside vector_sum problem_sum, N=%lld \n", N);
    for (int64_t i = 0; i < N; i++) {
        result += A[i];
    }
    return result;
}

