def compute_values(lambda_val, phi):
    phi2 = phi * phi
    phi4 = phi2 * phi2
    
    result = [
        lambda_val * (0.8707 - 0.131979 * phi2 + phi4 * (-0.013791 + phi4 * (0.003971 * phi2 - 0.001529 * phi4))),
        phi * (1.007226 + phi2 * (0.015085 + phi4 * (-0.044475 + 0.028874 * phi2 - 0.005916 * phi4)))
    ]
    
    return result

# Example usage:
lambda_val = 1.0  # Replace with actual lambda value
phi = 0.5         # Replace with actual phi value
values = compute_values(lambda_val, phi)
print(values)
