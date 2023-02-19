#include <iostream>
#include <string>

class Human {
	// private data
	private:
		std::string name;
		int age;
		float weight;
	
	public:
		//asking user for data to encapsulate 
		void setHumanDetails( std::string givenName, int givenAge, float givenWeight ) {
			name = givenName;
			age = givenAge;
			weight = givenWeight;
		} 

		void showHumanDetails() {
			std::cout << "Name: " << name << '\n'
					  << "Age: " << age << '\n'
					  << "Weight: " << weight
					  << std::endl;
		}

		void changeValues(std::string newName, int newAge, float newWeight) {
			name = newName;
			age = newAge;
			weight = newWeight;
		}
};

//employee class inherits human class
class Employee: public Human {
	private:
		float salary;
		int employeeId;

	public:
		void setEmployeeDetails( std::string givenName, int givenAge, float givenWeight, float givenSalary, int givenId ) {
			setHumanDetails(givenName, givenAge, givenWeight);
			salary = givenSalary;
			employeeId = givenId;
		}

		void showEmployeeDetails() {
			showHumanDetails();
			std::cout << "Salary: " << salary << '\n'
						<< "ID: " << employeeId << std::endl;
		}
};

class Vehichle {
	//private data
	private:
		std::string name;
		int number;
	
	public:
		//taking vehichle data
		void setCarDetails( std::string modelName, int carNumber ) {
			name = modelName;
			number = carNumber;
		}

		void showCarDetails() {
			std::cout << "Name: " << name << '\n'
						<< "Number: " << number
						<< std::endl;
		}
};

class Perimeter {
	public:
		virtual void showPerimeter() = 0;
};

class Circle: public Perimeter {
	private:
		float radius;
	
	public:
		void setRadius( float rad ) {
			radius = rad;
		} 

		void showPerimeter() {
			std::cout << "Circumference is: " << 2 * 3.14 * radius << std::endl;
		}
	
};

class Square: public Perimeter {
	private:
		int side;
	
	public:
		void setSide(int s) {
			side = s;
		}

		void showPerimeter() {
			std::cout << "Perimeter is: " << 4 * side << '\n';
		}
};

//demonstrating function overloading
class Polymorphism {
	public:
		void display(int x) {
			std::cout << "This is an Integer= " << x << '\n';
		}

		void display(double x) {
			std::cout << "This is a Float= " << x << '\n';
		}

		void display(std::string x) {
			std::cout << "This is a String= " << x << '\n';
		}
};

int main() {
	/////////////////////////////////// ENCAPSULATION /////////////////////////////////////////////////
	std::cout << "ENAPSULATION\n";
	std::cout << "------------\n";
	Human person1;
	person1.setHumanDetails( "Elliot", 26, 54.78 );
	Vehichle car1;
	car1.setCarDetails("Ford", 8978);
	std::cout << "Before Change\n";
	person1.showHumanDetails();
	car1.showCarDetails();
	//changing human value
	std::cout << std::endl;
	person1.changeValues("Jack", 26, 54.78);
	std::cout << "After Change\n";
	person1.showHumanDetails();
	car1.showCarDetails();
	std::cout << "\nObject attribute of the vehichle remains unchanged despite change in human. This is encapsulation\n\n";

	////////////////////////////////////// INHERITANCE /////////////////////////////////////////
	Employee employee1;
	//employee class also inherits other details from the human class
	std::cout << "INHERITANCE\n";
	std::cout << "-----------\n";
	employee1.setEmployeeDetails("Joe", 36, 67.8, 78000.12, 8080);
	employee1.showEmployeeDetails();
	std::cout << "Employee inherits the methods from Human class\n\n";

	//////////////////////////////////// ABSTRACTION //////////////////////////////////////////
	Circle circ;
	std::cout << "ABSTRACTION\n";
	std::cout << "-----------\n";
	circ.setRadius(7.2);
	//the virtual function from the abstract class Perimeter is used to find circumference
	circ.showPerimeter();
	std::cout << "\n\n";

	////////////////////////////////// POLYMORPHISM /////////////////////////////////////////
	Polymorphism poly;
	std::cout << "POLYMORPHISM\n";
	std::cout << "------------\n";
	poly.display("abab");
	poly.display(9);
	poly.display(2.78);
	std::cout << "\n\n";
	//////////////////////////////// INTERFACE ////////////////////////////////////////////
	
	//the class Perimeter has only virtual functions so we can also use it as an interface
	std::cout << "INTERFACE\n";
	std::cout << "---------\n";
	Square sqr;
	sqr.setSide(5);
	sqr.showPerimeter();



	return 0;
}
	
