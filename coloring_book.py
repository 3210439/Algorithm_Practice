class Solution {
    static int count = 0;
    
    public static void dfs(int num, int i, int j, int[][] picture)
    {
        if(i<0 || j <0 || i>=picture.length || j >= picture[0].length)
            return;
        if (picture[i][j] != num)
            return;
        count +=1;
        picture[i][j] = 0;
        dfs(num,i-1, j, picture);
        dfs(num,i+1, j, picture);
        dfs(num,i, j-1, picture);
        dfs(num,i, j+1, picture);
    }
    
    public int[] solution(int m, int n, int[][] picture) {
        int [][]pic = new int[m][n];
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        for (int x = 0; x < picture.length; x++) {
            for (int y = 0; y < picture[x].length; y++) {
                pic[x][y] = picture[x][y];
            }
        }
        

        for(int i=0; i< pic.length; i++)
        {
            for(int j=0; j<pic[i].length; j++)
            {
                if(pic[i][j] != 0)
                {
                    count = 0;
                    Solution.dfs(pic[i][j],i,j,pic);
                    numberOfArea +=1;
                    if (count > maxSizeOfOneArea)
                    {
                        maxSizeOfOneArea = count;
                    }
                }
            }
        }
        
        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }
}