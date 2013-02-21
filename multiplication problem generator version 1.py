print("#=======================================#")
print("#            ZenOokami Codes            #")
print("#          http://zenstudios.tk         #")
print("#=======================================#")
print("#          ~    /| ZEN |\   ~           #")
print("#              / |_____| \              #")
print("#             |           |             #")
print("#             |  __   __  |             #")
print("#             <  \/   \/  >             #")
print("#              <         >              #")
print("#                \  v  /                #")
print("#                 \___/                 #")
print("#           `~-::Ookami*::-~`           #")
print("#=======================================#")
print("# _____ _            _    _       _  __ #")
print("#|_   _| |          | |  | |     | |/ _|#")
print("#  | | | |__   ___  | |  | | ___ | | |_ #")
print("#  | | | '_ \ / _ \ | |/\| |/ _ \| |  _|#")
print("#  | | | | | |  __/ \  /\  / (_) | | |  #")
print("#  \_/ |_| |_|\___|  \/  \/ \___/|_|_|  #")
print("#=======================================#")

repeat_input = True
number_of_inputs = 0

#Import
from random import randint

print("Welcome to the Random Multiplication Problem Generator")
while repeat_input == True:
    #Ask how many problems does user want to solve
    number_of_problems = input("How many problems would you like to solve [1 through 10]: ")
    if int(number_of_problems) < 1 or int(number_of_problems) > 10:
        print("Number is not a correct value...")
    elif int(number_of_problems) >= 1 or int(number_of_problems) <= 10:
        print("You chose " + str(number_of_problems))
        repeat_input = False
        print("")


for problems_number in range(int(number_of_problems)):
    #Random numbers for (A * B) = C
    random_variable_a = randint(1, 12)
    random_variable_b = randint(1, 12)
    variable_c = random_variable_a * random_variable_b
    correct_answer = False
    while correct_answer == False:
        answer = input("Answer: " + str(random_variable_a) + "*" + str(random_variable_b) + "= ")
        number_of_inputs += 1
        if int(answer) > variable_c:
            print("Your answer is to high! Try again!")
            correct_answer = False
        elif int(answer) < variable_c:
            print("Your answer is to low! Try again!")
            correct_answer = False
        elif int(answer) == variable_c:
            print("You got the right answer!")
            correct_answer = True
print("")
print("The number of inputs you have is: " + str(number_of_inputs))
print("The number of problems you requested for was: " + str(number_of_problems))
average_of_tries = int(number_of_inputs) / int(number_of_problems)
print("Your average is: " + str(average_of_tries))
print("")
print('Coded by: Zane "ZenOokami"')
      
