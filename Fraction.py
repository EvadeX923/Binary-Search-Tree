class Fraction:

  def __init__(self, numerator, denominator):
    if denominator == 0:
      raise ZeroDivisionError
    self.__n = numerator
    self.__d = denominator
    self.__reduce()

  @staticmethod
  def gcd(n, d):
    while d != 0:
      t = d
      d = n % d
      n = t
    return n

  def __reduce(self):
    if self.__n < 0 and self.__d < 0:
      self.__n = self.__n * -1
      self.__d = self.__d * -1

    divisor = Fraction.gcd(self.__n, self.__d)
    self.__n = self.__n // divisor
    self.__d = self.__d // divisor

  def __add__(self, addend):
    num = self.__n * addend.__d + self.__d * addend.__n
    den = self.__d * addend.__d
    return Fraction(num, den)

  def __sub__(self, subtrahend):
    num = self.__n * subtrahend.__d - self.__d * subtrahend.__n
    den = self.__d * subtrahend.__d
    return Fraction(num, den)

  def __mul__(self, multiplicand):
    num = self.__n * multiplicand.__n
    den = self.__d * multiplicand.__d
    return Fraction(num, den)

  def __truediv__(self, divisor):
    if divisor.__n == 0:
      raise ZeroDivisionError
    num = self.__n * divisor.__d
    den = self.__d * divisor.__n
    return Fraction(num, den)

  def __lt__(self, other):
    return (self.__n * other.__d) < (self.__d * other.__n)

  def __gt__(self, other):
    return (self.__n * other.__d) > (self.__d * other.__n)

  def __eq__(self, other):
    return (self.__n * other.__d) == (self.__d * other.__n)

  def to_float(self):
    return self.__n / self.__d

  def __str__(self):
    return str(self.__n) + '/' + str(self.__d)

  def __repr__(self):
    return str(self)

if __name__ == '__main__':
    fractions = []
    fractions.append(Fraction(4, 5))
    fractions.append(Fraction(7, 2))
    fractions.append(Fraction(3, 5))
    fractions.append(Fraction(1, 4))
    fractions.append(Fraction(25, 26))
    fractions.append(Fraction(1, 12))
    fractions.append(Fraction(2, 5))
    fractions.append(Fraction(7, 10))
    fractions.append(Fraction(4, 8))
    fractions.append(Fraction(11, 19))
    fractions.append(Fraction(1, 5))
    fractions.append(Fraction(13, 16))
    bst = Binary_Search_Tree()
    for f in fractions:
        bst.insert_element(f)
    print(fractions)
    print(bst.to_list())