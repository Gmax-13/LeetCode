class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        
        // Traverse the digits from the end to the beginning
        for (int i = n - 1; i >= 0; i--) {
            // If the current digit is less than 9, increment it and return
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            // If the digit is 9, set it to 0 (carry over to the next digit)
            digits[i] = 0;
        }
        
        // If all digits were 9, we need to add an additional 1 at the beginning
        int[] result = new int[n + 1];
        result[0] = 1; // Set the first digit to 1, rest are already 0 by default
        return result;
    }
}
