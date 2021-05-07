Feature: Matrix Transformations

  Scenario: Multiplying by a TranslationMatrix matrix
    Given transform ← TranslationMatrix(5, -3, 2)
    And p ← Point(-3, 4, 5)
    Then transform * p = Point(2, 1, 7)

  Scenario: Multiplying by the inverse of a TranslationMatrix matrix
    Given transform ← TranslationMatrix(5, -3, 2)
    And inv ← transform.inverse()
    And p ← Point(-3, 4, 5)
    Then inv * p = Point(-8, 7, 3)

  Scenario: TranslationMatrix does not affect vectors
    Given transform ← TranslationMatrix(5, -3, 2)
    And v ← Vector(-3, 4, 5)
    Then transform * v = v

  Scenario: A scaling matrix applied to a point
    Given transform ← ScalingMatrix(2, 3, 4)
    And p ← Point(-4, 6, 8)
    Then transform * p = Point(-8, 18, 32)

  Scenario: A scaling matrix applied to a vector
    Given transform ← ScalingMatrix(2, 3, 4)
    And v ← Vector(-4, 6, 8)
    Then transform * v = Vector(-8, 18, 32)

  Scenario: Multiplying by the inverse of a scaling matrix
    Given transform ← ScalingMatrix(2, 3, 4)
    And inv ← transform.inverse()
    And v ← Vector(-4, 6, 8)
    Then inv * v = Vector(-2, 2, 2)

  Scenario: Reflection is scaling by a negative value
    Given transform ← ScalingMatrix(-1, 1, 1)
    And p ← Point(2, 3, 4)
    Then transform * p = Point(-2, 3, 4)