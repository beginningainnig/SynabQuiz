package synap_6;

import java.util.Scanner;

public class Main_6 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		// 12345678999, 99987654321, 그 사이 피보나치 수의 합은
		// 4byte이상 자료형이므로 long형
		long a = sc.nextLong();
		long b = sc.nextLong();

		// 범위 내 피보나치 수 개수
		int count = count(a, b);
		// 범위 내 피보나치 수 합
		long sum = sum(a, b);

		System.out.println("범위 내 피보나치 수의 개수: " + count);
		System.out.println("범위 내 피보나치 수의 총합: " + sum);

		sc.close();
	}

	// 범위 내 피보나치 수 개수 count
	private static int count(long a, long b) {
		int count = 0;
		long fib1 = 1;
		long fib2 = 2;

		while (fib1 <= b) {
			if (fib1 >= a) { // 범위 만족 시 count 1씩 누적
				count++;
			}

			long save = fib2; // fib2 갱신 전 저장하는 save
			fib2 = fib1 + fib2; // fib1과 fib2의 합으로 fib2 업뎃
			fib1 = save; // 전단계 fib2값(save)이 다음 단계의 fib1이 됌.
		} // 범위 a~b에서 반복

		return count; // 총 카운트 수 출력
	}

	// 범위 내 피보나치 수 합 sum
	private static long sum(long a, long b) {
		long sum = 0;
		long fib1 = 1;
		long fib2 = 2;

		while (fib1 <= b) {
			if (fib1 >= a) {
				sum += fib1;
				// fib1에 범위 내 모든 피보나치 수가 한번씩 저장되므로
				// fib1 모두 더하기
			}

			long save = fib2;
			fib2 = fib1 + fib2;
			fib1 = save; // 피보나치 수 구하는 로직 동일.
		}

		return sum;
	}

}
