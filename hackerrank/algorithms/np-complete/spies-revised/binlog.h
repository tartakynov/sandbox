/*
The binary log contains solution transitions so that the app can continue working on the solution after restart
*/

extern int binlog_fd;

struct solution_header {
    int n;
    int score;
};

int log_init();

int log_close();

int log_write_solution(int score, int n, int *solution);

int log_read_solution(int *score, int *n, int **solution);

