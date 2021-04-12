Feature: Canvas

  Scenario: Creating a Canvas
    Given c ← Canvas(10, 20)
    Then c.width = 10
    And c.height = 20
    And every pixel of c is Color(0, 0, 0)

  Scenario: Writing pixels to a Canvas
    Given c ← Canvas(10, 20)
    And red ← Color(1, 0, 0)
    When c.write_pixel(2, 3, red)
    Then c.pixel_at(2, 3) = red