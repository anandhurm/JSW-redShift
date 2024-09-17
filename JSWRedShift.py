import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulated dataset of galaxies from JWST (for demonstration purposes)
data = {
    'Galaxy_ID': [1, 2, 3, 4, 5],
    'Redshift': [6.3, 5.8, 6.1, 7.0, 5.9],
    'Mass_Msun': [1e10, 2e10, 5e9, 8e10, 4e9],
    'Size_kpc': [2.5, 3.1, 1.9, 4.0, 2.2],
    'Star_Formation_Rate': [15, 12, 9, 20, 13]  # in solar masses per year
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate average mass and size
avg_mass = np.mean(df['Mass_Msun'])
avg_size = np.mean(df['Size_kpc'])

print(f"Average Galaxy Mass: {avg_mass:.2e} Msun")
print(f"Average Galaxy Size: {avg_size:.2f} kpc")

# Visualization: Redshift vs Star Formation Rate
plt.figure(figsize=(8, 5))
plt.scatter(df['Redshift'], df['Star_Formation_Rate'], c='blue', marker='o')
plt.title('Star Formation Rate vs Redshift')
plt.xlabel('Redshift (z)')
plt.ylabel('Star Formation Rate (Msun/yr)')
plt.grid(True)
plt.savefig('star_formation_vs_redshift.png')
plt.show()
