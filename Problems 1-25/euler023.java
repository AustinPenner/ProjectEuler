import java.util.Arrays;
import java.util.ArrayList;

public class euler023 {
	public static void main(String[] args) {
		int maxInt = 28124;

		// Creates a boolean array to identify abundant numbers.
		boolean[] abundantBools = new boolean[maxInt];
		for (int i=0; i<maxInt; i++) {
			abundantBools[i] = isAbundant(i);
		}

		// Creats an arraylist of only the abundant numbers from the above array.
		ArrayList<Integer> abundantNumbers = new ArrayList<Integer>();
		for (int i=0; i<maxInt; i++) {
			if (abundantBools[i]) {
				abundantNumbers.add(i);
			}
		}

		int abundantNumsSize = abundantNumbers.size();

		// Creates an array of all numbers that can be written as the sum of
		// two abundant numbers.
		boolean[] abundantSum = new boolean[maxInt];
		for (int i=0; i< abundantNumsSize; i++) {
			for (int j=i; abundantNumbers.get(i) + abundantNumbers.get(j) < maxInt; j++) {
				int sum = abundantNumbers.get(i) + abundantNumbers.get(j);
				abundantSum[sum] = true;
			}
		}

		// Looks at each index that is false in the above array, and sums them together.
		int sumOfInts = 0;
		for (int i=0; i<maxInt; i++) {
			if (!abundantSum[i]) {
				sumOfInts += i;
			}
		}
		System.out.println(sumOfInts);
	}

	public static boolean isAbundant(int number) {
		if (number < 2) {
			return false;
		}

		ArrayList<Integer> divisors = getDivisors(number);
		int sum = 0;
		for (int element: divisors) {
			sum += element;
		}

		if (sum > number) {
			return true;
		} else {
			return false;
		}
	}

	public static ArrayList<Integer> getDivisors(int num) {
		ArrayList<Integer> divisors = new ArrayList<Integer>();
		divisors.add(1);

		int i = 2;
		while (i <= Math.sqrt(num)) {
			if (num % i == 0) {
				if (num / i == i) {
					divisors.add(i);
				} else {
					divisors.add(i);
					divisors.add(num / i);
				}
			}

			i++;
		}

		return divisors;
	}
}


// The answer is 4,179,871