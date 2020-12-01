def play(input_file, input_parameters, log_level):
    

    #Initialize and read input


    print("Day 1 begins!")


    #Part 1 of Day 1


    expenses = []

    for i in input_file:
        expenses.append(int(i))
        
        if log_level >= 1:
            print(f"Added expense: {i}")

    product = 0
    vals = []
    a = 0
    b = 0
    for e in range(len(expenses)):
        for r in range(len(expenses)):
            if e == r: continue

            a = expenses[e]
            b = expenses[r]
            if a + b == 2020:
                vals.append(a)
                vals.append(b)
                product = a * b
                break
            elif log_level >= 2:
                print(f"Expense[{e}]({a}) + Expense[{r}]({b}) sum {a+b} does not equal 2020")

        if (product > 0): break

    if (len(vals) > 0):
        print(f"Values {vals[0]} and {vals[1]} product is {product}")
    else:
        print("Unable to find values")


    #Part 2 of Day 1