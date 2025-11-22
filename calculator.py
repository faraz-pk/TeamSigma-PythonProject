def calculator():
    print("-----Welcome to the Calculator!-----")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1,2,3,4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")

            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")

            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")

            elif choice == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error! Division by zero.")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() == 'no':
                print("Shutting down the calculator. Goodbye!")
                break
        else:
            print("Invalid Input")
            
calculator()
def asad_guessing_game():
    import random

    while True:
        secret_number = random.randint(1, 50)
        attempt_count = 0

        print("I'm thinking of a number between 1 and 50...")

        while True:
            user_input = input("Enter your guess (1-50): ")

            try:
                user_guess = int(user_input)
            except ValueError:
                print("Invalid input! Enter a NUMBER.")
                continue

            if user_guess < 1 or user_guess > 50:
                print("Out of range! Enter a number between 1 and 50.")
                continue

            attempt_count += 1

            if user_guess < secret_number:
                print("Too low!")
            elif user_guess > secret_number:
                print("Too high!")
            else:
                print(f"Correct! You guessed it in {attempt_count} attempts.")
                break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break
