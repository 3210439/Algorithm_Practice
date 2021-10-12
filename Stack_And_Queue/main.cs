using System;
using System.Collections.Generic;

/* 초단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어
지지 않은 기간은 몇초인지를 return 하도록 solution 함수를 완성하세요. 
exam
prices [1,2,3,2,3]
return [4,3,1,1,0]
*/

class Program {
        public int[] solution(int[] prices)
        {
            int[] answer = new int[] { };
            Queue<int> Q = new Queue<int>();

            for (int i = 0; i < prices.Length; i++)
            {
                int k = 0;
                for (int j = i + 1; j < prices.Length; j++)
                {
                    k++;
                    if (prices[i] > prices[j])
                        break;
                }
                Q.Enqueue(k);
            }
            answer = Q.ToArray();

            return answer;
        }

        public static void Main(string[] args)
        {
            Program p = new Program();
            int[] prices = { 1, 2, 3, 2, 3 };
            int[] answers = p.solution(prices);
            foreach (int answer in answers)
            {
                Console.WriteLine(answer);
            }
        }
}