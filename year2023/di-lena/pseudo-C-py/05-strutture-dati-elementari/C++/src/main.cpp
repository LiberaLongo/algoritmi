//per i template servono: HPP, CPP, template class NOMECLASSE<TIPI USATI>

//dizionari implementati in vario modo
#include "./ArrayDisordDict.hpp"
#include "./ArrayDisordDict.cpp"
template class ArrayDisordDict<int, string>;

#include "./ArrayOrdDict.hpp"
#include "./ArrayOrdDict.cpp"
template class ArrayOrdDict<int, string>;

#include "./ListDict.hpp"
#include "./ListDict.cpp"
template class ListDict<int, string>;

//basati su lista
#include "./Lista.hpp"
#include "./Lista.cpp"
template class Lista<int>;

#include "./Stack.hpp"
#include "./Stack.cpp"
template class Stack<char>;

#include "./Queue.hpp"
#include "./Queue.cpp"
template class Queue<char>;

//alberi
#include "./Tree.hpp"
#include "./Tree.cpp"
template class Tree<int>;

void test_lista() {
	Lista<int> lista = Lista<int>();
	Lista<int> l2 = Lista<int>();
#if 0
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
#endif
	lista.insert_head(2); lista.insert_head(1); lista.print();
	l2.insert_head(4); l2.insert_head(3); l2.print();
	lista.append(l2);
	lista.print();
	l2.print();
}
void test_stack() {
	Stack<char> s = Stack<char>();
	//esercizio 7... EAS*Y*QUE***ST***IO*N***
	s.print();
	s.push('E'); s.push('A'); s.push('S');
	s.print();
	cout << s.pop() << endl;
	s.print();
	s.push('Y');
	s.print();
	cout << s.pop() << endl;
	s.print();
	s.push('Q'); s.push('U'); s.push('E');
	s.print();
	cout << s.pop() << s.pop() << s.pop() << endl;
	s.print();
	s.push('S'); s.push('T');
	s.print();
	cout << s.pop() << s.pop() << s.pop() << endl;
	s.print();
	s.push('I'); s.push('O');
	s.print();
	cout << s.pop() << endl;
	s.print();
	s.push('N');
	s.print();
	cout << s.pop() << s.pop() << s.pop() << endl;
	s.print();
}
void test_queue() {
	Queue<char> q = Queue<char>();
	//esercizio 7... EAS*Y*QUE***ST***IO*N*** ma fatto con le code (FIFO)
	q.print();
	q.enqueue('E'); q.enqueue('A'); q.enqueue('S');
	q.print();
	cout << q.dequeue() << endl;
	q.print();
	q.enqueue('Y');
	q.print();
	cout << q.dequeue() << endl;
	q.print();
	q.enqueue('Q'); q.enqueue('U'); q.enqueue('E');
	q.print();
	cout << q.dequeue() << q.dequeue() << q.dequeue() << endl;
	q.print();
	q.enqueue('S'); q.enqueue('T');
	q.print();
	cout << q.dequeue() << q.dequeue() << q.dequeue() << endl;
	q.print();
	q.enqueue('I'); q.enqueue('O');
	q.print();
	cout << q.dequeue() << endl;
	q.print();
	q.enqueue('N');
	q.print();
	cout << q.dequeue() << q.dequeue() << q.dequeue() << endl;
	q.print();
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

void test_alberi() {
	Tree<int> t = Tree<int>(1);
}

int main(int argc, char *argv[]) {
	//dictionary();
	test_lista();
	//test_stack();
	//test_queue();
	test_alberi();
}
