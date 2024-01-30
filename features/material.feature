Feature: Materials

  Background:
    Given m ← Material()
    And position ← Point(0, 0, 0)

  Scenario: The default material
#    Given m ← Material()
    Then m.color = Color(1, 1, 1)
    And m.ambient = 0.1
    And m.diffuse = 0.9
    And m.specular = 0.9
    And m.shininess = 200.0

  Scenario: Lighting with the eye between the light and the surface
    Given eye_v ← Vector(0, 0, -1)
    And normal_v ← Vector(0, 0, -1)
    And light ← LightSource(Point(0, 0, -10), Color(1, 1, 1))
    When result ← m.lighting(light, position, eye_v, normal_v)
    Then result = Color(1.9, 1.9, 1.9)

  Scenario: Lighting with the eye between light and surface, eye offset 45°
    Given eye_v ← Vector(0, √2/2, -√2/2)
    And normal_v ← Vector(0, 0, -1)
    And light ← LightSource(Point(0, 0, -10), Color(1, 1, 1))
    When result ← m.lighting(light, position, eye_v, normal_v)
    Then result = Color(1.0, 1.0, 1.0)

  Scenario: Lighting with eye opposite surface, light offset 45°
    Given eye_v ← Vector(0, 0, -1)
    And normal_v ← Vector(0, 0, -1)
    And light ← LightSource(Point(0, 10, -10), Color(1, 1, 1))
    When result ← m.lighting(light, position, eye_v, normal_v)
    Then result = Color(0.7364, 0.7364, 0.7364)

  Scenario: Lighting with eye in the path of the reflection vector
    Given eye_v ← Vector(0, -√2/2, -√2/2)
    And normal_v ← Vector(0, 0, -1)
    And light ← LightSource(Point(0, 10, -10), Color(1, 1, 1))
    When result ← m.lighting(light, position, eye_v, normal_v)
    Then result = Color(1.6364, 1.6364, 1.6364)

  Scenario: Lighting with the light behind the surface
    Given eye_v ← Vector(0, 0, -1)
    And normal_v ← Vector(0, 0, -1)
    And light ← LightSource(Point(0, 0, 10), Color(1, 1, 1))
    When result ← m.lighting(light, position, eye_v, normal_v)
    Then result = Color(0.1, 0.1, 0.1)

  Scenario: Lighting with the surface in shadow
    Given eye_v ← Vector(0, 0, -1)
    And normal_v ← Vector(0, 0, -1)
    And light ← LightSource(Point(0, 0, -10), Color(1, 1, 1))
    And in_shadow ← true
    When result ← m.lighting(light, position, eye_v, normal_v, in_shadow)
    Then result = Color(0.1, 0.1, 0.1)
