import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load poses from text file
data = np.loadtxt("poses.txt")

arrow_len = 0.3
C = np.diag([1, -1, -1])  # Change coordinates axis

positions = []

# Extract and transform camera positions
for row in data:
    R = row[:9].reshape(3, 3)
    t = row[9:12]
    t_inv = -R.T @ t
    t_corrected = C @ t_inv
    positions.append(t_corrected)

positions = np.array(positions)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-0.2, 0.4])
ax.set_ylim([-0.4, 0.2])
ax.set_zlim([0, 0.6])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.title("Camera trajectory")
plt.ion()

# Draw ground rectangle (baboon)
grid_pts = np.array([[0, 0, 0], [0.185, 0, 0], [0.185, -0.185, 0], [0, -0.185, 0], [0, 0, 0]])
ax.plot(grid_pts[:, 0], grid_pts[:, 1], grid_pts[:, 2], color='gray', linestyle='--')

# Draw coordinate frame at origin
rep_origin = np.array([0, 0, 0])
ax.quiver(*rep_origin, 0.1, 0, 0, color='b')    # X axis
ax.quiver(*rep_origin, 0, -0.1, 0, color='g')   # Y axis
ax.quiver(*rep_origin, 0, 0, 0.1, color='r')    # Z axis

# Plot full camera trajectory
ax.plot(positions[:, 0], positions[:, 1], positions[:, 2], color='purple', linewidth=2)

# Save figure to PNG
fig.savefig("camera_trajectory.png", dpi=300)

plt.ioff()
plt.show()
