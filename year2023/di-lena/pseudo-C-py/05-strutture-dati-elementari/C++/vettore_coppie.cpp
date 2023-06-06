//file copiato da:
// https://www.delftstack.com/it/howto/cpp/vector-pair-cpp/?utm_content=cmp-true

#include <iostream>
#include <vector>

using std::cout; using std::cin;
using std::endl; using std::string;
using std::vector; using std::pair;
using std::make_pair;

template<typename T>
void printVectorElements(vector<T> &vec)
{
    for (auto i = 0; i < vec.size(); ++i) {
        cout << "(" << vec.at(i).first << ","
            << vec.at(i).second << ")" << "; ";
    }
    cout << endl;
}

int main() {
    vector<pair<int, string>> vec1 = {{12, "twelve"},
                                      {32, "thirty-two"},
                                      {43, "forty-three"}};

    cout << "vec1: ";
    printVectorElements(vec1);

    vec1.push_back(make_pair(55, "fifty-five"));

    cout << "vec1: ";
    printVectorElements(vec1);
    cout << endl;

    return EXIT_SUCCESS;
}

