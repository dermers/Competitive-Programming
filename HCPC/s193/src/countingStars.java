import java.util.Scanner;

public class countingStars {

  static char[][] sky;

  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    int co = 1;
    while (kb.hasNextLine()) {
      int m = kb.nextInt();
      int n = kb.nextInt();
      kb.nextLine();
      sky = new char[m][n];
      for (int i = 0; i < m; i++) {
        sky[i] = kb.nextLine().toCharArray();
      }
      int stars = 0;
      for (int r = 0; r < sky.length; r++) {
        for (int c = 0; c < sky[r].length; c++) {
          if (sky[r][c] == '-') {
            apply(r, c, sky);
            stars += 1;
          }
        }
      }
      /*for (int r = 0; r < sky.length; r++) {
        for (int c = 0; c < sky[r].length; c++) {
          System.out.print(sky[r][c]);
        }
        System.out.println();
      }*/
      System.out.println("Case " + co + ": " + stars);
      co += 1;
    }
  }

  private static void apply(int r, int c, char[][] sky) {
    if (r < sky.length && r >= 0 && c < sky[0].length && c >= 0 && sky[r][c] == '-') {
      sky[r][c] = '#';
      apply(r-1, c, sky);
      apply(r+1, c, sky);
      apply(r, c-1, sky);
      apply(r, c+1, sky);
    }
  }
}
