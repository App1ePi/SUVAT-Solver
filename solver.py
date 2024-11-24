import math

modes = {1: "Simple Motion", 2: "Projected From Floor", 3: "Projected Upwards From Floor", 4: "Projected From Ledge",
         5: "Dropped From Ledge", 6: "Projected Upwards From Point"}


def simple_motion():
    print("Welcome to Simple Motion")
    s = input("S: ").lower()
    u = input("U: ").lower()
    v = input("V: ").lower()
    a = input("A: ").lower()
    t = input("T: ").lower()

    if s == "none" and u == "none":
        s = (float(v) * float(t)) - (0.5 * float(a) * math.pow(float(t), 2))
        u = float(v) - (float(a) * float(t))
        s = float(s).__round__(5)
        u = float(u).__round__(5)
        print(f"S: {s}, U: {u}, V: {v}, A: {a}, T: {t}")

    if s == "none" and v == "none":
        s = (float(u) * float(t)) + (0.5 * float(a) * math.pow(float(t), 2))
        v = math.sqrt(math.pow(float(u), 2) + (2 * float(a) * float(s)))
        s = float(s).__round__(5)
        v = float(v).__round__(5)
        print(f"S: {s}, U: {u}, V: +/-{v}, A: {a}, T: {t}")

    if s == "none" and a == "none":
        a = (float(v) - float(u)) / float(t)
        s = (float(u) * float(t)) + (0.5 * float(a) * math.pow(float(t), 2))
        s = float(s).__round__(5)
        a = float(a).__round__(5)
        print(f"S: {s}, U: {u}, V: {v}, A: {a}, T: {t}")

    if s == "none" and t == "none":
        s = ((float(v) + float(u)) / 2) * float(t)
        t = (float(v) - float(u)) / float(a)
        s = float(s).__round__(5)
        t = float(t).__round__(5)
        print(f"S: {s}, U: {u}, V: {v}, A: {a}, T: {t}")

    if u == "none" and v == "none":
        u = (float(s) - (0.5 * float(a) * math.pow(float(t), 2)))
        v = (float(u) + (float(a) * float(t)))
        u = float(u).__round__(5)
        v = float(v).__round__(5)
        print(f"S: {s}, U: {u}, V: {v}, A: {a}, T: {t}")

    if u == "none" and a == "none":
        u = ((float(s) / float(t)) * 2) - float(v)
        a = (float(v) - float(u)) / float(t)
        u = float(u).__round__(5)
        a = float(a).__round__(5)
        print(f"S: {s}, U: {u}, V: {v}, A: {a}, T: {t}")

    if u == "none" and t == "none":
        u = math.sqrt(math.pow(float(v), 2) - (float(a) * float(s) * 2))
        t = (float(v) - float(u)) / float(a)
        t2 = (float(v) - float(-u)) / float(a)
        u = float(u).__round__(5)
        t = float(t).__round__(5)
        t2 = float(t2).__round__(5)
        print(f"S: {s}, U: +/-{u}, V: {v}, A: {a}, T1: {t}, T2: {t2}")

    if v == "none" and a == "none":
        v = 2 * (float(s) / float(t)) - float(u)
        a = (float(v) - float(u)) / float(t)
        v = float(v).__round__(5)
        a = float(a).__round__(5)
        print(f"S: {s}, U: {u}, V: {v}, A: {a}, T: {t}")

    if v == "none" and t == "none":
        v = math.sqrt(math.pow(float(u), 2) + (2 * float(a) * float(s)))
        t1 = (float(v) - float(u)) / float(a)
        t2 = (float(-v) - float(u)) / float(a)
        v = float(v).__round__(5)
        t1 = float(t1).__round__(5)
        t2 = float(t2).__round__(5)
        print(f"S: {s}, U: {u}, V: +/-{v}, A: {a}, T1: {t1}, T2: {t2}")

    if a == "none" and t == "none":
        a = (math.pow(float(v), 2) - math.pow(float(u), 2)) / (float(s) * 2)
        t = (float(v) - float(u)) / float(a)
        a = float(a).__round__(5)
        t = float(t).__round__(5)
        print(f"S: {s}, U: {u}, V: {v}, A: {a}, T: {t}")


print("""
        1) Simple Motion                2) Projected from floor             3) Projected Upwards from floor
        |=================|             |=================|                 |=================|
        |                 |             |                 |                 |  ^              |
        |    ________     |             |                 |                 |  |              |
        |   /        \    |             |    @ -->        |                 |  |              |
        |  /          \   |             |                 |                 |  |              |
        | @            \  |             |                 |                 | @               |
        |_________________|             |_________________|                 |_________________|  
                 
    
        4) Projected from Ledge         5) Dropped from Ledge               6) Projected Upwards from Point
        |=================|             |=================|                 |=================|
        |   ___           |             |                 |                 |  ^              |
        |  /   \          |             |                 |                 |  |              |
        |_@_    \         |             |__@____          |                 | @               |
        |  |     \        |             |  |    \         |                 |  |              |
        |  |      \       |             |  |     \        |                 |  |              |
        |__|______________|             |__|______\_______|                 |_________________|""")

while True:
    calculator_mode = input("Your Selection: ")
    try:
        val = int(calculator_mode)
        if 0 < val < 7:
            print(f"You have selected Mode {val}: {modes[val]}")
            break
        else:
            print(f"ValueError: Value given '{val}' is not in range calculator_modes - ErrorCode MCRE")
    except ValueError:
        print(f"ValueError: Value given '{calculator_mode}' is not an integer - ErrorCode MCIE")

if val == 1:
    simple_motion()


