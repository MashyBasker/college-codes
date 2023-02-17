#include <iostream>
#include <unistd.h>
#include <climits>


int main() {
	int n;
	/* Get the array */
	std::cout << "Enter the size of the array: ";
	std::cin >> n;

	int arr[n];
	for( int i = 0; i < n; i++ ) {
		std::cout << "arr[" << i << "]: ";
		std::cin >> arr[i];
	}

	/* Creating child process using fork()*/
	pid_t chPid = fork();

	/* Displaying process */
	if( chPid > 0 ) {
		std::cout << "PARENT PROCESS RUNNING WITH PID " << getpid() << std::endl;
		int maxVal = INT_MIN;
		
		/* Get the maximum value */
		for( int i = 0; i < n; i++ ) {
			maxVal = std::max(maxVal, arr[i]);
		}
		std::cout << "THE MAX VALUE IS: " << maxVal << std::endl;
		std::cout << std::endl;
		/*Parent process terminating immediately */
		sleep(30);
	}
	
	else if( chPid == 0 ) {
		std::cout << "CHILD PROCESS RUNNING WITH PID " << getpid()
			<< "\nAND HAS PARENT PID " << getppid() << std::endl;
				int minVal = INT_MAX;

		/* Get the minimum value */
		for( int i = 0; i < n; i++ ) {
			minVal = std::min(minVal, arr[i]);
		}

		std::cout << "THE MIN VALUE IS: " << minVal << std::endl;
		std::cout << std::endl;
		exit(0);
	}

	return 0;




}
