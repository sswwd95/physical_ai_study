temperatures = [29.1, 29.5, 30.2, 31.8, 33.4, 32.9]
threshold = 32.0

for index, value in enumerate(temperatures):
    if value > threshold:
        print(f"경고: index={index}, temperature={value} C")
