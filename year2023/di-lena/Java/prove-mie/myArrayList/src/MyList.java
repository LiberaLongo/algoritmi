public class MyList<T> {

	private T[] array;
	private int index;

	public MyList() {
		this(2); 
	}
	public MyList(int initialCapacity) {
		//this.array = (T[]) new Object[initialCapacity];
		//this.array = new T[initialCapacity];
		this.index = 0;
	}

	public void add(T element) {
		if(index == array.length) {
			//T[] tmpArray = (T[]) new Object[array.length * 2];
			//T[] tmpArray = new T[array.length * 2];

			for(int i = 0; i < array.length; i++) {
				tmpArray[i] = array[i];
			}
			array = tmpArray;
		}
		array[index] = element;
		index ++;
	}
	public T get(int idx) {
		return array[idx];
	}
}
