import java.util.ArrayList; 

class crane_doll {
    static public int solution(int[][] board, int[] moves) {
        int answer = 0;
        ArrayList<Integer> before = new ArrayList<Integer>();
        for(int move : moves)
        {
          for(int i=0; i<board.length; i++)
          {
            if(board[i][move] !=0)
            {
              before.add(board[i][move]);
              if(before.size() >1)
              {
                if(before.get(before.size()) == before.get(before.size() - 1)){
                  before.remove(before.size());
                  before.remove(before.size()-1);
                  answer +=2;
                }
              }
            }
          }
        }
        return answer;
    }

    public static void main(String args[])
    {
      int[][] board = {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
      int[] moves = {1,5,3,5,1,2,1,4};
      int answer = 0;
      ArrayList<Integer> before = new ArrayList<Integer>();
      for(int move : moves)
      {
        for(int i=0; i<board.length; i++)
        {
          if(board[i][move] !=0)
          {
            before.add(board[i][move]);
            if(before.size() >1)
            {
              if(before.get(before.size()) == before.get(before.size() - 1)){
                before.remove(before.size());
                before.remove(before.size()-1);
                answer +=2;
              }
            }
          }
        }
      }
      System.out.println(answer);
    }
}

