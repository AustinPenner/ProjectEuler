import java.util.ArrayList;
import java.util.Arrays;

public class euler019 {
	public static void main(String[] args) {
		int count = 0;
		// current_date is set up with (year, month, day, day of week) format
		ArrayList<Integer> current_date = new ArrayList<Integer>(Arrays.asList(1900,1,1,1));

		while (current_date.get(0) < 2001) {
			int current_day_of_week = current_date.get(3);
			if (current_date.get(0) > 1900 && (current_date.get(3) == 0 && current_date.get(2) == 1)) {
				count++;
				System.out.println(current_date);
			}

			current_day_of_week += 1;
			current_day_of_week = current_day_of_week % 7;
			current_date.set(3,current_day_of_week);

			next_date(current_date);
		}

		System.out.println("The total number of Sundays that fell on the");
		System.out.println("first of the month in the 20th century was: " + count);
	}

	public static void next_date(ArrayList<Integer> current_date) {
		ArrayList<Integer> days_in_month = new ArrayList<Integer>(Arrays.asList(0,31,28,31,30,31,30,31,31,30,31,30,31));

		if (current_date.get(0) % 4 == 0) {
			if (current_date.get(0) % 400 == 0) {
				days_in_month.set(2,29);
			}
			else if (current_date.get(0) % 100 == 0) {
				int j = 0;
			}
			else {
				days_in_month.set(2,29);
			}
		}

		int year = current_date.get(0);
		int day = current_date.get(2);
		int month = current_date.get(1);
		if (day == days_in_month.get(month)) {
			if (month == 12) {
				current_date.set(0, year + 1);
				current_date.set(1, 1);
				current_date.set(2, 1);
			}
			else {
				current_date.set(1, month + 1);
				current_date.set(2, 1);
			}
		}
		else {
			current_date.set(2, day + 1);
		}
	}
}

// The answer is 171