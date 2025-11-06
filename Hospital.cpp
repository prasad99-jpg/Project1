#include <iostream>
#include <string>
#include <fstream>
using namespace std;

class Person {
private:
    string name;
    int age;
public:
    Person(string n, int a) {
        name = n;
        age = a;
    }

    string getName() { return name; }
    int getAge() { return age; }

    virtual void displayDetails() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }

    virtual void saveToFile(ofstream &file) {
        file << "Name: " << name << endl;
        file << "Age: " << age << endl;
    }

    virtual ~Person() {} 
};

class Doctor : public Person {
private:
    string specialization;
    int experience;
public:
    Doctor(string n, int a, string s, int e) : Person(n, a) {
        specialization = s;
        experience = e;
    }

    void displayDetails() override {
        cout << "---- Doctor Details ----" << endl;
        cout << "Name: " << getName() << endl;
        cout << "Age: " << getAge() << endl;
        cout << "Specialization: " << specialization << endl;
        cout << "Experience: " << experience << " years" << endl;
    }

    void saveToFile(ofstream &file) override {
        file << "---- Doctor Details ----" << endl;
        Person::saveToFile(file);
        file << "Specialization: " << specialization << endl;
        file << "Experience: " << experience << " years" << endl;
        file << "-------------------------" << endl;
    }
};

class Patient : public Person {
private:
    string disease;
    int roomNumber;
public:
    Patient(string n, int a, string d, int r) : Person(n, a) {
        disease = d;
        roomNumber = r;
    }

    void displayDetails() override {
        cout << "---- Patient Details ----" << endl;
        cout << "Name: " << getName() << endl;
        cout << "Age: " << getAge() << endl;
        cout << "Disease: " << disease << endl;
        cout << "Room Number: " << roomNumber << endl;
    }

    void saveToFile(ofstream &file) override {
        file << "---- Patient Details ----" << endl;
        Person::saveToFile(file);
        file << "Disease: " << disease << endl;
        file << "Room Number: " << roomNumber << endl;
        file << "-------------------------" << endl;
    }
};

class Nurse : public Person {
private:
    string shift;
public:
    Nurse(string n, int a, string s) : Person(n, a) {
        shift = s;
    }

    void displayDetails() override {
        cout << "---- Nurse Details ----" << endl;
        cout << "Name: " << getName() << endl;
        cout << "Age: " << getAge() << endl;
        cout << "Shift: " << shift << endl;
    }

    void saveToFile(ofstream &file) override {
        file << "---- Nurse Details ----" << endl;
        Person::saveToFile(file);
        file << "Shift: " << shift << endl;
        file << "-------------------------" << endl;
    }
};

int main() {
    Person* p;

    Doctor d1("Dr. Varma", 45, "Sychology", 20);
    Patient p1("Elon Musk", 30, "Fever", 105);
    Nurse n1("Anita Verma", 28, "Night");

    cout << "===== HOSPITAL MANAGEMENT SYSTEM =====" << endl;

    ofstream file("hospital_data.txt", ios::out);
    if (!file) {
        cout << "Error opening file!" << endl;
        return 1;
    }

    p = &d1;
    p->displayDetails();
    p->saveToFile(file);
    cout << endl;

    p = &p1;
    p->displayDetails();
    p->saveToFile(file);
    cout << endl;

    p = &n1;
    p->displayDetails();
    p->saveToFile(file);
    cout << endl;

    file.close();
    cout << "✅ All details saved to 'hospital_data.txt' successfully!" << endl;

    cout << "\n===== Reading Data from File =====" << endl;
    ifstream infile("hospital_data.txt");
    if (infile) {
        string line;
        while (getline(infile, line)) {
            cout << line << endl;
        }
        infile.close();
    } else {
        cout << "Error reading file!" << endl;
    }

    return 0;
}
