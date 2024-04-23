/*
Counting DNA Nucleotides
url: http://rosalind.info/problems/dna/

Given: A DNA string  of length at most 1000 nt
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in
*/
#include <iostream>
#include <fstream>
#include <istream>
#include <string>

int main(){
    std::cout << "Ciao" << std::endl;
    std::string text;
    std::string dna = "";
    std::ifstream data("../1_Counting_DNA_Nucleotides/rosalind_dna.txt");

    while(getline(data, text)){
        dna = dna + text;
    }

    int a = 0, c = 0, g = 0, t = 0;
    for (int i = 0; i < dna.length(); i++){
        if (dna[i] == 'A'){
            a++;
        }else if (dna[i] == 'C'){
            c++;
        }else if (dna[i] == 'G'){
            g++;
        }else if (dna[i] == 'T'){
            t++;
        }
    }

    std::cout << a << " " << c << " " << g << " " << t << std::endl;     

    data.close();

}
