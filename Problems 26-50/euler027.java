public class euler027 {
	public static void main(String[] args) {
		int mostConsecutivePrimes = 0;
		int mostA;
		int mostB;

		for (int a= -999; a<1000; a++) {
			for (int b= -1000; b<=1000; b++) {
				if (consecutivePrimes(a,b) > mostConsecutivePrimes) {
					mostConsecutivePrimes = consecutivePrimes(a,b);
					mostA = a;
					mostB = b;
					System.out.println("a: " + a + ", b: " + b);
					System.out.println("consecutive primes: " + mostConsecutivePrimes);
				}
			}
		}
	}

	public static int consecutivePrimes(int a, int b) {
		int n = 0;
		while (isPrime(n*n+a*n+b)) {
			n++;
		}

		return n;
	}

	public static boolean isPrime(int number) {
		if (number < 2) {
			return false;
		} else {
			for (int i=2; i <= Math.sqrt(number); i++) {
				if (number % i == 0) {
					return false;
				}
			}
		}
		return true;
	}
}

// Answer is -59,231