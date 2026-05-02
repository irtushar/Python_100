print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12   
        print("Please pay $12.")
        
    photo = input("Do you want a photo taken? Y or N. ")
    if photo == "Y":
        bill += 3
        print("You have to pay an additional $3 for the photo.")
    elif photo == "N":
        print("No photo will be taken.")   
else:
    print("Sorry, you have to grow taller before you can ride.")        