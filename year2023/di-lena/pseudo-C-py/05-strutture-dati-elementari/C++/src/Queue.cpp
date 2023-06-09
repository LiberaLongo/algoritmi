#include "./Queue.hpp"

//costruttore e distruttore
template <typename Tipo>
Queue<Tipo>::Queue(void)
{
	this->list = Lista<Tipo>();
}

//read
template <typename Tipo>
Tipo Queue<Tipo>::read(void)
{
	return this->list.read(this->list.head());
}

//Queue
template <typename Tipo>
void Queue<Tipo>::enqueue(Tipo elem)
{
	this->list.insert_tail(elem);
}

template <typename Tipo>
Tipo Queue<Tipo>::dequeue(void)
{
	return this->list.read(this->list.remove_head());
}

// stampe
template <typename Tipo>
void Queue<Tipo>::print(void)
{
	cout << "Queue";
	this->list.print();
}

template <typename Tipo>
void Queue<Tipo>::print(string str)
{
    cout << str << "\t";
	this->print();
}

