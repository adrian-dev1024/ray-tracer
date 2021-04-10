Feature: coordinates

Scenario: A Coordinate with w=1.0 is a point
  Given a ← Coordinate(4.3, -4.2, 3.1, 1.0)
  Then a.x = 4.3
    And a.y = -4.2
    And a.z = 3.1
    And a.w = 1.0
    And a is a point
    And a is not a vector

Scenario: A Coordinate with w=0 is a vector
  Given b ← Coordinate(4.3, -4.2, 3.1, 0.0)
  Then b.x = 4.3
    And b.y = -4.2
    And b.z = 3.1
    And b.w = 0.0
    And b is not a point
    And b is a vector

Scenario: Point() creates tuples with w=1
  Given p ← Point(4, -4, 3)
  Then p = Coordinate(4, -4, 3, 1)

Scenario: Vector() creates tuples with w=0
  Given v ← Vector(4, -4, 3)
  Then v = Coordinate(4, -4, 3, 0)
