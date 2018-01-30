class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) <= 1:
            return 0
        step, max_range, next_range = 1, A[0], A[0]


        for i in xrange(1,len(A)):
            if max_range >= len(A)-1:
                return step
            if i > max_range:
                max_range = next_range
                step += 1
            next_range = max(next_range, i + A[i])
        return step

public class Solution {
    public int jump(int[] nums) {
      int n = nums.length, jumps = 0, max = nums[0], curMax = 0;
      if(n == 0 || n == 1) return 0;

      for(int i = 1; i < n-1; i++){
        curMax = Math.max(curMax, i + nums[i]);
        if(i == max){
          max = curMax;
          jumps++;
        }
      }
      jumps++;

      return jumps;
    }
}
