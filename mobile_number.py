import re 
def is_valid(mob_num):
    pattern = re.compile("/^(\+|\()\d{2,3}\)?\s\d{2,3}(\s|\-)\d{3,7}\s?(\d{1,3}?\s?(\d{1,3})?$/")
    return pattern.match(mob_num)

mob_num = input("Enter your mobile number: ")

if is_valid(mob_num):
     print(f"{mob_num} is valid mobile number.")
else:
    print(f"{mob_num} is not valid mobile number.")
