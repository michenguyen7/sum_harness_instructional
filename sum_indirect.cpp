#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

int64_t result;

void setup(int64_t N, uint64_t A[]) {
    std::cout << "Inside setup, N = " << N << std::endl;
    result = 0;

    for (int64_t i = 0; i < N; i++) {
      A[i] = lrand48() % N;
    }
}

int64_t sum(int64_t N, uint64_t A[]) {
    int64_t indx = A[0];
    for (int64_t i = 0; i < N; i++) {
        result += indx;
        indx = A[indx];
    }
    return result;
}

