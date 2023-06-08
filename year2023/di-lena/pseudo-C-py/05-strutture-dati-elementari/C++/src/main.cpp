#define DIZIONARIO //scegli cosa vuoi che sia definito...

#ifdef LISTA
#include "./Lista.hpp"
#include "./Lista.cpp" //per i templates serve il CPP
template class Lista<int>; //dichiariamo che ci serve una lista di interi
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
#endif //LISTA

#ifdef DIZIONARIO
#include "./ArrayDisordDict.hpp"
#include "./ArrayOrdDict.hpp"
//per i template servono i CPP
#include "./ArrayDisordDict.cpp"
#include "./ArrayOrdDict.cpp"
template class ArrayDisordDict<int, string>;
template class ArrayOrdDict<int, string>;

void dictionary() {
	//declaration
	//ArrayDisordDict<int, string> diz = ArrayDisordDict<int, string>();
	ArrayOrdDict<int, string> diz = ArrayOrdDict<int, string>();
	//insert in tail
	diz.insert(3, "my dear");
	diz.print();
	diz.insert(4, "friend");
	diz.print();
	diz.insert(1, "hello");
	diz.print();
	diz.insert(2, "darkness");
	diz.print();
	//replace
	diz.insert(3, "my");
	diz.print();
	diz.insert(4, "dear");
	diz.print();
	//insert again in tail
	diz.insert(5, "friend");
	diz.print();

	//and now remove...
	diz.remove(3);
	diz.print();
	//an element that doesn't exists
	diz.remove(6);
	diz.print();
}
#endif //DIZIONARIO

int main(int argc, char *argv[]) {
	dictionary();
}
