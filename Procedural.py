#line by line

#step 1 - collect grades
def get_grades():
    grades = [85,90,78,92,99, 100] #hardcoded for simplicity
    return grades

#step 2 - process the grades (calc total and avg)
def calculate_average(grades):
    return sum(grades) / len(grades)


# step 2 - process the grades (calc total and avg)
def calculate_average(grades):
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    return average
    #return sum(grades) / len(grades)

def display_average(average):
    print('The class average is', average)

def main():
    grades = get_grades()
    average = calculate_average(grades)
    display_average(average)
