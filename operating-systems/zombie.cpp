#include <iostream>
#include <unistd.h>
#include <algorithm>
#include <stdlib.h>


/* parent subroutine */
int parentMaxValue( int *arr, int n ) {
	int maxVal = arr[0];
	for( int i = 0; i < n; i++ ) {
		maxVal = std::max( maxVal, arr[i] );
	}
	return maxVal;
}

/* child subroutine */
int childMinValue( int *arr, int n ) {
	int minVal = arr[0];
	for( int i = 0; i < n; i++ ) {
		minVal = std::min( minVal, arr[i] );
	}
	return minVal;
}

/* driver main function */
int main( int argc, char **argv ) {
	if( argc != 2 ) {
		std::cout << "USAGE: ./zmb <arraySize>" << std::endl;
		exit(0);
	}
	
	/* get user input */ 
	int n = atoi(argv[1]);
	int arr[n];
	for( int i = 0; i < n; i++ ) {
		std::cout << "arr[" << i << "]: ";
		std::cin >> arr[i];
	}

	/* creating processes */
	pid_t pid = fork();
	
	/* creating zombie processes */
	if( pid < 0 ) {
		std::cout << "[ERROR] Process creation failed" << std::endl;
	}
	else if( pid > 0 ) {
		std::cout << "PARENT PROCESS RUNNING WITH PID " << getpid() << std::endl;
		std::cout << "MAX VALUE: " << parentMaxValue( arr, n ) << std::endl << std::endl;
		/* parent is put to sleep so that
		 * it does not recieve the return code of
		 * the child even when it has terminated
		 * threby creating a zombie process*/
		sleep(20);
	}
	else if( pid == 0 ) {
		std::cout << "CHILD PROCESS RUNNING WITH PID " << getpid()
			<< "WITH PARENT PID " << getppid() << std::endl;
		std::cout << "MIN VALUE: " << childMinValue( arr, n ) << std::endl << std::endl;
	}
	return 0;
}
