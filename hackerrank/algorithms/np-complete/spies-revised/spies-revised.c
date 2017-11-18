#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <string.h>
#include <errno.h>
#include <math.h>

#include "binlog.h"

/*
https://www.hackerrank.com/challenges/spies-revised/problem
Trying to solve with hill climbing or simulated anneal techniques, although it's very slow with bigger N
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
        j = (int) (random() % n);
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

    current_score = number_of_blown_covers(n, solution);
    printf("score = %d\n", current_score);

    while (current_score > 0) {
        for (i = 0; i < n; i++) {
            for (j = i + 1; j < n; j++) {
                swap(solution, i, j);
                next_score = number_of_blown_covers(n, solution);
                if (next_score < current_score) {
                    current_score = next_score;
                    printf("score = %d\n", current_score);
                    log_write_solution(n, solution);
                } else if (current_score == next_score) {
                    if (random() % 2 == 0) {
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

/**
 * Runs until solution is found
 */
int simulated_anneal(int n, int *solution) {
    double temperature, epsilon, flip, alpha;
    int i, j;
    int current_score, delta;

    alpha = 0.999;
    epsilon = 0.001;
    temperature = 400.0;
    current_score = number_of_blown_covers(n, solution);
    while (temperature > epsilon && current_score > 0) {
        i = (int) (random() % n);
        j = (int) (random() % n);
        swap(solution, i, j);
        delta = number_of_blown_covers(n, solution) - current_score;
        if (delta < 0) {
            current_score += delta;
            printf("temperature = %.5f, score = %d\n", temperature, current_score);
        } else {
            flip = ((double) random()) / RAND_MAX;
            if (exp(-delta / temperature) > flip) {
                current_score += delta;
            } else {
                swap(solution, i, j);
            }
        }

        temperature *= alpha;
    }

    return current_score;
}

int main(int argc, char* argv[]) {
    int n, i, score;
    int *solution;

    if (argc != 2) {
        printf("Usage: %s N or -c or --continue\n", argv[0]);
        return -1;
    }

    srand((unsigned int) time(NULL));
    log_init();
    if (strcmp(argv[1], "-c") == 0 || strcmp(argv[1], "--continue") == 0) {
        if (log_read_solution(&n, &solution) != 0) {
            printf("failed to read binlog\n");
            return 1;
        }

        printf("n = %d\n", n);
    } else {
        errno = 0;
        n = (int) strtol(argv[1], NULL, 0);
        if (errno) {
            printf("error parsing N\n");
            return 1;
        }

        solution = malloc(n * sizeof(int));
        random_solution(n, solution);
    }

    score = hill_climber(n, solution);
    printf("n = %d, score = %d\n", n, score);
    for (i = 0; i < n; i++) {
        printf("%d ", solution[i] + 1);
    }

    printf("\n");
    log_close();
    free(solution);
    return 0;
}
