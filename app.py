# app.py
def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    return a / b  # Notice the bug: We didn't handle division by zero!

if __name__ == "__main__":
    print("2 + 2 =", add_numbers(2, 2))
    print("10 / 2 =", divide_numbers(10, 2))