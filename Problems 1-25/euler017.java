import java.util.ArrayList;
import java.util.Arrays;

public class euler017 {
	public static void main(String[] args) {
		int total_sum = 0;
		int total_digits;
		String number;
		for (int i = 1; i < 1000; i++) {
			total_digits = 0;
			number = Integer.toString(i);
			total_digits = underHundred(number) + overHundred(number);
			total_sum += total_digits;

			System.out.println(i + ": " + total_digits);
		}

		/*	This additional 11 is to add 1000 since the loop only
		 *	goes to 999.
		 */
		total_sum += 11;

		System.out.println("\nThe total number of letters is: " + total_sum);
	}

	/*	This finds the number of letters for the ones
	 *	and the tens.
	 */
	public static int underHundred(String number) {
		if (number.length() == 3) {
			number = number.substring(1,3);
		}

		int one_to_99 = Integer.parseInt(number);
		ArrayList<Integer> below20 = new ArrayList<>(Arrays.asList(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19));
		ArrayList<Integer> below20_digits = new ArrayList<>(Arrays.asList(0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8));

		ArrayList<Integer> tens_place = new ArrayList<>(Arrays.asList(0,1,2,3,4,5,6,7,8,9));
		ArrayList<Integer> tens_place_digits = new ArrayList<>(Arrays.asList(0,0,6,6,5,5,5,7,6,6));

		if (below20.indexOf(one_to_99) > -1) {
			int index = below20.indexOf(one_to_99);
			return below20_digits.get(index);
		}

		else {
			int tens = Integer.parseInt(number.substring(0,1));
			int ones = Integer.parseInt(number.substring(1,2));
			
			int tens_index = tens_place.indexOf(tens);
			int ones_index = below20.indexOf(ones);

			int sum = below20_digits.get(ones_index) + tens_place_digits.get(tens_index);
			return sum;
		}
	}

	/*	This finds the number of letters for
	 *	the hundreds place, including the "and".
	 */
	public static int overHundred(String number) {
		if (number.length() != 3) {
			return 0;
		}

		int also_and = 3;

		if ("00".equals(number.substring(1,3))) {
			also_and = 0;
		}

		if (number.length() == 3) {
			number = number.substring(0,1);
		}
		else {
			return 0;
		}

		ArrayList<Integer> hundreds_place = new ArrayList<>(Arrays.asList(0,1,2,3,4,5,6,7,8,9));
		ArrayList<Integer> hundreds_place_digits = new ArrayList<>(Arrays.asList(0,10,10,12,11,11,10,12,12,11));

		int hund = Integer.parseInt(number);

		int hund_index = hundreds_place.indexOf(hund);

		return hundreds_place_digits.get(hund_index) + also_and;
	}
}

/*	The answer is 21124.
 */