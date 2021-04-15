Feature: Matrices

  Scenario: Constructing and inspecting a 4x4 matrix
    Given the following 4x4 Matrix m:
      |  1   |  2   |  3   |  4   |
      |  5.5 |  6.5 |  7.5 |  8.5 |
      |  9   | 10   | 11   | 12   |
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
      | -3 |  5 |
      |  1 | -2 |
    Then m[0,0] = -3
    And m[0,1] = 5
    And m[1,0] = 1
    And m[1,1] = -2

  Scenario: A 3x3 matrix ought to be representable
    Given the following 3x3 Matrix m:
      | -3 |  5 |  0 |
      |  1 | -2 | -7 |
      |  0 |  1 |  1 |
    Then m[0,0] = -3
    And m[1,1] = -2
    And m[2,2] = 1

  Scenario: Matrix equality with identical matrices
    Given the following Matrix a:
      | 1 | 2 | 3 | 4 |
      | 5 | 6 | 7 | 8 |
      | 9 | 8 | 7 | 6 |
      | 5 | 4 | 3 | 2 |
    And the following matrix b:
      | 1 | 2 | 3 | 4 |
      | 5 | 6 | 7 | 8 |
      | 9 | 8 | 7 | 6 |
      | 5 | 4 | 3 | 2 |
    Then a = b

  Scenario: Matrix equality with different matrices
    Given the following Matrix a:
      | 1 | 2 | 3 | 4 |
      | 5 | 6 | 7 | 8 |
      | 9 | 8 | 7 | 6 |
      | 5 | 4 | 3 | 2 |
    And the following Matrix b:
      | 2 | 3 | 4 | 5 |
      | 6 | 7 | 8 | 9 |
      | 8 | 7 | 6 | 5 |
      | 4 | 3 | 2 | 1 |
    Then a != b