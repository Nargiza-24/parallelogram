import json
import math

with open('parallelepipeds.json', 'r') as file:
    parallelepipeds = json.load(file)

characteristics = {}
total_volumes = 0
total_surface_areas = 0
total_diagonals = 0
total_alphas = 0
total_betas = 0
total_gammas = 0
total_radii = 0
total_volumes_described_spheres = 0

for key, dimensions in parallelepipeds.items():
    a = float(dimensions['a'])
    b = float(dimensions['b'])
    c = float(dimensions['c'])
    
    volume = a * b * c
    diagonal = math.sqrt(a**2 + b**2 + c**2)
    surface_area = 2 * (a * b + a * c + b * c)
    alpha = math.degrees(math.acos(a / diagonal))
    beta = math.degrees(math.acos(b / diagonal))
    gamma = math.degrees(math.acos(c / diagonal))
    radius_described_sphere = diagonal / 2
    volume_described_sphere = (4 / 3) * math.pi * (radius_described_sphere**3)
    
    characteristics[key] = {
        'diag': str(diagonal),
        'volume': str(volume),
        'surface_area': str(surface_area),
        'alpha': str(alpha),
        'beta': str(beta),
        'gamma': str(gamma),
        'radius_described_sphere': str(radius_described_sphere),
        'volume_described_sphere': str(volume_described_sphere)
    }
    
    total_volumes += volume
    total_surface_areas += surface_area
    total_diagonals += diagonal
    total_alphas += alpha
    total_betas += beta
    total_gammas += gamma
    total_radii += radius_described_sphere
    total_volumes_described_spheres += volume_described_sphere

with open('characteristics.json', 'w') as file:
    json.dump(characteristics, file, indent=4)

total_figures = len(parallelepipeds)
average_volume = total_volumes / total_figures
average_surface_area = total_surface_areas / total_figures
average_diagonal = total_diagonals / total_figures
average_alpha = total_alphas / total_figures
average_beta = total_betas / total_figures
average_gamma = total_gammas / total_figures
average_radius_described_sphere = total_radii / total_figures
average_volume_described_sphere = total_volumes_described_spheres / total_figures

statistics = {
    'avg_diag': str(average_diagonal),
    'avg_volume': str(average_volume),
    'avg_surface_area': str(average_surface_area),
    'avg_alpha': str(average_alpha),
    'avg_beta': str(average_beta),
    'avg_gamma': str(average_gamma),
    'avg_radius_described_sphere': str(average_radius_described_sphere),
    'avg_volume_described_sphere': str(average_volume_described_sphere)
}

with open('statistics.json', 'w') as file:
    json.dump(statistics, file, indent=4)

print(f"Total number of figures: {total_figures}")
print(f"Average volume: {average_volume:.2f}")
print(f"Average surface area: {average_surface_area:.2f}")
print(f"Average diagonal: {average_diagonal:.2f}")
print(f"Average alpha: {average_alpha:.2f}")
print(f"Average beta: {average_beta:.2f}")
print(f"Average gamma: {average_gamma:.2f}")
print(f"Average radius described sphere: {average_radius_described_sphere:.2f}")
print(f"Average volume described sphere: {average_volume_described_sphere:.2f}")
