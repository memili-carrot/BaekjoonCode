import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int buYear = Integer.parseInt(br.readLine());
        int gregoriYear = buYear - 543;

        System.out.println(gregoriYear);
    }
}