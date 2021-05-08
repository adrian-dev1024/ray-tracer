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

  Scenario: Rotating a point around the x axis
    Given p ← Point(0, 1, 0)
    And half_quarter ← RotationMatrix(x_radians=π / 4)
    And full_quarter ← RotationMatrix(x_radians=π / 2)
    Then half_quarter * p = Point(0, √2/2, √2/2)
    And full_quarter * p = Point(0, 0, 1)

  Scenario: The inverse of an x-rotation rotates in the opposite direction
    Given p ← Point(0, 1, 0)
    And half_quarter ← RotationMatrix(x_radians=π / 4)
    And inv ← half_quarter.inverse()
    Then inv * p = Point(0, √2/2, -√2/2)

  Scenario: Rotating a point around the y axis
    Given p ← Point(0, 0, 1)
    And half_quarter ← RotationMatrix(y_radians=π / 4)
    And full_quarter ← RotationMatrix(y_radians=π / 2)
    Then half_quarter * p = Point(√2/2, 0, √2/2)
    And full_quarter * p = Point(1, 0, 0)

  Scenario: Rotating a point around the z axis
    Given p ← Point(0, 1, 0)
    And half_quarter ← RotationMatrix(z_radians=π / 4)
    And full_quarter ← RotationMatrix(z_radians=π / 2)
    Then half_quarter * p = Point(-√2/2, √2/2, 0)
    And full_quarter * p = Point(-1, 0, 0)
