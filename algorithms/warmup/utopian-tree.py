def grow(height, c):
    if c <= 0:
        return height
    elif c == 1:
        return height * 2;
    else:
        return grow(height*2+1, c-2)


test_cases = input()

grows_cycles = []
for tc in range(0, test_cases):
    cycles = input()
    grows_cycles.append(cycles)

for cycles in grows_cycles:
    print grow(1, cycles)