"""
Program to return all bit strings with no consecutive 0s
-------------------------------------------------------------------
The solution to above problem is Nth term of the fibonacci sequence.
This can be derived as:

Suppose A represents all even bit strings (i.e ending with 0)
Suppose B represents all odd bit strings (i.e ending with 1)

If we don't know the answer and start writing down all possibilities (for say n = 3)
& represent the three positions of our length-3 bit string as __ __ __ :

We will see that if a position is filled with 0, the next position can be filled
with only 1 and if it is filled with 1, the next position can be filled by either
0 or 1.

Following above statement:

We get out recurrence relation as:

A(n) = A(n -1) + B(n -1)
B(n) = A(n - 1)

Which is nothing but the very familiar fibonacci sequence!
================================================================================

Below is an implementation to find Nth fibonacci sequence in sublinear time space
"""


def mat_mul(mat1, mat2):
    """
    Multiplies two matrices
    Parameters:
    -----------------------
    mat1 : 2x2 int matrix
    mat2 : 2x2 int matrix
    =====================
    Returns:
    -----------------------------------------
    mat1 : 2x2 int matrix
        Multipication of the matrices F and M
    """

    # elements of Multipication matrix
    x = mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0]  # M[0][0]
    y = mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]  # M[0][1]
    z = mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0]  # M[1][0]
    w = mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]  # M[1][1]

    mat1[0][0] = x
    mat1[0][1] = y
    mat1[1][0] = z
    mat1[1][1] = w

    return mat1


def mat_power(mat, n):
    """
    Multipies a matrix n times (Raises to power n)
    Parameters:
    ---------------------------------------------------
    mat : 2x2 int matrix
        Input matrix whose exponent is to be calculated
    n : int
        index to raise the matrix
    ====================================================
    Returns:
    --------------------------------
    mat : 2x2 int matrix
        Input matrix raised to power n
    """

    # base cases
    if(n == 0 or n == 1):
        return mat

    M = [[1, 1], [1, 0]]

    mat = mat_power(mat, n / 2)
    mat = mat_mul(mat, mat)

    if n % 2 != 0:
        mat = mat_mul(mat, M)
    return mat


def fibonacci(n):
    """
    Computes Nth term of fibonacci sequence (which is the solution to our problem)
    Parameters:
    ----------------------------------------------------------------------------
    n : int
        index of the required fibonacci number
    ==========================================
    Returns:
    -------------------------------------------------
    bitstrings : 2x2 int matrix
        number of bitstrings without 2 consecutive 0s
    """
    # Magic matrix ;)
    # This magical matrix when multiplied by n times, gives fibonacci(n + 1)
    # at [0][0] position
    F = [[1, 1], [1, 0]]

    if n == 0:
        return "Wrong Input"
    F = mat_power(F, n - 1)
    bitstrings = F[0][0]
    return bitstrings

if __name__ == '__main__':
    # Driver to test the task
    test_cases = raw_input("Enter the number of test cases: ")
    limit = (10 ** 9) + 7

    input_nums = []  # Input array
    for i in range(int(test_cases)):
        input_nums.append(raw_input("Test case_%d: " % i))  # get the test cases

    for num in input_nums:
        print (fibonacci(int(num) + 2) % limit)  # since the number of strings can be very large
