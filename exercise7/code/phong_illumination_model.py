
# Phong Illumination Model for a 3D Object

import numpy as np
import matplotlib.pyplot as plt

# Get user inputs
print("PHONG ILLUMINATION MODEL")

ka = float(input("Enter ambient coefficient (ka, 0-1): "))
kd = float(input("Enter diffuse coefficient (kd, 0-1): "))
ks = float(input("Enter specular coefficient (ks, 0-1): "))
Ia = float(input("Enter ambient light intensity: "))
Il = float(input("Enter point light intensity: "))
shininess = float(input("Enter shininess exponent: "))

# Light and viewer positions
light = np.array([2.0, 2.0, 3.0])
viewer = np.array([0.0, 0.0, 3.0])

# Create sphere
u = np.linspace(0, 2 * np.pi, 150)
v = np.linspace(0, np.pi, 100)

x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones_like(u), np.cos(v))

# Normalize surface normals
normals = np.stack((x, y, z), axis=-1)

# Normalize light and viewer vectors
light_vectors = light - normals
light_vectors /= np.linalg.norm(
    light_vectors, axis=-1, keepdims=True
)

view_vectors = viewer - normals
view_vectors /= np.linalg.norm(
    view_vectors, axis=-1, keepdims=True
)

# Ambient component
ambient = ka * Ia

# Diffuse component: kd * Il * max(N.L, 0)
ndotl = np.sum(normals * light_vectors, axis=-1)
diffuse = kd * Il * np.maximum(ndotl, 0)

# Reflection vector: R = 2(N.L)N - L
reflection = (
    2 * ndotl[..., np.newaxis] * normals - light_vectors
)

reflection /= np.maximum(
    np.linalg.norm(reflection, axis=-1, keepdims=True),
    1e-10
)

# Specular component: ks * Il * max(R.V, 0)^n
rdotv = np.sum(reflection * view_vectors, axis=-1)
specular = ks * Il * np.maximum(rdotv, 0) ** shininess

# Total intensity
intensity = ambient + diffuse + specular
intensity = np.clip(intensity, 0, 1)

# Display shaded 3D sphere
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(
    x, y, z,
    facecolors=plt.cm.coolwarm(intensity),
    rstride=1,
    cstride=1,
    linewidth=0,
    antialiased=True,
    shade=False
)

ax.set_title("Phong Illumination Model")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_box_aspect([1, 1, 1])

plt.tight_layout()
plt.show()

print("\nPhong illumination model implemented successfully!")
print("Ambient intensity:", round(ambient, 3))
print("Average diffuse intensity:", round(np.mean(diffuse), 3))
print("Average specular intensity:", round(np.mean(specular), 3))
