Feature: Matrix Transformations

  Scenario: Multiplying by a translation matrix
    Given transform ← Translation(5, -3, 2)
    And p ← Point(-3, 4, 5)
    Then transform * p = Point(2, 1, 7)

  Scenario: Multiplying by the inverse of a translation matrix
    Given transform ← Translation(5, -3, 2)
    And inv ← transform.inverse()
    And p ← Point(-3, 4, 5)
    Then inv * p = Point(-8, 7, 3)

  Scenario: Translation does not affect vectors
    Given transform ← Translation(5, -3, 2)
    And v ← Vector(-3, 4, 5)
    Then transform * v = v
