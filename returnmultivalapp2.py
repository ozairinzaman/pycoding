def cube(side):
    volume = side **3
    surface_area = 6 * (side**2)
    return volume, surface_area

returned_values = cube(8)
print(returned_values)

print("\n")

volume, area = cube(6.5)
print(f"Volume of the cube is {volume} cubic units and the total surface area is {area} sq. units\n")