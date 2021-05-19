Feature: Spheres

  Scenario: A ray intersects a sphere at two points
    Given r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And s ← Sphere()
    When xs ← s.intersect(r)
    Then len(xs) = 2
    And xs[0] = 4.0
    And xs[1] = 6.0

  Scenario: A ray intersects a sphere at a tangent
    Given r ← Ray(Point(0, 1, -5), Vector(0, 0, 1))
    And s ← Sphere()
    When xs ← s.intersect(r)
    Then len(xs) = 2
    And xs[0] = 5.0
    And xs[1] = 5.0

  Scenario: A ray misses a sphere
    Given r ← Ray(Point(0, 2, -5), Vector(0, 0, 1))
    And s ← Sphere()
    When xs ← s.intersect(r)
    Then len(xs) = 0

  Scenario: A ray originates inside a sphere
    Given r ← Ray(Point(0, 0, 0), Vector(0, 0, 1))
    And s ← Sphere()
    When xs ← s.intersect(r)
    Then len(xs) = 2
    And xs[0] = -1.0
    And xs[1] = 1.0

  Scenario: A sphere is behind a ray
    Given r ← Ray(Point(0, 0, 5), Vector(0, 0, 1))
    And s ← Sphere()
    When xs ← s.intersect(r)
    Then len(xs) = 2
    And xs[0] = -6.0
    And xs[1] = -4.0