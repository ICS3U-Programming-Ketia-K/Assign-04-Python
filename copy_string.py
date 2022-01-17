#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 10, 2022
# This program asks the user to enter an integer,n, and a string
# then it uses a loop to return a larger string that is n copies
# of the original string.

def copy_string():
  # initialize the loop counter and the string copy
  loop_counter = 0
  string_copy = ""

  # get user input as string
  user_string = input("\033[1;36;38mEnter a string: ")
  user_number_string = input("\033[1;36;38mEnter a number: ")
  print("")

  # checks to catch errors
  try:
      # covert user number string to an integer
      user_number_int = int(user_number_string)
      # checks to see if user number string is a whole number
      if (user_number_int > 0):
          # calculate the copies of the user string using the user number string
          for loop_counter in range(user_number_int):
              string_copy = string_copy + user_string 
          print("\033[1;33;38mOriginal string is : {} ".format(user_string))
          print("\033[1;33;38mNew string is : {} ".format(string_copy))
      else:
          print("\033[1;32;38m{} is not a valid input. Please "
                  "enter a positive number.".format(user_number_string))
  except Exception:
      print("\033[1;31;38m{} is not a number. Please try again."
                   .format(user_number_string))
  finally:
    print ("")
    print("\033[1;35;38mThanks for playing.")

def main():
    # This function calls other functions
    
    # call functions
    copy_string()
    
    
if __name__ == "__main__":
    main()
