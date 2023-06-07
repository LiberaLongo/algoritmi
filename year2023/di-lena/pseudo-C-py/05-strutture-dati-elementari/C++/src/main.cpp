#include "./Lista.hpp"
#include "./ArrayDisordDict.hpp"

//per utilizzare i template...
#include "./Lista.cpp"
template class Lista<int>; //dichiariamo che ci serve una lista di interi

#include "./ArrayDisordDict.cpp"
template class ArrayDisordDict<int, string>;

void test_lista() {
	Lista<int> lista = Lista<int>();
	cout << "vuota? " << lista.empty() << endl;
	lista.insert_head(3);
	cout << "\t\t";
	lista.print();
	cout << "vuota? " << lista.empty() << endl;
	lista.insert_head(1);
	lista.print("insert head(1)");
	lista.insert(lista.next(lista.head()), 2);
	lista.print("insert(...)");
	lista.insert_tail(4);
	lista.print("insert tail(4)");
	cout << "lunghezza: " << lista.lunghezza() << endl;
	lista.remove_head();
	lista.print("remove head");
}
void dictionary_array_disordinati() {
	ArrayDisordDict<int, string> diz = ArrayDisordDict<int, string>();
	diz.Insert(1, "hello");
	diz.print();
	diz.Insert(2, "darkness");
	diz.print();
	diz.Insert(3, "my dear");
	diz.print();
	diz.Insert(4, "friend");
	diz.print();
}
int main(int argc, char *argv[]) {
	dictionary_array_disordinati();
}
