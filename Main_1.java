package synap_1;

import java.util.Scanner;

public class Main_1 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N;

		do {
			N = sc.nextInt(); // 입력된 끝나는 범위

		} while (N < 1 || N > 9999); // 입력 범위 제한

		int total = 0;
		int sum = 0;

		for (int i = 1; i <= N; i++) {
			if (isHappy(i)) {
				total++;
				sum += i;
			}
		}

		System.out.println("1~" + N + "범위의 행복수는" + total + "개이고 총합은" + sum + "입니다.");

		sc.close();
	}

	// isHappy
	private static boolean isHappy(int num) {
		int slow = num;
		int fast = num;

		do {
			slow = SumOfSquares(slow);
			fast = SumOfSquares(SumOfSquares(fast));
		} while (slow != fast);

		return slow == 1;
	}

	// 자릿수제곱의합 정의
	private static int SumOfSquares(int num) {
		int sum = 0;
		while (num > 0) {
			int digit = num % 10;
			sum += digit * digit;
			num /= 10;
		}
		return sum;
	}
}
