units = [[55,65,75],[120,150,170],[210,230,240]]
def costslab1(units):
    first_slab_rate = 10
    print("Bill for Slab 1 is")
    for u in units[0]:
        print(u*first_slab_rate,end="\t")
    print()

def costslab2(units):
    second_slab_rate = 15
    print("Bill for Slab 2 is")
    for u in units[0]:
        print(u*second_slab_rate,end="\t")
    print()


def costslab3(units):
    third_slab_rate = 15
    print("Bill for Slab 3 is")
    for u in units[0]:
        print(u*third_slab_rate,end="\t")
    print()

def main():
    print("student_id : XYZ12345")
    n = int(input("Press 1 for slab 1 & 2 Bill\nPress 2 for slab 3 Bill\n"))
    if n == 1:
        costslab1(units)
        costslab2(units)
    elif n == 2:
        costslab3(units)
main()