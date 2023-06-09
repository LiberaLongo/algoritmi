#ifndef STACK_HPP
#define STACK_HPP

#include "./Lista.hpp"

//le pile sono LIFO = Last In First Out
//esempio piatti da lavare

template <typename Tipo>
class Stack
{
	private:
		Lista<Tipo> list;
	public:
		//costruttore
		Stack();
		//distruttore
		virtual ~Stack(){};
		//read
		Tipo read(void);
		//stack
		void push(Tipo elem);
		Tipo pop(void);
		//stampe
		void print(void);
		void print(string str);
};

#endif //STACK_CPP
