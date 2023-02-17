## PROCESSES

A parent process can be forked to create a child process using `fork()`.

- A parent process has PID > 0
- A child process has PID = 0 when it is running, that is how we can identify it.

### ZOMBIE PROCESS

A zombie process is when the proces is when the process but is still present in the process table. This can be achieved when we have an `exit(0)` at the end of the child process and a `sleep()` at the end of the parent process.

```cpp
pid_t p = fork();
if(p == 0) {
	exit(0);
}
else if(p > 0) {
	sleep(50);
}
```

The parent process sleeps for 50 seconds after the child process terminates, so it does not get the status of the child process and hence for those sleep time, the child process remains in the process table despite being already executed and terminated.
