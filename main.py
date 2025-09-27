import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def main():
    print("Circle Area Calculator")
    try:
        radius = float(input("Enter radius: "))
        area = calculate_circle_area(radius)
        print(f"Area: {area:.2f}")
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
