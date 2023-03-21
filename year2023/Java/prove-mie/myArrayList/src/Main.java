public class Main {
	public static void main (String[] args) {
		MyList<String> list = new MyList<String>();
		list.add("pippo");
		list.add("pluto");
		System.out.println(list.get(0));
		System.out.println(list.get(1));
	}
}
