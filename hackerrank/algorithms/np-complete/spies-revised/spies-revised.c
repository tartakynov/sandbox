#include <stdlib.h>
#include <stdio.h>
#include <time.h>

/*
https://www.hackerrank.com/challenges/spies-revised/problem
Trying to solve with hill climbing technique, although it's very slow with bigger N
*/

static inline void swap(int *solution, int first, int second) {
    int tmp;
    tmp = solution[first];
    solution[first] = solution[second];
    solution[second] = tmp;
}

/**
 * Check if three points are collinear
 */
static inline int are_collinear(int x1, int y1, int x2, int y2, int x3, int y3) {
    return (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2);
}

/**
 * Check if the line between the two points is at a 45 degree angle to the horizontal
 */
static inline int are_diagonal(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) == abs(y1 - y2);
}

/**
 * Init random solution
 */
void random_solution(int n, int *solution) {
    int i, j;

    for (i = 0; i < n; i++) {
        solution[i] = i;
    }

    for (i = 0; i < n; i++) {
        j = rand() % n;
        swap(solution, i, j);
    }
}

/**
 * Total number of blown covers
 */
int number_of_blown_covers(int n, int *solution) {
    int count;
    int x1, x2, x3;

    count = 0;
    for (x1 = 0; x1 < n; x1++) {
        for (x2 = x1 + 1; x2 < n; x2++) {
            if (are_diagonal(x1, solution[x1], x2, solution[x2]) == 1) {
                count++;
            }

            for (x3 = x2 + 1; x3 < n; x3++) {
                if (are_collinear(x1, solution[x1], x2, solution[x2], x3, solution[x3]) == 1) {
                    count++;
                }
            }
        }
    }

    return count;
}

/**
 * Runs until solution is found (though it can stuck at a local optima)
 */
int hill_climber(int n, int *solution) {
    int current_score, next_score, i, j;

    random_solution(n, solution);
    current_score = number_of_blown_covers(n, solution);
    while (current_score > 0) {
        for (i = 0; i < n; i++) {
            for (j = i + 1; j < n; j++) {
                swap(solution, i, j);
                next_score = number_of_blown_covers(n, solution);
                if (next_score < current_score) {
                    current_score = next_score;
                    printf("score = %d\n", current_score);
                } else if (current_score == next_score) {
                    if (rand() % 2 == 0) {
                        swap(solution, i, j);
                    }
                } else {
                    swap(solution, i, j);
                }
            }
        }
    }

    return current_score;
}

int main(void) {
    int n, score;
    int *solution;

    srand(time(NULL));
    n = 199;
    solution = malloc(n * sizeof(int));
    score = hill_climber(n, solution);
    printf("n = %d, score = %d\n", n, score);
    for (int i = 0; i < n; i++) {
        printf("%d ", solution[i] + 1);
    }

    printf("\n");

    free(solution);
    return 0;
}