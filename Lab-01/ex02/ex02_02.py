# Program to calculate circle area and circumference

# Input radius from user
radius = float(input("Nhập bán kính hình tròn: "))

# Calculate area and circumference 
pi = 3.14159
area = pi * radius * radius 
circumference = 2 * pi * radius

# Display results
print(f"Diện tích hình tròn là: {area:.2f}")
print(f"Chu vi hình tròn là: {circumference:.2f}")