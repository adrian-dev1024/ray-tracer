Feature: World

  Scenario: Creating a world
    Given w ← World()
    Then w contains no shapes
    And w has no light source

  Scenario: The default world
    Given light_source ← LightSource(Point(-10, 10, -10), Color(1, 1, 1))
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

  Scenario: Shading an intersection
    Given w ← default_world()
    And r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And shape ← the first object in w
    And i ← Intersection(4, shape)
    When comps ← i.pre_compute(r)
    And c ← w.shade_hit(comps)
    Then c = Color(0.38066, 0.47583, 0.2855)

  Scenario: Shading an intersection from the inside
    Given w ← default_world()
    And w.light_source ← LightSource(Point(0, 0.25, 0), Color(1, 1, 1))
    And r ← Ray(Point(0, 0, 0), Vector(0, 0, 1))
    And shape ← the second object in w
    And i ← Intersection(0.5, shape)
    When comps ← i.pre_compute(r)
    And c ← w.shade_hit(comps)
    Then c = Color(0.90498, 0.90498, 0.90498)

  Scenario: The color when a ray misses
    Given w ← default_world()
    And r ← Ray(Point(0, 0, -5), Vector(0, 1, 0))
    When c ← w.color_at(r)
    Then c = Color(0, 0, 0)

  Scenario: The color when a ray hits
    Given w ← default_world()
    And r ← Ray(Point(0, 0, -5), Vector(0, 0, 1))
    When c ← w.color_at(r)
    Then c = Color(0.38066, 0.47583, 0.2855)

  Scenario: There is no shadow when nothing is collinear with point and light
    Given w ← default_world()
    And p ← Point(0, 10, 0)
    Then w.is_in_shadow(p) is false

  Scenario: The shadow when an object is between the point and the light
    Given w ← default_world()
    And p ← Point(10, -10, 10)
    Then w.is_in_shadow(p) is true

  Scenario: There is no shadow when an object is behind the light
    Given w ← default_world()
    And p ← Point(-20, 20, -20)
    Then w.is_in_shadow(p) is false

  Scenario: There is no shadow when an object is behind the point
    Given w ← default_world()
    And p ← Point(-2, 2, -2)
    Then w.is_in_shadow(p) is false

    # TODO Look into why if this is moved after test below the test fails!?!
  @wip
  Scenario: shade_hit() is given an intersection in shadow
    Given light ← LightSource(Point(0, 0, -10), Color(1, 1, 1))
    And w1 ← World(light)
    And s1 ← Sphere()
    And s1 is added to w1
    And s2 ← Sphere(TranslationMatrix(0, 0, 10))
    And s2 is added to w1
    And r ← Ray(Point(0, 0, 5), Vector(0, 0, 1))
    And i ← Intersection(4, s2)
    When c ← w1.shade_hit(i.pre_compute(r))
    Then c = Color(0.1, 0.1, 0.1)

  Scenario: The color with an intersection behind the ray
    Given w ← default_world()
    And outer ← the first object in w
    And outer.material.ambient ← 1
    And inner ← the second object in w
    And inner.material.ambient ← 1
    And r ← Ray(Point(0, 0, 0.75), Vector(0, 0, -1))
    When c ← w.color_at(r)
    Then c = inner.material.color