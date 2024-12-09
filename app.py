import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Judul aplikasi
st.title("WILMA NUR FATIMAH")

# Penjelasan aplikasi
st.write("Data acak yang berubah setiap tombol ditekan.")

# Fungsi untuk membuat data acak
def generate_random_data():
    n = 100
    angles = np.linspace(0, 2 * np.pi, n)
    radii = np.random.rand(n)
    x = radii * np.cos(angles)
    y = radii * np.sin(angles)
    sizes = np.random.rand(n) * 300
    colors = np.random.rand(n)
    return x, y, sizes, colors

# Tombol untuk memperbarui data
if st.button("Generate New Data"):
    # Generate data baru ketika tombol ditekan
    x, y, sizes, colors = generate_random_data()
else:
    # Generate data awal saat aplikasi pertama kali dibuka
    x, y, sizes, colors = generate_random_data()

# Buat plot dengan data
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(x, y, s=sizes, c=colors, alpha=0.5)
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.grid(True, linestyle='--', alpha=0.5)

# Tambahkan nama dan judul di atas grafik
fig.suptitle("Fisika Komputasi Awan\nWILMA NUR FATIMAH", fontsize=14, fontweight='bold')

# Tampilkan grafik di Streamlit
st.pyplot(fig)
