import java.util.Arrays;
public class Program{
		public static void main(String [] args) {
		int firstNum = 1;
		int lastNum = 21;
		int[] firstMassive = new int[(lastNum+firstNum)/2];
		firstMassive[0] = 1;
		for (int i = 1; i < firstMassive.length; i++) {

			firstMassive[i] = firstMassive[i-1] + 2;
		}

		int nums = 10;
		double [] secondMassive = new double [nums];
		double min = -12.0;
		double max = 12.0;
		for (int i = 0; i < secondMassive.length; i++) {
			 
			secondMassive[i] = min + Math.random() * (max-min);

		}
		double[][] thirdMassive = new double[11][10];
		int[] targetList = {3,11,13,17,19};
		for (int i = 0; i < 11; i++) {
			for (int j = 0; j < 10; j++) {
				double x = secondMassive[j];
				if (firstMassive[i] == 9) {
					thirdMassive[i][j] = Math.exp(Math.atan(Math.cos(x)));
				} else if (Arrays.asList(targetList).contains(firstMassive)) {
					thirdMassive[i][j] = Math.asin(Math.exp(Math.cbrt(-(Math.pow(Math.tan(x), 2)))));
					
				} else {
					thirdMassive[i][j] = Math.cbrt(Math.log(Math.abs(((x-1)/2)/(3/Math.PI))));
				}
			}

			}
		
		for (int i = 0; i < 11; i++) {
			for (int j = 0; j < 10; j++) {
				System.out.printf( "%.5f\t", thirdMassive[i][j]);
			}
			System.out.println();
		}
	}
}

