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