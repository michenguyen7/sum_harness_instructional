#include <algorithm>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
#include <string.h>

int64_t result; // Global variable to store the result

void setup(int64_t N, uint64_t A[]) {
    // Log statement similar to code #2
    printf(" inside sum_indirect problem_setup, N=%lld \n", N);

    // Initialize the result to 0
    result = 0;

    // Set up the array with random values as in code #1
    for (int64_t i = 0; i < N; i++) {
        A[i] = lrand48() % N; // Randomly assign values between 0 and N-1
    }
}

int64_t sum(int64_t N, uint64_t A[]) {
    // Log statement similar to code #2
    printf(" inside sum_indirect perform_sum, N=%lld \n", N);

    // Use the logic from code #1 to perform the sum
    int64_t indx = A[0]; // Start from the first element of the array
    for (int64_t i = 0; i < N; i++) {
        result += indx; // Accumulate the sum
        indx = A[indx]; // Move to the next index using the value in A
    }

    // Return the computed result
    return result;
}