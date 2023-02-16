#include <iostream>
#include <unistd.h>
#include <algorithm>
#include <climits>

int main() {
	int n;
	/* Get the size of the array */
	std::cout << "Enter the size of the array: ";
	std::cin >> n;

	int array[n];

	/* Get the array */
	for( int i = 0; i < n; i++ ) {
		std::cout << "array[" << i << "]: ";
		std::cin >> array[i];
	}
	std::cout << std::endl;	
	/* Creating the child process */ 
	pid_t ps1 = fork();
	
	/* Show fork() error */ 
	if ( ps1 < 0 ) {
		std::cout << "[ERROR] Could not fork" << std::endl;
		return -1;
	}

	else if( ps1 == 0 ) {
		std::cout << "CHILD PROCESS RUNNING WITH PID " << getpid() << std::endl;
		int minVal = INT_MAX;

		for( int i = 0; i < n; i++ ) {
			minVal = std::min( minVal, array[i] );
		}

		std::cout << "THE MINIMUM VALUE: " << minVal << std::endl;
		std::cout << "FINISHED TASK 1\n\n";
	}

	else if( ps1 > 0 ) {
		sleep(4);
		std::cout << "PARENT PROCESS RUNNING WITH PID " << getpid() << std::endl;
		int maxVal = INT_MIN;

		for( int i = 0; i < n; i++ ) {
			maxVal = std::max( maxVal, array[i] );
		}
		
		std::cout << "THE MAXIMUM VALUE: " << maxVal << std::endl;
		std::cout << "FINISHED TASK 2\n\n";
	}

	return 0;


}
