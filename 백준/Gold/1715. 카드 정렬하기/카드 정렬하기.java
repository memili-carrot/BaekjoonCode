import java.util.*;
import java.io.*;
class Main{
    static PriorityQueue<Integer> que = new PriorityQueue<>();
    static int solution(){
        int result = 0;
        if (que.size()==1){
            return 0;
        }
        while(!que.isEmpty()){
            int n1 = que.poll();
            int n2 = que.poll();
            result =result+n1+n2;
            que.offer(n1+n2);
            if(que.size()==1)
                break;
        }
        return result;
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for(int i = 0; i < n; i++){
            int v = Integer.parseInt(br.readLine());
            que.offer(v);
        }
        System.out.print(solution());
    }
}