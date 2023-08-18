#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>

using namespace std;

// Set of C++ keywords to ignore
unordered_set<string> keywords = {"alignas", "alignof", "and", "and_eq", "asm",
        "auto", "bitand", "bitor", "bool", "break",
        "case", "catch", "char", "char16_t", "char32_t",
        "class", "compl", "const", "constexpr", "const_cast",
        "continue", "decltype", "default", "delete", "do",
        "double", "dynamic_cast", "else","endl", "enum", "explicit",
        "export", "extern", "false", "float", "for",
        "friend", "goto", "if","include", "inline", "int",
        "long", "mutable", "namespace", "new", "noexcept",
        "not", "not_eq", "nullptr", "operator", "or",
        "or_eq", "private", "protected", "public", "register",
        "reinterpret_cast", "return", "short", "signed", "sizeof",
        "static", "static_assert", "static_cast","std","stdc","string", "struct", "switch",
        "template", "this", "thread_local", "throw", "true",
        "try", "typedef", "typeid", "typename", "union",
        "unsigned", "using", "virtual", "void", "volatile",
        "wchar_t", "while", "xor", "xor_eq"};

string removeComments(string prgrm)
{
    int n = prgrm.length();
    string res;
   
    bool s_cmt = false;
    bool m_cmt = false;
   
    for(int i=0;i<n;i++)
    {
        if(s_cmt == true && prgrm[i] == '\n')
         s_cmt = false;
        else if(m_cmt == true && prgrm[i] == '*' && prgrm[i+1] == '/')
         m_cmt = false, i++;
        else if (s_cmt || m_cmt)
            continue;
        else if(prgrm[i] == '/' && prgrm[i+1] == '/')
         s_cmt = true, i++;
        else if(prgrm[i] == '/' && prgrm[i+1] == '*')
         m_cmt = true, i++;
        else
         res += prgrm[i];
    }
    return res;
}

// NFA function to recognize identifiers
unordered_set<string> findIdentifiers(string input) {
    unordered_set<string> identifiers;
    int currentState = 0;
    string currentIdentifier;

    for (size_t i = 0; i < input.length(); i++) {
        char ch = input[i];

        switch (currentState) {
            case 0: // Start state
                if (isalpha(ch) || ch == '_') {
                    currentState = 1;
                    currentIdentifier = ch;
                } else if (ch == '"') {
                    currentState = 3; // Ignore string
                }
                break;

            case 1: // State q1
                if (isalpha(ch) || isdigit(ch) || ch == '_') {
                    currentState = 2;
                    currentIdentifier += ch;
                } else {
                    if (!currentIdentifier.empty() && keywords.find(currentIdentifier) == keywords.end()) {
                        identifiers.insert(currentIdentifier);
                    }
                    currentIdentifier.clear();
                    currentState = 0;
                    i--; 
                }
                break;

            case 2: // State q2
                if (isalpha(ch) || isdigit(ch) || ch == '_') {
                    currentIdentifier += ch;
                } else {
                    if (!currentIdentifier.empty() && keywords.find(currentIdentifier) == keywords.end()) {
                        identifiers.insert(currentIdentifier);
                    }
                    currentIdentifier.clear();
                    currentState = 0;
                    i--; 
                }
                break;

            case 3: // Ignore string
                if (ch == '"') {
                    currentState = 0; 
                }
                break;
        }
    }

    // Check if the final state is reached
    if ((currentState == 2 || currentState == 1) && !currentIdentifier.empty() && keywords.find(currentIdentifier) == keywords.end()) {
        identifiers.insert(currentIdentifier);
    }

    return identifiers;
}

int main() {
string file_path = "source_code.cpp";
    ifstream file(file_path);

    if (!file) {
        cerr << "Error opening file.\n";
        return 1;
    }

    string program((istreambuf_iterator<char>(file)), istreambuf_iterator<char>());

    string modified_program = removeComments(program);
    unordered_set<string> identifiers = findIdentifiers(modified_program);

    cout << "Identifiers found in the program:\n";
    for (auto identifier : identifiers) {
        cout << identifier << endl;
    }

    return 0;
}
