from app.calculator import add, subtract

if __name__ == "__main__":
    x, y = 1, 2.1

    ans1 = add(x, y)
    ans2 = subtract(x, y)
    print(ans1, ans2)
