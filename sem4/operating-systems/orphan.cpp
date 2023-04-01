#include <unistd.h>
#include <iostream>
#include <algorithm>
#include <stdlib.h>


/* parent subroutine */
int parentMaxVal( int *arr, int n ) {
	int maxVal = arr[0];
	for( int i = 0; i < n; i++ ) {
		maxVal = std::max( maxVal, arr[i] );
	}
	return maxVal;
}

/* child subroutine */
int childMinVal( int *arr, int n ) {
	int minVal = arr[0];
	for( int i = 0; i < n; i++ ) {
		minVal = std::min( minVal, arr[i] );
	}
	return minVal; 
}

/* driver main function */
int main( int argc, char **argv ) {
	if( argc != 2 ) {
		std::cout << "USAGE: ./orp <arraySize" << std::endl;
		exit(0);
	}

	/* array input */
	int n = atoi(argv[1]);
	int arr[n];
	for( int i = 0; i < n; i++ ) {
		std::cout << "arr[" << i << "]: ";
		std::cin >> arr[i];
	}

	/* creating childs */
	pid_t pid = fork();

	/* making orphan process */
	if( pid < 0 ) {
		std::cout << "[ERROR] Process creation failed" << std::endl;
	}
	else if( pid > 0 ) {
		std::cout << "PARENT PROCESS RUNNING WITH PID " << getpid() << std::endl;
		std::cout << "MAX VALUE: " << parentMaxVal( arr, n ) << std::endl << std::endl;
	}
	else if( pid == 0 ) {
		sleep(4);
		std::cout << "CHILD PROCESS RUNNING WITH PID " << getpid()
			<< "\nWITH PARENT PID " << getppid() << std::endl;
		std::cout << "MIN VALUE: " << childMinVal( arr, n ) << std::endl << std::endl;
	}
	return 0;
}

