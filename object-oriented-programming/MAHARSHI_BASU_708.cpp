#include <iostream>
#include <utility>
#include <algorithm>
#include <vector>

class AdjMatrix {
    private:
        std::vector<std::pair<int, int>> gdata;
        int nodes;
        int edges = 0;
        std::vector<std::vector<int>> matrix;
    public:
        AdjMatrix(int n_nodes);
        void add_edge();
        void remove_edge();
        void display_matrix();
        void create_matrix();

};

AdjMatrix::AdjMatrix( int n_nodes ) {
    nodes = n_nodes;
    matrix.resize(n_nodes, std::vector<int>(nodes, 0));
}

void AdjMatrix::create_matrix() {
    matrix.resize(nodes, std::vector<int>(nodes, 0));
    for( int i = 0; i < edges; i++ ) {
        matrix[gdata[i].first - 1][gdata[i].second - 1]++;
    }
}

void AdjMatrix::add_edge() {
    std::pair<int, int> p;
    std::cin >> p.first >> p.second;
    gdata.push_back(p);
    edges++;
    create_matrix();
}

void AdjMatrix::remove_edge() {
    std::pair<int, int> p;
    std::cin >> p.first >> p.second;
    gdata.push_back(p);
    edges--;
    create_matrix();
}

void AdjMatrix::display_matrix() {
    for( int i = 0; i < nodes; i++ ) {
        for( int j = 0; j < nodes; j++) {
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    int e, n;
    std::cout << "ENTER THE NUMBER OF NODES: ";
    std::cin >> n;
    AdjMatrix admat(n);
    int ch;
    do {
        std::cout << "Press 1 to add edge\n";
        std::cout << "Press 2 to remove edge\n";
        std::cout << "Press 3 to display matrix\n";
        std::cout << "Press -1 to exit\n";
        std::cout << "Enter choice: ";
        std::cin >> ch;
        switch(ch) {
            case 1:
                admat.add_edge();
                break;
            case 2:
                admat.remove_edge();
                break;
            case 3:
                std::cout << std::endl;
                admat.display_matrix();
                std::cout << std::endl;
                break;
        }
    }while(ch != -1);
    return 0;
}

/*

The following OOP concepts are used in this program:

- Encapsulation: The private member variables (gdata, nodes, edges, matrix) are encapsulated inside the class and cannot be accessed directly from outside the class. Access to these variables is provided through public member functions.

- Abstraction: The user of the class does not need to know the details of how the adjacency matrix is implemented. The member functions of the class provide an abstraction layer that allows the user to interact with the adjacency matrix without knowing its implementation details.

- Constructor: The class has a constructor that takes an argument for the number of nodes and initializes the adjacency matrix with the given number of nodes.

- Member functions: The class has member functions that allow the user to add an edge, remove an edge, and display the adjacency matrix. These member functions provide access to the encapsulated member variables and implement the logic of modifying and displaying the adjacency matrix.

- Data hiding: The private member variables of the class are hidden from the user of the class, and only the public member functions can access and modify them.

*/

