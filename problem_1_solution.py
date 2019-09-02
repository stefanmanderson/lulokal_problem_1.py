my_strings = input()

my_strings_split = my_strings.split(",")
my_strings_split_sort = sorted(my_strings_split)

print(",".join(my_strings_split_sort))
