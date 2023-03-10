userINput = input("Enter Message you want to save: ")

with open('files/sample_text_file.txt', 'w') as file:
    file.write(userINput)
