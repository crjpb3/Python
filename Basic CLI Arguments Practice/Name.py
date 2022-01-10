import sys

num_of_args = len(sys.argv) - 1
required_num_of_args = 2

if  num_of_args < required_num_of_args:
    sys.exit("\n\tMissing Arguments: Requires <First Name> <Last Name>")

if num_of_args > required_num_of_args:
    sys.exit("\n\tToo Many Arguments: <First Name> <Last Name> Only")

full_name = sys.argv[1] + ' ' + sys.argv[2]

print("Hello", full_name)
