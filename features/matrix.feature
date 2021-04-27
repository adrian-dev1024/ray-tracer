Feature: Matrices

  Scenario: Constructing and inspecting a 4x4 matrix
    Given the following 4x4 Matrix m:
      | 1    | 2    | 3    | 4    |
      | 5.5  | 6.5  | 7.5  | 8.5  |
      | 9    | 10   | 11   | 12   |
      | 13.5 | 14.5 | 15.5 | 16.5 |
    Then m[0,0] = 1
    And m[0,3] = 4
    And m[1,0] = 5.5
    And m[1,2] = 7.5
    And m[2,2] = 11
    And m[3,0] = 13.5
    And m[3,2] = 15.5

  Scenario: A 2x2 matrix ought to be representable
    Given the following 2x2 Matrix m:
      | -3 | 5  |
      | 1  | -2 |
    Then m[0,0] = -3
    And m[0,1] = 5
    And m[1,0] = 1
    And m[1,1] = -2

  Scenario: A 3x3 matrix ought to be representable
    Given the following 3x3 Matrix m:
      | -3 | 5  | 0  |
      | 1  | -2 | -7 |
      | 0  | 1  | 1  |
    Then m[0,0] = -3
    And m[1,1] = -2
    And m[2,2] = 1

  Scenario: Matrix equality with identical matrices
    Given the following 4x4 Matrix a:
      | 1 | 2 | 3 | 4 |
      | 5 | 6 | 7 | 8 |
      | 9 | 8 | 7 | 6 |
      | 5 | 4 | 3 | 2 |
    And the following 4x4 Matrix b:
      | 1 | 2 | 3 | 4 |
      | 5 | 6 | 7 | 8 |
      | 9 | 8 | 7 | 6 |
      | 5 | 4 | 3 | 2 |
    Then a = b

  Scenario: Matrix equality with different matrices
    Given the following 4x4 Matrix a:
      | 1 | 2 | 3 | 4 |
      | 5 | 6 | 7 | 8 |
      | 9 | 8 | 7 | 6 |
      | 5 | 4 | 3 | 2 |
    And the following 4x4 Matrix b:
      | 2 | 3 | 4 | 5 |
      | 6 | 7 | 8 | 9 |
      | 8 | 7 | 6 | 5 |
      | 4 | 3 | 2 | 1 |
    Then a != b

  Scenario: Multiplying two Matrix 4x4
    Given the following 4x4 Matrix a:
      | 1 | 2 | 3 | 4 |
      | 5 | 6 | 7 | 8 |
      | 9 | 8 | 7 | 6 |
      | 5 | 4 | 3 | 2 |
    And the following 4x4 Matrix b:
      | -2 | 1 | 2 | 3  |
      | 3  | 2 | 1 | -1 |
      | 4  | 3 | 6 | 5  |
      | 1  | 2 | 7 | 8  |
    Then a * b is the following 4x4 Matrix:
      | 20 | 22 | 50  | 48  |
      | 44 | 54 | 114 | 108 |
      | 40 | 58 | 110 | 102 |
      | 16 | 26 | 46  | 42  |

  Scenario: Multiplying two Matrix
    Given the following 2x3 Matrix a:
      | 1 | 2 | 3 |
      | 4 | 5 | 6 |
    And the following 3x2 Matrix b:
      | 7  | 8  |
      | 9  | 10 |
      | 11 | 12 |
    Then a * b is the following 2x2 Matrix:
      | 58  | 64  |
      | 139 | 154 |

  Scenario: A matrix multiplied by a tuple
    Given the following 4x4 Matrix a:
      | 1 | 2 | 3 | 4 |
      | 2 | 4 | 4 | 2 |
      | 8 | 6 | 4 | 1 |
      | 0 | 0 | 0 | 1 |
    And b ← Coordinate(1, 2, 3, 1)
    Then a * b = Coordinate(18, 24, 33, 1)

  Scenario: Multiplying a matrix by the identity matrix
    Given the following 4x4 Matrix a:
      | 0 | 1 | 2  | 4  |
      | 1 | 2 | 4  | 8  |
      | 2 | 4 | 8  | 16 |
      | 4 | 8 | 16 | 32 |
    Then a * identity_matrix = a

  Scenario: Multiplying the identity matrix by a tuple
    Given a ← Coordinate(1, 2, 3, 4)
    Then identity_matrix * a = a

  Scenario: Transposing a matrix
    Given the following 4x4 Matrix a:
      | 0 | 9 | 3 | 0 |
      | 9 | 8 | 0 | 8 |
      | 1 | 8 | 5 | 3 |
      | 0 | 0 | 5 | 8 |
    Then a.transpose() is the following matrix:
      | 0 | 9 | 1 | 0 |
      | 9 | 8 | 8 | 0 |
      | 3 | 0 | 5 | 5 |
      | 0 | 8 | 3 | 8 |

  Scenario: Transposing the identity matrix
    Given a ← identity_matrix.transpose()
    Then a = identity_matrix

  Scenario: Calculating the determinant of a 2x2 matrix
    Given the following 2x2 Matrix a:
      | 1  | 5 |
      | -3 | 2 |
    Then a.determinant() = 17

  Scenario: A sub_matrix of a 3x3 matrix is a 2x2 matrix
    Given the following 3x3 Matrix a:
      | 1  | 5 | 0  |
      | -3 | 2 | 7  |
      | 0  | 6 | -3 |
    Then a.sub_matrix(0, 2) is the following 2x2 matrix:
      | -3 | 2 |
      | 0  | 6 |

  Scenario: A sub_matrix of a 4x4 matrix is a 3x3 matrix
    Given the following 4x4 Matrix a:
      | -6 | 1 | 1  | 6 |
      | -8 | 5 | 8  | 6 |
      | -1 | 0 | 8  | 2 |
      | -7 | 1 | -1 | 1 |
    Then a.sub_matrix(2, 1) is the following 3x3 matrix:
      | -6 | 1  | 6 |
      | -8 | 8  | 6 |
      | -7 | -1 | 1 |

  Scenario: Calculating a minor of a 3x3 Matrix
    Given the following 3x3 Matrix a:
      | 3 | 5  | 0  |
      | 2 | -1 | -7 |
      | 6 | -1 | 5  |
    And b ← a.sub_matrix(1, 0)
    Then b.determinant() = 25
    And a.minor(1, 0) = 25

  Scenario: Calculating a cofactor of a 3x3 Matrix
    Given the following 3x3 Matrix a:
      | 3 | 5  | 0  |
      | 2 | -1 | -7 |
      | 6 | -1 | 5  |
    Then a.minor(0, 0) = -12
    And a.cofactor(0, 0) = -12
    And a.minor(1, 0) = 25
    And a.cofactor(1, 0) = -25

  Scenario: Calculating the determinant of a 3x3 Matrix
    Given the following 3x3 Matrix a:
      | 1  | 2 | 6  |
      | -5 | 8 | -4 |
      | 2  | 6 | 4  |
    Then a.cofactor(0, 0) = 56
    And a.cofactor(0, 1) = 12
    And a.cofactor(0, 2) = -46
    And a.determinant() = -196

  Scenario: Calculating the determinant of a 4x4 Matrix
    Given the following 4x4 Matrix a:
      | -2 | -8 | 3  | 5  |
      | -3 | 1  | 7  | 3  |
      | 1  | 2  | -9 | 6  |
      | -6 | 7  | 7  | -9 |
    Then a.cofactor(0, 0) = 690
    And a.cofactor(0, 1) = 447
    And a.cofactor(0, 2) = 210
    And a.cofactor(0, 3) = 51
    And a.determinant() = -4071

  Scenario: Testing an invertible Matrix for invertibility
    Given the following 4x4 Matrix a:
      | 6 | 4  | 4 | 4  |
      | 5 | 5  | 7 | 6  |
      | 4 | -9 | 3 | -7 |
      | 9 | 1  | 7 | -6 |
    Then a.determinant() = -2120
    And a is invertible

  Scenario: Testing a noninvertible matrix for invertibility
    Given the following 4x4 Matrix a:
      | -4 | 2  | -2 | -3 |
      | 9  | 6  | 2  | 6  |
      | 0  | -5 | 1  | -5 |
      | 0  | 0  | 0  | 0  |
    Then a.determinant() = 0
    And a is not invertible

  Scenario: Calculating the inverse of a matrix
    Given the following 4x4 Matrix a:
      | -5 | 2  | 6  | -8 |
      | 1  | -5 | 1  | 8  |
      | 7  | 7  | -6 | -7 |
      | 1  | -3 | 7  | 4  |
    And b ← a.inverse()
    Then a.determinant() = 532
    And a.cofactor(2, 3) = -160
    And b[3,2] = -160/532
    And a.cofactor(3, 2) = 105
    And b[2,3] = 105/532
    And b is the following 4x4 Matrix:
      | 0.21805   | 0.45113  | 0.24060   | -0.045113 |
      | -0.80827  | -1.45677 | -0.44361  | 0.52068   |
      | -0.078947 | -0.22368 | -0.052632 | 0.19737   |
      | -0.52256  | -0.81391 | -0.30075  | 0.30639   |

  Scenario: Calculating the inverse of another matrix
    Given the following 4x4 Matrix a:
      | 8  | -5 | 9  | 2  |
      | 7  | 5  | 6  | 1  |
      | -6 | 0  | 9  | 6  |
      | -3 | 0  | -9 | -4 |
    Then a.inverse() is the following 4x4 Matrix:
      | -0.15385  | -0.15385 | -0.28205 | -0.53846 |
      | -0.076923 | 0.12308  | 0.025641 | 0.030769 |
      | 0.35897   | 0.35897  | 0.43590  | 0.92308  |
      | -0.69231  | -0.69231 | -0.76923 | -1.92308 |

  Scenario: Calculating the inverse of a third matrix
    Given the following 4x4 Matrix a:
      | 9  | 3  | 0  | 9  |
      | -5 | -2 | -6 | -3 |
      | -4 | 9  | 6  | 4  |
      | -7 | 6  | 6  | 2  |
    Then a.inverse() is the following 4x4 Matrix:
      | -0.040741 | -0.077778 | 0.14444  | -0.22222 |
      | -0.077778 | 0.033333  | 0.36667  | -0.33333 |
      | -0.029012 | -0.14630  | -0.10926 | 0.12963  |
      | 0.17778   | 0.066667  | -0.26667 | 0.33333  |

  Scenario: Multiplying a product by its inverse
    Given the following 4x4 Matrix a:
      |  3 | -9 |  7 |  3 |
      |  3 | -8 |  2 | -9 |
      | -4 |  4 |  4 |  1 |
      | -6 |  5 | -1 |  1 |
    And the following 4x4 Matrix b:
      |  8 |  2 |  2 |  2 |
      |  3 | -1 |  7 |  0 |
      |  7 |  0 |  5 |  4 |
      |  6 | -2 |  0 |  5 |
    And c ← a * b
    Then c * inverse(b) = a