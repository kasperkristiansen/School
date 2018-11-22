orchard = [[4, 2, 3, 4, 7, 2, 11, 8, 3, 5],
           [5, 9, 6, 6, 6, 11, 6, 4, 9, 8],
           [6, 3, 7, 10, 6, 7, 9, 10, 3, 5],
           [4, 4, 7, 9, 8, 6, 6, 12, 6, 2],
           [11, 13, 12, 6, 8, 6, 4, 3, 8, 7],
           [5, 6, 6, 8, 5, 5, 9, 9, 8, 11],
           [9, 15, 6, 3, 8, 6, 5, 4, 7, 6],
           [8, 5, 7, 5, 7, 8, 7, 9, 9, 9]]


def sum_apples(row):
    print(sum(row))


def orchard_data():
    print("Apples in row 1: " + str(sum(orchard[0])))
    print("Apples in row 2: " + str(sum(orchard[1])))
    print("Apples in row 3: " + str(sum(orchard[2])))
    print("Apples in row 4: " + str(sum(orchard[3])))
    print("Apples in row 5: " + str(sum(orchard[4])))
    print("Apples in row 6: " + str(sum(orchard[5])))
    print("Apples in row 7: " + str(sum(orchard[6])))
    print("Apples in row 8: " + str(sum(orchard[7])))
    print("Total apples: " + str(sum(orchard[0] + orchard[1] + orchard[2] + orchard[3] + orchard[4] + orchard[5] + orchard[6] + orchard[7])))


orchard_data()


def single_tree():
    pick_row = int(input("Choose a row: "))
    pick_tree = int(input("Choose a tree: "))
    print("Tree number", pick_tree, "in row", pick_row, "produces", orchard[pick_row-1][pick_tree-1], "apples.")


single_tree()


def change_tree():
    pick_row = int(input("Choose a row: "))
    pick_tree = int(input("Choose a tree: "))
    new_value = int(input("What is the new value: "))
    orchard[pick_row-1][pick_tree-1] = new_value
    print("The value of tree number", pick_tree, "in row number", pick_row, "has been updated to", new_value, "apples.")


change_tree()
print(orchard[2][2])


# def update_percent():
#    for tree in row:
#        tree *= 1.2
#        row += 1
#