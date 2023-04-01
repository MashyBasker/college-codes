#include <iostream>
#include <unistd.h>
#include <algorithm>
#include <cstdlib>
#include <string.h>

std::string parent_choice() {

	int N = rand() % 2;
	std::string ans;

	if(N == 0) {
		ans = "MIN";
	} 
	else if(N == 1) {
		ans = "MAX";
	}
	return ans;
}

int verdict(int c, int d, std::string choice) {
	int v;
	if(choice == "MIN") {

		v = std::min(c, d);
	}
	else if(choice == "MAX") {

		v = std::max(c, d);
	}
	return v;
}

int main() {

	int cfd[2];
	int dfd[2];

	if(pipe(cfd) == -1) {
		std::cout << "[Error] Pipe creation for process C failed\n";
		EXIT_FAILURE;
	}

	if(pipe(dfd) == -1) {
		std::cout << "[Error] Pipe creation for process D failed\n";
	}

	size_t cpid, dpid;
	cpid = fork();
	dpid = fork();
	int cpoints = 0, dpoints = 0;

	while(cpoints != 10 && dpoints != 10) {


		if(cpid < 0 || dpid < 0) {

			perror("Child process creation failed\n");
		}
		else if(cpid == 0 && dpid > 0) {
			int cnum = rand() % 100;
			write(cfd[1], &cnum, sizeof(int));
			sleep(1);
		}
		else if(dpid == 0 && cpid > 0) {
			int dnum = rand() % 99;
			write(dfd[1], &dnum, sizeof(int));
			sleep(1);
		}
		else if(dpid == 0 && cpid == 0) {
			sleep(1);
			int cnum, dnum;
			read(cfd[0], &cnum, sizeof(int));
			read(dfd[0], &dnum, sizeof(int));
			std::string ch = parent_choice();
			std::cout << "------------------------------------------------------\n";
			std::cout << "[PARENT CHOICE]: " << ch << std::endl;
			std::cout << "[PROCESS C]: " << cnum << "   [PROCESS D]: " << dnum << "\n";

			int verd = verdict(cnum, dnum, ch);
			std::cout << "Verdict: " << verd << '\n';
			if(verd == cnum) {
				std::cout << "Process C wins this round\n";
				cpoints++;
			}
			else if(verd == dnum) {
				std::cout << "Process D wins this round\n";
				dpoints++;
			}
			std::cout << "Process C points: " << cpoints << std::endl;
			std::cout << "Process D points: " << dpoints << std::endl;
			std::cout << "------------------------------------------------------\n";
		}
	}

	if(cpoints == 10) {

		std::cout << "\nWINNER IS PROCESS C\n"; 
	}

	else if(dpoints == 10) {

		std::cout << "\nWINNER IS PROCESS D\n";
	}

	return 0;

}