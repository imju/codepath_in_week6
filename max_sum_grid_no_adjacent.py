// Function to find max sum without adjacent
 public static int maxSum(int grid[][], int n)
 {
     // Sum including maximum element of first
     // column
     int incl = Math.max(grid[0][0], grid[1][0]);

     // Not including first column's element
     int excl = 0, excl_new;

     // Traverse for further elements
     for (int i = 1; i < n; i++ )
     {
         // Update max_sum on including or
         // excluding of previous column
         excl_new = Math.max(excl, incl);

         // Include current column. Add maximum element
         // from both row of current column
         incl = excl + Math.max(grid[0][i], grid[1][i]);

         // If current column doesn't to be included
         excl = excl_new;
     }

     // Return maximum of excl and incl
     // As that will be the maximum sum
     return Math.max(excl, incl);
 }
