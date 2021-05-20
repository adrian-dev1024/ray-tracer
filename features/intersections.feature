Feature: Intersections

  Scenario: An intersection encapsulates t and object
    Given s ← Sphere()
    When i ← Intersection(3.5, s)
    Then i.t = 3.5
    And i.obj = s

  Scenario: Aggregating intersections
    Given s ← Sphere()
    And i1 ← Intersection(1, s)
    And i2 ← Intersection(2, s)
    When xs ← Intersections(i1, i2)
    Then len(xs) = 2
    And xs[0].t = 1
    And xs[1].t = 2

  Scenario: The hit, when all intersections have positive t
    Given s ← Sphere()
    And i1 ← Intersection(1, s)
    And i2 ← Intersection(2, s)
    And xs ← Intersections(i2, i1)
    When i ← xs.hit()
    Then i = i1

  Scenario: The hit, when some intersections have negative t
    Given s ← Sphere()
    And i1 ← Intersection(-1, s)
    And i2 ← Intersection(1, s)
    And xs ← Intersections(i2, i1)
    When i ← xs.hit()
    Then i = i2

  Scenario: The hit, when all intersections have negative t
    Given s ← Sphere()
    And i1 ← Intersection(-2, s)
    And i2 ← Intersection(-1, s)
    And xs ← Intersections(i2, i1)
    When i ← xs.hit()
    Then i is nothing

  Scenario: The hit is always the lowest nonnegative intersection
    Given s ← Sphere()
    And i1 ← Intersection(5, s)
    And i2 ← Intersection(7, s)
    And i3 ← Intersection(-3, s)
    And i4 ← Intersection(2, s)
    And xs ← Intersections(i1, i2, i3, i4)
    When i ← xs.hit()
    Then i = i4