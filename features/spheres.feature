Feature: Spheres

  Scenario: A ray intersects a sphere at two points
    Given r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And s ← Sphere()
    When xs ← s.intersect(r)
    Then len(xs) = 2
    And xs[0].t = 4.0
    And xs[1].t = 6.0

  Scenario: A ray intersects a sphere at a tangent
    Given r ← Ray(Point(0, 1, -5), Vector(0, 0, 1))
    And s ← Sphere()
    When xs ← s.intersect(r)
    Then len(xs) = 2
    And xs[0].t = 5.0
    And xs[1].t = 5.0

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
    And xs[0].t = -1.0
    And xs[1].t = 1.0

  Scenario: A sphere is behind a ray
    Given r ← Ray(Point(0, 0, 5), Vector(0, 0, 1))
    And s ← Sphere()
    When xs ← s.intersect(r)
    Then len(xs) = 2
    And xs[0].t = -6.0
    And xs[1].t = -4.0

  Scenario: Intersect sets the object on the intersection
    Given r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And s ← Sphere()
    When xs ← s.intersect(r)
    Then len(xs) = 2
    And xs[0].obj = s
    And xs[1].obj = s

  Scenario: A sphere's default transformation
    Given s ← Sphere()
    Then s.transform = IdentityMatrix(4)

  Scenario: Changing a sphere's transformation
    Given s ← Sphere()
    And t ← TranslationMatrix(2, 3, 4)
    When s.transform ← t
    Then s.transform = t

  Scenario: Intersecting a scaled sphere with a ray
    Given r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And s ← Sphere(transform=ScalingMatrix(2, 2, 2))
    When xs ← s.intersect(r)
    Then len(xs) = 2
    And xs[0].t = 3
    And xs[1].t = 7

  Scenario: Intersecting a translated sphere with a ray
    Given r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And s ← Sphere(transform=TranslationMatrix(5, 0, 0))
    When xs ← s.intersect(r)
    Then len(xs) = 0

  Scenario: The normal on a sphere at a point on the x axis
    Given s ← Sphere()
    When n ← s.normal_at(Point(1, 0, 0))
    Then n = Vector(1, 0, 0)

  Scenario: The normal on a sphere at a point on the y axis
    Given s ← Sphere()
    When n ← s.normal_at(Point(0, 1, 0))
    Then n = Vector(0, 1, 0)

  Scenario: The normal on a sphere at a point on the z axis
    Given s ← Sphere()
    When n ← s.normal_at(Point(0, 0, 1))
    Then n = Vector(0, 0, 1)

  Scenario: The normal on a sphere at a nonaxial point
    Given s ← Sphere()
    When n ← s.normal_at(Point(√3/3, √3/3, √3/3))
    Then n = Vector(√3/3, √3/3, √3/3)

  Scenario: The normal is a normalized vector
    Given s ← Sphere()
    When n ← s.normal_at(Point(√3/3, √3/3, √3/3))
    Then n = n.normalize()

  Scenario: Computing the normal on a translated sphere
    Given s ← Sphere(transform=TranslationMatrix(0, 1, 0))
    When n ← s.normal_at(Point(0, 1.70711, -0.70711))
    Then n = Vector(0, 0.70711, -0.70711)

  Scenario: Computing the normal on a transformed sphere
    Given s ← Sphere(transform=RotationMatrix(z_radians=π/5).scale(1, 0.5, 1))
    When n ← s.normal_at(Point(0, √2/2, -√2/2))
    Then n = Vector(0, 0.97014, -0.24254)