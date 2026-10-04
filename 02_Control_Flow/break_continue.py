# break and continue

print("Using break:")

for i in range(1, 11):
    if i == 6:
        break

    print(i)


print("\nUsing continue:")

for i in range(1, 11):
    if i == 6:
        continue

    print(i)