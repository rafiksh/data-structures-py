def boiling_material(boiling_map, boiling_point):
    for element, degree in boiling_map.items():
        if abs(degree) * 1.05 >= abs(boiling_point) >= abs(degree) * 0.95:
            return element
    return 'Unknown'


if __name__ == '__main__':
    print(
        boiling_material({'Nonane': 150.8, 'Gold': 2660, 'Water': 100, 'Silver': 2197, 'Mercury': 357, 'Copper': 1187,
                           'Butane': -0.5, 'Methane': -161.7}, 95))
