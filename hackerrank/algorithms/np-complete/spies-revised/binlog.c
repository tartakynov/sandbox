#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <time.h>

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

    if (fsync(binlog_fd) < 0) {
        fprintf(stderr, "error syncing binlog\n");
        return 1;
    }

    close(binlog_fd);
    binlog_fd = -1;
    return 0;
}


int log_write_solution(int n, int *solution) {
    int size;

    if (binlog_fd == -1) {
        fprintf(stderr, "please call log_init() before using binlog\n");
        return 1;
    }

    size = sizeof(int) * n;
    if (write(binlog_fd, solution, size) != size) {
        fprintf(stderr, "unable to write %d bytes into the binlog file\n", size);
        return -1;
    }

    size = sizeof(int);
    if (write(binlog_fd, &n, size) != size) {
        fprintf(stderr, "unable to write %d bytes into the binlog file\n", size);
        return -1;
    }

    if (fsync(binlog_fd) < 0) {
        fprintf(stderr, "error syncing binlog\n");
        return 1;
    }

    return 0;
}


int log_read_solution(int *n, int **solution) {
    int header_size, solution_size;

    if (binlog_fd == -1) {
        fprintf(stderr, "please call log_init() before using binlog\n");
        return 1;
    }

    header_size = sizeof(int);
    lseek(binlog_fd, -header_size, SEEK_END);

    if (read(binlog_fd, n, header_size) != header_size) {
        fprintf(stderr, "failed to read (1) from binlog\n");
        return 1;
    }

    solution_size = sizeof(int) * (*n);
    *solution = malloc(solution_size);
    lseek(binlog_fd, -(header_size + solution_size), SEEK_END);

    if (read(binlog_fd, *solution, solution_size) != solution_size) {
        fprintf(stderr, "failed to read (2) from binlog\n");
        return 1;
    }

    lseek(binlog_fd, 0, SEEK_END);

    return 0;
}
