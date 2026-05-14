def v_gugudan():
    for i in range(1, 10):
        print("\n\n" + str(i) + "단")
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}")


def h_gugudan():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f"{i} x {j} = {i * j}", end = "\t")
        print()
