
case = [["A1", "Compact", 75.0], ["A2", "Tower", 150.0]]
ram = [["B1", "8GB", 79.99],["B2", "16GB", 149.99],["B3", "32GB", 299.99]]
hdd1 = [["C1", "1TB HDD", 49.99],["C2", "2TB HDD", 89.99],["C3", "4TB HDD", 129.99]]
ssd = [["D1", "240GB SSD", 59.99],["D2", "480GB SSD", 119.99]]
hdd2 = [["E1", "1TB HDD", 49.99],["E2", "2TB HDD", 89.99],["E3", "4TB HDD", 129.99]]
od = [["F1", "DVD Blu-Ray Player", 50.0],["F2", "DVD Blu-Ray Re-writer", 100.0]]
os = [["G1", "Standard Version", 100.0],["G2", "Professional Version", 175.0]]

components = [case, ram, hdd1, ssd, hdd2, od, os]


def body_case(components):
    while True:
        print("Case?")

        incase = int(input("1. Tower\n2. Compact\n"))

        if incase == 1:
            if case[0] not in build:
                build.append(case[0])
            break
        elif incase == 2:
            if case[1] not in build:
                build.append(case[1])
            break
        else:
            print("Invalid Choice, Choose again.")

def body_ram(components):
    while True:
        print("Ram?")

        incase = int(input("1. 8GB\n2. 16GB\n3. 32GB\n"))

        if incase == 1:
            if ram[0] not in build:
                build.append(ram[0])
            break
        elif incase == 2:
            if ram[1] not in build:
                build.append(ram[1])
            break
        elif incase == 3:
            if ram[2] not in build:
                build.append(ram[2])
            break
        else:
            print("Invalid Choice, Choose again.")


def first_hdd(components):
    while True:
        print("1st HDD?")

        incase = int(input("1. 1TB\n2. 2TB\n3. 4TB\n"))

        if incase == 1:
            if ram[0] not in build:
                build.append(hdd1[0])
            break
        elif incase == 2:
            if ram[1] not in build:
                build.append(hdd1[1])
            break
        elif incase == 3:
            if ram[2] not in build:
                build.append(hdd1[2])
            break
        else:
            print("Invalid Choice, Choose again.")


def body_ssd(components):
    while True:
        print("SSD?")

        incase = int(input("1. 240GB\n2. 480GB\n"))

        if incase == 1:
            if ssd[0] not in build:
                build.append(ssd[0])
            break
        elif incase == 2:
            if ssd[1] not in build:
                build.append(ssd[1])
            break
        else:
            print("Invalid Choice, Choose again.")



def second_hdd(components):
    while True:
        print("2nd HDD?")

        incase = int(input("1. 1TB\n2. 2TB\n"))

        if incase == 1:
            if hdd2[0] not in build:
                build.append(hdd2[0])
            break
        elif incase == 2:
            if hdd2[0] not in build:
                build.append(hdd2[1])
            break
        else:
            print("Invalid Choice, Choose again.")
def body_od(components):
    while True:
        print("Optical Drive?")

        incase = int(input("1. Blu-Ray Player\n2. Blu-Ray Re-writer\n"))

        if incase == 1:
            if od[0] not in build:
                build.append(od[0])
            break
        elif incase == 2:
            if od[1] not in build:
                build.append(od[1])
            break
        else:
            print("Invalid Choice, Choose again.")


def body_os(components):
    while True:
        print("Operating System?")

        incase = int(input("1. Standard Version\n2. Professional Version\n3. Not Required\n"))

        if incase == 1:
            if os[0] not in build:
                build.append(os[0])
            break
        elif incase == 2:
            if os[1] not in build:
                build.append(os[1])
            break
        else:
            break


def add_req(components):
    add_count = 0
    while True:
        add_requ = int(input("Any additional requirement?\n"
                             "1. Yes\n2. No\n"))
        if add_requ == 1:
            print(f'Which Category?\n'
                  f'1. Case\n'
                  f'2. Ram\n'
                  f'3. 1st HDD\n'
                  f'4. SSD\n'
                  f'4. 2nd HDD\n'
                  f'5. Optical Drive\n'
                  f'6. Operating System\n')

            n = int(input())
            if n == 1:
                body_case(components)
            elif n == 2:
                body_ram(components)
            elif n == 3:
                first_hdd(components)
            elif n == 4:
                body_ssd(components)
            elif n == 5:
                second_hdd(components)
            elif n == 6:
                body_os(components)
            add_count += 1
        else:
            print("\nYour Build Details:\n")
            total = 0
            for i in build:
                for k in i:
                    print(k, end="\t\t")
                    if type(k) == float:
                        total += k
                print()
            print("Total : ", total)

            if add_count == 1:
                print("Discounted Total",total - (total*(5/100)))
            elif add_count > 1:
                print("Discounted Total", total - (total * (10/100)))
            break


# Start of Prompt

build = []
print("Choose your build!")

body_case(components)
body_ram(components)
first_hdd(components)
body_ssd(components)
second_hdd(components)
body_od(components)
body_os(components)

add_req(components)

