
def melon_report(day, file_path):
    the_file = open(file_path)
    print(f"Day {day}")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    
    the_file.close()









melon_report(1,"um-deliveries-20140519.txt")
melon_report(2,"um-deliveries-20140520.txt")
melon_report(3,"um-deliveries-20140521.txt")
