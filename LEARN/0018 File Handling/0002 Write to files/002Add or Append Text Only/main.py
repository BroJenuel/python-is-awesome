userINput = input("Enter Message you want to save: ")

with open('files/sample_text_file.txt', 'a') as file:
    file.write(userINput + '\n')
