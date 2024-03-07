package synap_3;

public class Main_3 {
	public static void main(String[] args) {
		int[][] rectangles = { { 1, 0, 4, 2 }, { 8, 3, 9, 4 }, { 2, 3, 5, 7 }, { 4, 6, 7, 8 }, { 3, 1, 6, 5 },
				{ 1, 8, 4, 10 }, { 7, 2, 9, 5 }, { 8, 8, 10, 9 }, { 1, 4, 2, 6 } };

		int[][] screen = new int[1920][1080];

		for (int[] rectangle : rectangles) {
			int leftTopX = rectangle[0];
			int leftTopY = rectangle[1];
			int rightBottomX = rectangle[2];
			int rightBottomY = rectangle[3];

			// 사각형이 차지하는 부분을 1로 표시
			for (int i = leftTopX; i < rightBottomX; i++) {
				for (int j = leftTopY; j < rightBottomY; j++) {
					screen[i][j] = 1;
				}
			}
		}

		// 전체 면적 계산
		int totalArea = 0;
		for (int i = 0; i < screen.length; i++) {
			for (int j = 0; j < screen[i].length; j++) {
				if (screen[i][j] == 1) {
					totalArea++;
				}
			}
		}

		System.out.println("화면에서 직사각형들이 차지하고 있는 총면적: " + totalArea);
	}
}
