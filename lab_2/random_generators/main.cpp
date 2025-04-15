#include <bitset>
#include <ctime>
#include <fstream>
#include <iostream>
#include <random>

using namespace std;

const string PATH_TO_SAVE = "sequence.txt";

/**
 * A function for writing content to a file
 * 
 * @param path Path to file
 * @param content The content that we write to the file
 *
 * @return A boolean variable that determines whether it was written to the file
 */
bool writeInFile(string path, string content) {
	ofstream file(path);
	if (file.is_open()) {
		file << content << endl;
		return true;
	}
	file.close();
	return false;
}

/**
 * A function that generates a random binary sequence 
 *
 * @return Binary sequence
 */
string generateRandomSequence() {
	srand(time(NULL));
	string sequence;

	for (int i = 0; i < 128; i++) {
		int elem = rand() % 2;
		if (elem)
			sequence += "1";
		else
			sequence += "0";
	}
	return sequence;
}

int main() {
	string sequence = generateRandomSequence();

	cout << sequence << endl;
	writeInFile(PATH_TO_SAVE, sequence);

	return 0;
}