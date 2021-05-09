Feature: Scalars

  Scenario: A Scalar with w=1.0 is a point
    Given a ← Scalar(4.3, -4.2, 3.1, 1.0)
    Then a.x = 4.3
    And a.y = -4.2
    And a.z = 3.1
    And a.w = 1.0
    And a is a point
    And a is not a vector

  Scenario: A Scalar with w=0 is a vector
    Given b ← Scalar(4.3, -4.2, 3.1, 0.0)
    Then b.x = 4.3
    And b.y = -4.2
    And b.z = 3.1
    And b.w = 0.0
    And b is not a point
    And b is a vector

  Scenario: Point() creates tuples with w=1
    Given p ← Point(4, -4, 3)
    Then p = Scalar(4, -4, 3, 1)

  Scenario: Vector() creates tuples with w=0
    Given v ← Vector(4, -4, 3)
    Then v = Scalar(4, -4, 3, 0)

  Scenario: Adding two tuples
    Given a1 ← Scalar(3, -2, 5, 1)
    And a2 ← Scalar(-2, 3, 1, 0)
    Then a1 + a2 = Scalar(1, 1, 6, 1)

  Scenario: Subtracting two points
    Given p1 ← Point(3, 2, 1)
    And p2 ← Point(5, 6, 7)
    Then p1 - p2 = Vector(-2, -4, -6)

  Scenario: Subtracting a vector from a point
    Given p1 ← Point(3, 2, 1)
    And v2 ← Vector(5, 6, 7)
    Then p1 - v2 = Point(-2, -4, -6)

  Scenario: Subtracting two vectors
    Given v1 ← Vector(3, 2, 1)
    And v2 ← Vector(5, 6, 7)
    Then v1 - v2 = Vector(-2, -4, -6)

  Scenario: Subtracting a vector from the zero vector
    Given zero ← Vector(0, 0, 0)
    And v ← Vector(1, -2, 3)
    Then zero - v = Vector(-1, 2, -3)

  Scenario: Negating a tuple
    Given a ← Scalar(1, -2, 3, -4)
    Then -a = Scalar(-1, 2, -3, 4)

  Scenario: Multiplying a Scalar by a scalar
    Given a ← Scalar(1, -2, 3, -4)
    Then a * 3.5 = Scalar(3.5, -7, 10.5, -14)

  Scenario: Multiplying a Scalar by a fraction
    Given a ← Scalar(1, -2, 3, -4)
    Then a * 0.5 = Scalar(0.5, -1, 1.5, -2)

  Scenario: Dividing a Scalar by a scalar
    Given a ← Scalar(1, -2, 3, -4)
    Then a / 2 = Scalar(0.5, -1, 1.5, -2)

  Scenario: Computing the magnitude of Vector(1, 0, 0)
    Given v ← Vector(1, 0, 0)
    Then v.magnitude() = 1

  Scenario: Computing the magnitude of Vector(0, 1, 0)
    Given v ← Vector(0, 1, 0)
    Then v.magnitude() = 1

  Scenario: Computing the magnitude of Vector(0, 0, 1)
    Given v ← Vector(0, 0, 1)
    Then v.magnitude() = 1

  Scenario: Computing the magnitude of Vector(1, 2, 3)
    Given v ← Vector(1, 2, 3)
    Then v.magnitude() = √14

  Scenario: Computing the magnitude of Vector(-1, -2, -3)
    Given v ← Vector(-1, -2, -3)
    Then v.magnitude() = √14

  Scenario: Normalizing Vector(4, 0, 0) gives (1, 0, 0)
    Given v ← Vector(4, 0, 0)
    Then v.normalize() = Vector(1, 0, 0)

  Scenario: Normalizing Vector(1, 2, 3)
    Given v ← Vector(1, 2, 3)
                                     # vector(1/√14,   2/√14,   3/√14)
    Then v.normalize() = approximately Vector(0.26726, 0.53452, 0.80178)
    And v.normalize() = Vector(1/√14, 2/√14, 3/√14)

  Scenario: The magnitude of a normalized Vector
    Given v ← Vector(1, 2, 3)
    When norm ← v.normalize()
    Then norm.magnitude() = 1

  Scenario: The dot product of two Vectors
    Given a ← Vector(1, 2, 3)
    And b ← Vector(2, 3, 4)
    Then a.dot(b) = 20

  Scenario: The cross product of two Vectors
    Given a ← Vector(1, 2, 3)
    And b ← Vector(2, 3, 4)
    Then a.cross(b) = Vector(-1, 2, -1)
    And b.cross(a) = Vector(1, -2, 1)