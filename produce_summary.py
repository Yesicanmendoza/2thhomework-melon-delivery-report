def deliveries_per_day(the_file):
    #Function that get the information of the deliveries per day


    for line in the_file:
        line = line.rstrip()
        #Eliminate all the empty spaces at the right
        word = line.split('|')
        #Split every line by the "|" symbol

        product = word[0]
        count = word[1]
        amount = word[2]

        print(f"Delivered {count} {product}s for total of ${amount}")
    
    the_file.close()

print("Day 1")
the_file = open("um-deliveries-day-1.txt")
deliveries_per_day(the_file)

print("Day 2")
the_file = open("um-deliveries-day-2.txt")
deliveries_per_day(the_file)

print("Day 3")
the_file = open("um-deliveries-day-3.txt")
deliveries_per_day(the_file)
