#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#include "binlog.h"

int binlog_fd = -1;


int log_init() {
    if (binlog_fd != -1) {
        fprintf(stderr, "binlog is already initialized\n");
        return 1;
    }

    binlog_fd = open("log.bin", O_RDWR | O_CREAT, S_IRUSR | S_IWUSR | S_IRGRP | S_IWGRP | S_IROTH);
    lseek(binlog_fd, 0, SEEK_END);
    return 0;
}


int log_close() {
    if (binlog_fd == -1) {
        fprintf(stderr, "please call log_init() before using binlog\n");
        return 1;
    }

    fsync(binlog_fd);
    close(binlog_fd);
    binlog_fd = -1;
    return 0;
}


int log_write_solution(int n, int *solution) {
    if (binlog_fd == -1) {
        fprintf(stderr, "please call log_init() before using binlog\n");
        return 1;
    }

    write(binlog_fd, solution, sizeof(int) * n);
    write(binlog_fd, &n, sizeof(int));
    fsync(binlog_fd);
    return 0;
}


int log_read_solution(int *n, int **solution) {
    size_t solution_size;

    if (binlog_fd == -1) {
        fprintf(stderr, "please call log_init() before using binlog\n");
        return 1;
    }

    if (lseek(binlog_fd, -sizeof(int), SEEK_END) < 0) {
        return 1;
    }
    if (read(binlog_fd, n, sizeof(int)) != sizeof(int)) {
        return 1;
    }

    solution_size = sizeof(int) * (*n);
    *solution = malloc(solution_size);
    if (lseek(binlog_fd, -(sizeof(int) + solution_size), SEEK_END) < 0) {
        return 1;
    }
    if (read(binlog_fd, *solution, solution_size) != solution_size) {
        return 1;
    }

    lseek(binlog_fd, 0, SEEK_END);
    return 0;
}
