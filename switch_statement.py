# MATCH CASE  (SWITCH CASE STATEMENT) => AN ALTERNATIVE TO USING ELIF STATEMENTS


def WeekDay(day):
    match day :
        case 1:
            return"IT IS MODAY" 
        case 2:
            return "IT IS TUESDAY" 
        case 3:
            return "IT IS WEDNESDAY" 
        case 4:
            return "IT IS THURSDAY" 
        case 5:
            return "IT IS FRIDAY" 
        case 6:
            return "IT IS SATURDAY"
        case 7:
            return "IT IS SUNDAY"
        case _:
            return "INVALID" 
    return day

print(WeekDay(1))



