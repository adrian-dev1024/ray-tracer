Feature: World

  Scenario: Creating a world
    Given w ← World()
    Then w contains no objects
    And w has no light source

  Scenario: The default world
    Given light_source ← LightPoint(Point(-10, 10, -10), Color(1, 1, 1))
    And s1 ← Sphere(material=Material(color=Color(0.8, 1.0, 0.6), diffuse=0.7, specular=0.2)
    And s2 ← Sphere(transform=ScalingMatrix(0.5, 0.5, 0.5))
    When w ← default_world()
    Then w.light_source = light_source
    And w contains s1
    And w contains s2

  Scenario: Intersect a world with a ray
    Given w ← default_world()
    And r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))
    When xs ← w.intersect(r)
    Then len(xs) = 4
    And xs[0].t = 4
    And xs[1].t = 4.5
    And xs[2].t = 5.5
    And xs[3].t = 6