# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: August 29, 2023

# Description: This program prompts the user for a text file containing
# a list of words and a name for an output file. It then outputs a count
# of occurrences of each unique word to the output file.

# Logic:
# main:
#   get input file
#   create output file
#   for loop to read lines into list
#   sort list
#   initialize an accumulator and a pointer
#   while loop:
#       if element == next element: counter ++, pointer ++
#       if element != next element: write word and count to file, pointer ++
#       if end of list: write word and count to file, break
#   print completion message
#
# get input file: 
#   prompt user for file name
#   try: open file
#   except: display error, try again

# create output file:
#   prompt user for file name
#   try to open file for reading to see if it is found
#   if found, inform user and ask if it shoud be replaced
#       if y: open file for writing and end function
#       else: start over at prompt
#   if not found, open file for writing and end function

# create main function to begin program execution
def main():
    # initialize list to read file words into
    word_list = []
    
    # call functions to open input and output files
    word_file = get_word_file()
    count_file = create_count_file()

    # for loop to read input file words and append to word list
    # ignore blank lines, strip newline characters, make all lowercase
    for line in word_file:
        if not line.isspace():
            word_list.append(line.lower().rstrip())

    # close input file
    word_file.close()

    # sort word list to group matching words for comparison
    word_list.sort()

    # initialize pointer for index reference
    # and accumulator to keep count of word occurrences
    pointer = 0
    counter = 1

    # initialize control variable and begin while loop for processing the data
    not_done = True
    while not_done:
        # try clause to cause loop to iterate until reaching end of list
        try:
            # check if pointer word matches the next word
            # if they match, increment counter
            if word_list[pointer] == word_list[pointer + 1]:
                counter += 1
            # if they do not match, write result to file and reset counter
            else:
                count_file.write(f'{word_list[pointer]}: {str(counter)}\n')
                counter = 1
            # increment pointer for index for next iteration
            pointer += 1
        # if invalid index, end of list has been reached
        # write final result to file and update control variable to end loop
        except IndexError:
            count_file.write(f'{word_list[pointer]}: {str(counter)}\n')
            not_done = False

    # close output file and display confirmation message
    count_file.close()
    print(f'Your file has been created.')

# function to prompt user for input file name, test whether file exists
# and open file for reading
def get_word_file():
    # get input file name from user and assign to variable for testing
    test = input(f'Please enter the name of the file to read: ')

    # initialize control variable and begin while loop
    not_done = True
    while not_done:
        # try opening file for reading
        # if successful, update control variable to end loop / function
        try:
            file_name = open(test, 'r')
            not_done = False
        # if unsuccessful, prompt user for a new name and iterate again
        except:
            test = input(f'File not found. Please try another name: ')
    return file_name

# function to prompt user for output file name and open file for writing
# checks whether filename already exists, and confirms with user whether
# they would like to replace the existing file if applicable
def create_count_file():
    # get output file name from user and assign to variable for testing
    test = input(f'Please enter a name for your count file: ')

    # initialize control variable and begin while loop
    not_done = True
    while not_done:
        # try opening file for reading, to see if it already exists
        try:
            file_name = open(test, 'r')
            # if successful, close file and ask user if it should be replaced
            file_name.close()
            replace = input(f'This file already exists. Replace? (y/n): ')
            # if user entered 'y' or 'Y', open file for writing and end loop
            if replace.lower() == 'y':
                file_name = open(test, 'w')
                not_done = False
            # if user did not enter 'y' or 'Y', prompt for another filename
            else:
                test = input(f'Please try another name: ')
        # if no existing file found, open for writing and end loop
        except:
            file_name = open(test, 'w')
            not_done = False
    return file_name
            
# call main() to execute program    
if __name__ == '__main__':
    main()
    
