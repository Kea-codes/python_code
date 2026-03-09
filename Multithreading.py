# Multithreading => Used to perform multiple tasks concurrently (multitasking)
#                => Good for I/O bounds tasks like reading files or fetching data from APIs
#                => threading.Thread(target=my_function)


import threading #for multithreading
import time

def walk_dog(first_name, last_name):
    time.sleep(8) #it takes 8 seconds to walk the do
    print(f"you finished walking {first_name} {last_name}")
    

def take_out_trash():
    time.sleep(2)
    print("You took out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")


def main():
    # THE FUNCTIONS ARE RUNNING ON THE SAME THREAD
    # WE CAN  ACCOMPLISH ALL THREE TASKS AT THE SAME 
    # walk_dog()
    # take_out_trash()
    # get_mail()

    # IF THE FUNTION HAS ARGUMENTS
    # WE INCLUDE args IN THE THREAD AS AN ARGUEMENT
    # THE WE PUT A COMA TO LET PYTHON KNOW THAT args IS A TUPLE
    chore1 = threading.Thread(target= walk_dog, args=("Scooby","Doo" ))
    chore1.start()

    chore2 = threading.Thread(target= take_out_trash)
    chore2.start()

    chore3 = threading.Thread(target= get_mail)
    chore3.start()

    # PRINTING OUT THE CONFIRMATION MESSAGE
    # BUT WE USE THE join() METHOD FIRST SO THAT CHORES CAN BE COMPLETE
    # THEN THE CONFIRMATION METHOD POPS UP
    chore1.join()
    chore2.join()
    chore3.join()
    print("ALL CHORES ARE COMPLETE!")


if __name__ == "__main__":
    main()