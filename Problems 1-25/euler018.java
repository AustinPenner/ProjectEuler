import java.util.ArrayList;
import java.util.Arrays;

public class euler018 {
	public static void main(String[] args) {
		ArrayList<ArrayList<Integer>> triangle = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> path = new ArrayList<Integer>(
			Arrays.asList(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0));
		ArrayList<Integer> end_state = new ArrayList<Integer>(
			Arrays.asList(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14));

		triangleBuild(triangle);

		int currentMax = 0;
		int holder;
		int number;
		int tempSum;

		while (!path.equals(end_state)) {
			tempSum = 0;
			for (int k = 0; k < 15; k++) {
				holder = path.get(k);
				number = triangle.get(k).get(holder);
				tempSum += number;
			}

			if (tempSum > currentMax) {
				currentMax = tempSum;
				System.out.println(currentMax);
				System.out.println(path);
			}
			nextPath(path);
		}
	}



	/*	This takes some path and outpus what
	 *	the next path should be.
	 */
	public static void nextPath(ArrayList<Integer> path) {
		int above;
		int current;

		/*	Start at the bottom and add one. We can treat it like
		 *	counting in base n. If you add one to whatever place
		 *	(ones, tens, etc) that you're in, and your current 
		 *	digit is n-1, then you add one to the above digit
		 *	and change all the below digits to 0.
		 */
		for (int i = 14; i > 0; i--) {
			above = path.get(i-1);
			current = path.get(i);
			if (current == above) {
				for (int j = i; j < 15; j++) {
					path.set(j, current + 1);
				}
				return;
			}
		}
	}

	public static void triangleBuild(ArrayList<ArrayList<Integer>> triangle) {
		ArrayList<Integer> row1 = new ArrayList<Integer>(Arrays.asList(75));
		ArrayList<Integer> row2 = new ArrayList<Integer>(Arrays.asList(95, 64));
		ArrayList<Integer> row3 = new ArrayList<Integer>(Arrays.asList(17, 47, 82));
		ArrayList<Integer> row4 = new ArrayList<Integer>(Arrays.asList(18, 35, 87, 10));
		ArrayList<Integer> row5 = new ArrayList<Integer>(Arrays.asList(20, 4, 82, 47, 65));
		ArrayList<Integer> row6 = new ArrayList<Integer>(Arrays.asList(19, 1, 23, 75, 3, 34));
		ArrayList<Integer> row7 = new ArrayList<Integer>(Arrays.asList(88, 2, 77, 73, 7, 63, 67));
		ArrayList<Integer> row8 = new ArrayList<Integer>(Arrays.asList(99, 65, 4, 28, 6, 16, 70, 92));
		ArrayList<Integer> row9 = new ArrayList<Integer>(Arrays.asList(41, 41, 26, 56, 83, 40, 80, 70, 33));
		ArrayList<Integer> row10 = new ArrayList<Integer>(Arrays.asList(41, 48, 72, 33, 47, 32, 37, 16, 94, 29));
		ArrayList<Integer> row11 = new ArrayList<Integer>(Arrays.asList(53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14));
		ArrayList<Integer> row12 = new ArrayList<Integer>(Arrays.asList(70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57));
		ArrayList<Integer> row13 = new ArrayList<Integer>(Arrays.asList(91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48));
		ArrayList<Integer> row14 = new ArrayList<Integer>(Arrays.asList(63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31));
		ArrayList<Integer> row15 = new ArrayList<Integer>(Arrays.asList(4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23));

		triangle.add(row1);
		triangle.add(row2);
		triangle.add(row3);
		triangle.add(row4);
		triangle.add(row5);
		triangle.add(row6);
		triangle.add(row7);
		triangle.add(row8);
		triangle.add(row9);
		triangle.add(row10);
		triangle.add(row11);
		triangle.add(row12);
		triangle.add(row13);
		triangle.add(row14);
		triangle.add(row15);
	}
}

// The answer is 1,074