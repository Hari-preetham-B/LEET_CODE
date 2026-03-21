class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;                                       // we are checking from the start for the duplicates if they match then we move forward 
                nums[i] = nums[j];                         // till we get a different element and copy the element in the place of duplicate.
            }
        }
        return i + 1;
    }
}
