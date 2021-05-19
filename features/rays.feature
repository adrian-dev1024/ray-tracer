Feature: Rays

  Scenario: Creating and querying a ray
    Given origin ← Point(1, 2, 3)
    And direction ← Vector(4, 5, 6)
    When r ← Ray(origin, direction)
    Then r.origin = origin
    And r.direction = direction

  Scenario: Computing a point from a distance
    Given r ← Ray(Point(2, 3, 4), Vector(1, 0, 0))
    Then r.position(0) = Point(2, 3, 4)
    And r.position(1) = Point(3, 3, 4)
    And r.position(-1) = Point(1, 3, 4)
    And r.position(2.5) = Point(4.5, 3, 4)