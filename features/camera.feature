Feature: Camera

  Scenario: Constructing a camera
    Given h_size ← 160
    And v_size ← 120
    And field_of_view ← π/2
    When c ← Camera(h_size, v_size, field_of_view)
    Then c.h_size = 160
    And c.v_size = 120
    And c.field_of_view = π/2
    And c.transform = IdentityMatrix()

  Scenario: The pixel size for a horizontal canvas
    Given c ← Camera(200, 125, π/2)
    Then c.pixel_size = 0.01

  Scenario: The pixel size for a vertical canvas
    Given c ← Camera(125, 200, π/2)
    Then c.pixel_size = 0.01

  Scenario: Constructing a ray through the center of the canvas
    Given c ← Camera(201, 101, π/2)
    When r ← c.ray_for_pixel(100, 50)
    Then r.origin = Point(0, 0, 0)
    And r.direction = Vector(0, 0, -1)

  Scenario: Constructing a ray through a corner of the canvas
    Given c ← Camera(201, 101, π/2)
    When r ← c.ray_for_pixel(0, 0)
    Then r.origin = Point(0, 0, 0)
    And r.direction = Vector(0.66519, 0.33259, -0.66851)

  Scenario: Constructing a ray when the camera is transformed
    Given transform ← rotation_y(π/4) * translation(0, -2, 5)
    And c ← Camera(201, 101, π/2, transform)
    When r ← c.ray_for_pixel(100, 50)
    Then r.origin = Point(0, 2, -5)
    And r.direction = Vector(√2/2, 0, -√2/2)

  Scenario: Rendering a world with a camera
    Given w ← default_world()
    And from ← Point(0, 0, -5)
    And to ← Point(0, 0, 0)
    And up ← Vector(0, 1, 0)
    And pov ← PointOfView(from, to, up)
    And transform ← pov.transform()
    And c ← Camera(11, 11, π/2, transform)
    When canvas ← c.render(w)
    Then canvas.pixel_at(5, 5) = Color(0.38066, 0.47583, 0.2855)