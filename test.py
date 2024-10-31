# from twilio.rest import Client

# # Your Account SID and Auth Token from twilio.com/console
# account_sid = 'your_account_sid'
# auth_token = 'your_auth_token'
# client = Client(account_sid, auth_token)

# # List of phone numbers to send the message to
# phone_numbers = ['+2347081165523', '+19876543210', '+11234567890']

# # Message content
# message_body = 'This is a test message sent to multiple devices.'

# for number in phone_numbers:
#     message = client.messages.create(
#         body=message_body,
#         from_='+2349029150535',  # Your Twilio phone number
#         to=number
#     )
#     print(f"Message sent to {number}: {message.sid}"
# message SMS someone














import random
number = random.randint(1, 100)
print("Welcome to the number guessing game!")
print(" Let's atart guessing, Shall we!")

while True:
    guess = (input("Enter your guess: "))

    if guess.isdigit():
        guess = float(guess)

        if guess < 1 or guess > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
        elif guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number correctly.")
            break
    else:
        print("Invalid input. Please enter a valid number within the range of 1 to 100.")

