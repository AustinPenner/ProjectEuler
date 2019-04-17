import java.util.ArrayList;
import java.util.Arrays;

public class euler024 {
	public static void main(String[] args) {
		int numDigits = 10;
		Integer[] permuteArray = new Integer[numDigits];

		for (int i=0; i < numDigits; i++) {
			permuteArray[i] = i;
		}

		Integer[] subArray;
		Integer[] newSubArray;

		int permutationCount = 0;
		int indexCount = 2;
		while (indexCount < numDigits + 1 && permutationCount < 1000001) {
			if ((permutationCount % 10000 == 0) || permutationCount > 999900) {
				System.out.println("permutation: " + permutationCount);
				System.out.print("array is: ");
				printArray(permuteArray);
			}

			subArray = Arrays.copyOfRange(permuteArray, permuteArray.length - indexCount, permuteArray.length);
			newSubArray = nextArray(Arrays.copyOfRange(permuteArray, permuteArray.length - indexCount, permuteArray.length));
			
			if (Arrays.equals(subArray, newSubArray)) {
				indexCount++;
			} else {
				for (int j=0; j<indexCount; j++) {
					permuteArray[numDigits - j - 1] = newSubArray[indexCount - j - 1];
				}

				indexCount = 2;
				permutationCount++;
			}
		}
	}

	// Receives an array or subarray. If the current array is not the last item in 
	// the array, it outputs the next permutation. Otherwise, it returns the initial 
	// array.
	public static Integer[] nextArray(Integer[] initialArray) {
		Integer elem0 = initialArray[0];
		Integer elem1 = initialArray[1];

		int length = initialArray.length;
		if (elem0 < elem1) {
			Integer nextLargest = elem1;
			Integer index = 0;
			for (int i=0; i<length; i++) {
				if (initialArray[i] > elem0 && initialArray[i] <= nextLargest) {
					nextLargest = initialArray[i];
					index = i;
				}
			}

			initialArray[index] = elem0;
			initialArray[0] = nextLargest;
			return reSort(initialArray, length - 1);
		} else {
			return initialArray;
		}
	}

	// Takes a whole array as input and sorts the last (count) elements
	// from smallest to largest. It returns the whole array, not just the
	// last few elements.
	public static Integer[] reSort(Integer[] array, int count) {
		Integer[] subArray = Arrays.copyOfRange(array, array.length - count, array.length);
		Arrays.sort(subArray);

		for (int i = 0; i<count; i++) {
			array[array.length - count + i] = subArray[i];
		}
		return array;
	}

	public static void printArray(Integer[] array) {
		ArrayList<Integer> arrayList = new ArrayList<Integer>(Arrays.asList(array));
		System.out.println(arrayList);
	}
}

// Answer is 2,783,915,460