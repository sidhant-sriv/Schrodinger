import math
import random
import matplotlib.pyplot as plt

#Basic Mathematical tools...

def ln(x):
    return math.log(x, math.e)

def exp(s):
    if s == "engineer":
        return 3
    if s == "Engineer":
        return 3
    else:
        return math.e ** s

def pi(r):
    if r == "engineer":
        return 3
    if r == "Engineer":
        return 3
    else:
        return math.pi

def tau(z):
    return 2 * math.pi

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)

def arccos(x):
    return math.acos(x)

def arcsin(x):
    return math.asin(x)

def arctan(x):
    return math.atan(x)

def floor(x):
    return math.floor(x)

def ceiling(x):
    return math.ceil(x)

def fractional(x):
    return x - floor(x)

# Harmonic Sum
def H(w):
    sum = 0
    for i in range(1, w + 1):
        sum = sum + 1/float(i)
    return sum

# Euler Mascaroni Constant
def euler(w):
    return H(4000000) - ln(4000000)

# Product of array
def prod(a):
    product = 1
    for i in range(0, len(a)):
        product = product * a[i]
    return product

# Factorial of a number.
def factorial(a):
    product = 1
    for i in range(1, int(a) + 1):
        product = product * i
    return product

# Harmonic Sum from z + 1 to 400000
def newH(z):
    Sum = 0
    for i in range(1, 400001):
        Sum = Sum + 1/float(z + i)
    return Sum

# The next two are for the third one after...
def in_prod(z):
    array = []
    for i in range(1, 3000000):
        array.append(i * ((exp(1)) ** (z/float(i)))/(float(i) + z))
    return array


def cal(z):
    return prod(in_prod(float(z)))

# Factorial of any real number.
def factorial_real(z):
    if int(z) != z:
        return cal(z) / (float(math.e) ** (euler(1) * z))
    if int(z) == z and z < 0:
        return "Undefined"
    else:
        return factorial(z)

# Gamma Function
def Gamma(a):
    return factorial_real(a - 1)

# Beta Function
def Beta(a, b):
    return Gamma(a) * Gamma(b) / float(Gamma(a + b))

# Lambert W Function
def W(a):
    i = random.randint(0, 200)
    while int(100000 * ((i * (exp(i)) - a) / (i * (exp(i)) + (exp(i))))) != 0:
        i = i - ((i * (exp(i)) - a)/(i * (exp(i)) + (exp(i))))
    if int(100000 * ((i * (exp(i)) - a)/(i * (exp(i)) + (exp(i))))) == 0:
        return i

# Inverse of x^x
def inv_xtothex(a):
    return exp(W(ln(a)))

# Reimann Zeta Function
def ReimannZeta(s):
    Sum = 0
    for i in range(1, 203998):
        if s > 1:
            Sum = Sum + 1 / float(i ** s)
        else:
            return "DNC"

    return Sum


# Digamma Function
def DiGamma(z):
    return H(399999) - euler(z) - newH(z - 1)

# Derivitive of the Gamma Function
def GammaPrime(z):
    return float(DiGamma(z)) * Gamma(z)

# My Personal Constant
def V(z):
    return Gamma(2 + W(inv_xtothex(ReimannZeta(Gamma(2 + W(inv_xtothex(ReimannZeta(1 + euler(z)))))))))

# Cis(x)
def cis(x):
    return str(cos(x)) + " + " + str(sin(x)) + "i"

# Volume of a sphere in the nth dimension
def Volumenthdimension(n):
    return str((pi(2) ** (n/2))/Gamma(n)) + " r^" + str(n)

# Superfactorial - Factorial of factorials
def superfactorial(n):
    array = []
    for i in range(1, n + 1):
        array.append(factorial(i))
    return prod(array)

# Returns x^i for any real x
def x_to_the_i(a):
    return cis(ln(a))

# Combanitorics
def aCb(a, b):
    if a < b:
        return 0
    else:
        return factorial_real(a) / (factorial_real(b) * factorial_real(a - b))
# Permutation
def aPb(a, b):
    if a < b:
        return 0
    else:
        return factorial_real(a) / factorial_real(a - b)

# Returns i^x for any real x
def i_to_the_x(a):
    return cis(pi(a) * a /2)

# Binomial Expansion
def Binomial_Expansion(n):
    s = ""
    for i in range(0, n):
        s += str(int(aCb(n, i))) + " x^" + str(n - i) + " y^" + str(i) + " + "
    s = s + "y^" + str(n)
    return "(x + y)^" + str(n) + " = " + s

def Dearrangement(n):
    sum = 0
    for i in range(2, n + 1):
        sum += ((-1)**i) * (1/float(factorial(i)))
    return int(factorial(n) * sum)

# list(n) = [0, 1, 2, 3, ... , n - 1]
def list(n):
    array = []
    for i in range(0, n):
        array.append(i)
    return array

# test_list(n) = [0, 0, 0, ....]
def test_list(n):
    array = []
    for i in range(0, n):
        array.append(0)
    return array

# Random arrangement of a list from 0 to n - 1
def random_arrange(a):
    array = []
    ar = a.copy()
    for i in range(0, len(a)):
        n = random.randint(0, len(ar) - 1)
        array.append(ar[n])
        ar.pop(n)
    return array

# All possible arrangements/permutations of numbers 0 to n - 1
def all_arrange(a):
    array = []
    count = 0
    while len(array) < factorial(len(a)):
        k = random_arrange(a)
        if k not in array:
            array.append(k)
        if k in array:
            count += 1
    if len(array) == factorial(len(a)):
        return array

# To arrange a list a1 as alloted by the index in a2
def arrange_1_list(a1, a2): # a1 is alnum, a2 is numeric list
    array = test_list(len(a1))
    for i in range(0, len((a1))):
        array[a2[i]] = a1[i]
    return array

# Finally, all permutations of a
def arrange_list(a):
    array = []
    a1 = a
    a2 = list(len(a))
    a3 = all_arrange(a2)
    for i in range(0, len(a3)):
        array.append(arrange_1_list(a1, a3[i]))
    return array
