import sys
from unittest import result

first_number = int(sys.argv[1])
second_number = int(sys.argv[2])
result_sum = first_number + second_number

if result_sum <= 0:
    print("You have chosen the path of destitution.")
elif result_sum > 0 and result_sum <= 100:
    print("You chosen the path of plenty")
else:
    print("You chosem the path of excess")