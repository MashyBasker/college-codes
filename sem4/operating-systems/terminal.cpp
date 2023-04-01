#include <iostream>
#include <cstdlib>
#include <unistd.h>
#include <lastlog.h>
#include <dirent.h>
#include <vector>
#include <sstream>
#include <sys/stat.h>
#include <sys/un.h>
#include <filesystem>
#include <sys/wait.h>


// function for emulating the "who" command
void who_cmd() {
    std::string user_name = getlogin(); 
    struct lastlog ll;
    int uid = getuid();
    time_t last_log_time = static_cast<time_t>(ll.ll_time);
    std::cout << user_name << "\t\t" << ctime(&last_log_time) << std::endl;
}

void mkdir_cmd(std::string dirname) {
    int status = mkdir(dirname.c_str(), S_IRWXU | S_IRWXU | S_IROTH | S_IXOTH);
    if(status == -1) {
        std::cout << "Error: Could not create directory\n";
    }
}

// function for emulating the "ls" command
void ls_cmd() {
    DIR *dir;
    struct dirent *ent;
    if((dir = opendir(".")) != NULL) {
        while((ent = readdir(dir)) != NULL) {
            std::cout << ent->d_name << std::endl;
        }
        closedir(dir);
    } else {
        std::cout << "Error: Not could not list the directory\n";
    }
}

// remove an empty directory
void rmdir_cmd(std::string dirname) {
    int status = rmdir(dirname.c_str());
    if(status == -1) {
        std::cout << "Error: Could not remove directory\n";
    }
}

//gets the current working directory
std::string pwd_cmd() {
    char cwd[1024];
    if(getcwd(cwd, sizeof(cwd)) != NULL) {
        std::cout << cwd << std::endl;
    } else {
        std::cout << "Error: Could not get current directory\n";
    }
    return cwd;
}

void cd_cmd(std::string dirpath) {
    int status = chdir(dirpath.c_str());
    if(status == -1) {
        std::cout << "Error: Could not change directory\n";
    }
}

void execute_file(char *filename) {
    char *arg[] = {NULL};
    execv(filename, arg);
}

int main() {
    std::string s;
    std::system("clear");
    std::vector<std::string> cc;
    do {
        cc.clear();
        std::string command = "";
        std::cout << "\033[32mbasu\033 >> ";
        std::getline(std::cin, command);
        std::stringstream ss(command);
        std::string token;
        while(ss >> token) {
            cc.push_back(token);
        }

        if(cc[0] == "ls") {
            ls_cmd();
        }
        else if(cc[0] == "who") {
            who_cmd();
        }
        else if(cc[0] == "pwd") {
            pwd_cmd();
        }
        else if(cc[0] == "mkdir") {
            mkdir_cmd(cc[1]);
        }
        else if(cc[0] == "rmdir") {
            rmdir_cmd(cc[1]);
        }
        else if(cc[0] == "cd") {
            cd_cmd(cc[1]);
        }
        else {
            // char *a = cc[0].c_str();
            size_t pid = fork();
            if(pid == 0) {
                std::cout << "Child process running with PID " << getpid() << std::endl;
                execute_file(strdup(cc[0].c_str()));
            }
            else if(pid > 0) {
                wait(0);
            }
        }
        std::cout << std::endl;

    }while(cc[0] != "exit");
}