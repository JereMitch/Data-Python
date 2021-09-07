open_file = open('Cupcakeinvoices.csv')
for order in open_file:
    order = order.rstrip('\n').split(',')
    print(order[2])

open_file.seek(0)

for line in open_file:
    value = line.rstrip('\n').split(',')
    total = int(value[3]) * float(value[4])
    print(total)
    
open_file.seek(0)

total = 0

for line in open_file:
    value = line.rstrip('\n').split(',')
    total += int(value[3]) * float(value[4])

print(total)


open_file.seek(0)
total_chocolate = 0
total_strawberry = 0
total_vanilla = 0
total_orders = 0

for line in open_file:
    value = line.rstrip('\n').split(',')
    for flavor in value:
        if flavor == 'Chocolate':
            total_chocolate += 1
        elif flavor == 'Vanilla':
            total_vanilla += 1
        elif flavor == 'Strawberry':
            total_strawberry += 1
total_orders = total_chocolate + total_strawberry + total_vanilla


print("Chocolate", total_chocolate)
print("Strawberry",total_strawberry)
print("Vanilla", total_vanilla)
print("Total", total_orders)

open_file.close()