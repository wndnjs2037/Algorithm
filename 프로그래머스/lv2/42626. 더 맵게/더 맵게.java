// 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
// -> a + b*2
// 배열의 값(스코빌 지수)이 가장 낮은 두개의 음식을 위의 조건에 맞춰서 모든 배열의 값이 k 이상이 되게 만들고, 섞은 횟수를 return 한다.
// 조건
// 가장 작은 값 2개를 배열에서 뽑아낸다 (최소값 2개) -> 우선순위 큐 사용
// 가장 작은 값, 두번째로 작은 값을 a +b*2에 맞추어 계산
// 계산한 값을 다시 배열에 반환
// 배열의 값이 전부 k보다 클 때 까지 반복한다.

import java.util.PriorityQueue; //우선순위 큐 import

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> heap = new PriorityQueue(); //우선순위 큐를 사용할 객체 생성
        
        for (int aScoville : scoville){ 
            heap.offer(aScoville);
        }
        
        while(heap.peek() <= K) { //배열의 모든 값이 K보다 클 때 까지 반복한다.
            if (heap.size() == 1){ //사이즈가 1이라면 그냥 -1 리턴
                return -1;
            }
            int a = heap.poll();
            int b = heap.poll();
            
            int result = a + (b * 2); //조건에 맞춘 계산
            heap.offer(result);
            answer ++;
        }
        return answer;
    }
}