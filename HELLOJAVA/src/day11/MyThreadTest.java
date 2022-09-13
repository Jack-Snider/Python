package day11;

public class MyThreadTest {
	
	public static void printNum() {
		
		for( int i = 1; i <= 100000; i++ ) {
			System.out.print( i );
			if( i % 100 == 0 ) {
				System.out.println();
			}
		}
		
	}
	
public static void printAscii() {
		
		for( int i = 1; i <= 100000; i++ ) {
			System.out.print( ( char ) i );
			if( i % 100 == 0 ) {
				System.out.println();
			}
		}
		
	}
	
	
	public static void main(String[] args) {
		
		printAscii();
		
	}
	
}
