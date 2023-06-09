#ifndef Queue_HPP
#define Queue_HPP

#include "./Lista.hpp"

//le code sono FIFO = First In First Out
//esempio code alla posta

template <typename Tipo>
class Queue
{
	private:
		Lista<Tipo> list;
	public:
		//costruttore
		Queue();
		//distruttore
		virtual ~Queue(){};
		//read
		Tipo read(void);
		//queue
		void enqueue(Tipo elem);
		Tipo dequeue(void);
		//stampe
		void print(void);
		void print(string str);
};

#endif //Queue_CPP
