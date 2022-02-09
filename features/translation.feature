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

  Scenario: Individual transformations are applied in sequence
    Given p ← Point(1, 0, 1)
  # apply rotation first
    When p2 ← p.rotate(x_radians=π / 2)
    Then p2 = Point(1, -1, 0)
  # then apply scaling
    When p3 ← p2.scale(5, 5, 5)
    Then p3 = Point(5, -5, 0)
  # then apply translation
    When p4 ← p3.translate(10, 5, 7)
    Then p4 = Point(15, 0, 7)

  Scenario: Chained transformations
    Given p ← Point(1, 0, 1)
    When p2 ← p.rotate(x_radians=π / 2).scale(5, 5, 5).translate(10, 5, 7)
    Then p2 = Point(15, 0, 7)
  Scenario: A shearing transformation moves x in proportion to y
    Given transform ← ShearingMatrix(x_y=1)
    And p ← Point(2, 3, 4)
    Then transform * p = Point(5, 3, 4)

  Scenario: A shearing transformation moves x in proportion to z
    Given transform ← ShearingMatrix(x_z=1)
    And p ← Point(2, 3, 4)
    Then transform * p = Point(6, 3, 4)

  Scenario: A shearing transformation moves y in proportion to x
    Given transform ← ShearingMatrix(y_x=1)
    And p ← Point(2, 3, 4)
    Then transform * p = Point(2, 5, 4)

  Scenario: A shearing transformation moves y in proportion to z
    Given transform ← ShearingMatrix(y_z=1)
    And p ← Point(2, 3, 4)
    Then transform * p = Point(2, 7, 4)

  Scenario: A shearing transformation moves z in proportion to x
    Given transform ← ShearingMatrix(z_x=1)
    And p ← Point(2, 3, 4)
    Then transform * p = Point(2, 3, 6)

  Scenario: A shearing transformation moves z in proportion to y
    Given transform ← ShearingMatrix(z_y=1)
    And p ← Point(2, 3, 4)
    Then transform * p = Point(2, 3, 7)

  Scenario: The transformation matrix for the default orientation
    Given from ← Point(0, 0, 0)
    And to ← Point(0, 0, -1)
    And up ← Vector(0, 1, 0)
    And pov ← PointOfView(from, to, up)
    When t ← pov.transform()
    Then t = IdentityMatrix()

  Scenario: A view transformation matrix looking in positive z direction
    Given from ← Point(0, 0, 0)
    And to ← Point(0, 0, 1)
    And up ← Vector(0, 1, 0)
    And pov ← PointOfView(from, to, up)
    When t ← pov.transform()
    Then t = ScalingMatrix(-1, 1, -1)

  Scenario: The view transformation moves the world
    Given from ← Point(0, 0, 8)
    And to ← Point(0, 0, 0)
    And up ← Vector(0, 1, 0)
    And pov ← PointOfView(from, to, up)
    When t ← pov.transform()
    Then t = TranslationMatrix(0, 0, -8)


  Scenario: An arbitrary view transformation
    Given from ← Point(1, 3, 2)
    And to ← Point(4, -2, 8)
    And up ← Vector(1, 1, 0)
    And pov ← PointOfView(from, to, up)
    When t ← pov.transform()
    Then t is the following 4x4 matrix:
      | -0.50710 | 0.50710 | 0.67613  | -2.3665 |
      | 0.76772  | 0.60610 | 0.12122  | -2.8284 |
      | -0.35857 | 0.59761 | -0.71714 | 0.0001  |
      | 0        | 0       | 0        | 1       |