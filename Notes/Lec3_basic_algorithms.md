# Lec3_Basic_Algorithms

## Binary Search

**Example: find cube**

Another method: [Newton’s method - Wikipedia](https://en.wikipedia.org/wiki/Newton%27s_method)

instead exhausive search, use binary search -> half the search space each time

## Binary represenation

* Integer to binary

* <u>**Float to binary**</u>

  * Multiply by 2 ^n to make it a integer

    * Use 2 ^ n because later division is simplier by shifting

  * Convert integer to binary

  * Divide binary by 2^n

    ```
    eg.
    0.375
    1. 0.375 * 2 ^ 3 = 3
    2. 3 -> 11(binary)
    3. 11(binary) / 2 ^ 3 -> 0.011 (simply right shift >> 3) 
    ```

* Testing float equation is not accurate -> use `abs(x - y) < epsilon`

