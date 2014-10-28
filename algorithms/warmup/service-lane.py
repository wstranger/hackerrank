
def find_largest_vehicle(highway, test_case):
    segment = highway[test_case[0]:test_case[1]+1]
    min_vehicle_type = vehicles[0]
    for vt in vehicles:
        if vt <= min(segment):
            min_vehicle_type = vt
    return min_vehicle_type

vehicles = (1,2,3)

test_cases = []

highway_length, test_cases_count = raw_input().split(" ")
highway  = map(int, raw_input().split(" "))
for i in range(int(test_cases_count)):
    test_cases.append(map(int, raw_input().split(" ")))

for case in test_cases:
    print find_largest_vehicle(highway, case)