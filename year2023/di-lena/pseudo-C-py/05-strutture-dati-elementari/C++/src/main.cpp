
//per i template servono: HPP, CPP, template class NOMECLASSE<TIPI USATI>

#include "./ArrayDisordDict.hpp"
#include "./ArrayDisordDict.cpp"
template class ArrayDisordDict<int, string>;

#include "./ArrayOrdDict.hpp"
#include "./ArrayOrdDict.cpp"
template class ArrayOrdDict<int, string>;

#include "./ListDict.hpp"
#include "./ListDict.cpp"
template class ListDict<int, string>;

#include "./Lista.hpp"
#include "./Lista.cpp"
template class Lista<int>;

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

void dictionary() {
	//declaration
	//ArrayDisordDict<int, string> diz = ArrayDisordDict<int, string>();
	//ArrayOrdDict<int, string> diz = ArrayOrdDict<int, string>();
	ListDict<int, string> diz = ListDict<int, string>();
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

int main(int argc, char *argv[]) {
	dictionary();
	//test_lista();
}
