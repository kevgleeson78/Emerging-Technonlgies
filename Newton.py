# formula for newtons method
import math

z_input = 1.0


def newton(x, z):

    z_next = z - ((z*z - x) / (2 * z))
# print out each result of the calculation
    print("\n", z_next)
# conditional to check if the current number is equal to the square root of the original number #
    if z_next == math.sqrt(x):
        return z_next
    else:

        return newton(x, z_next)


newton(25, z_input)


