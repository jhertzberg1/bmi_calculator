'''
TODO
Greeting
Create commandline prompt for height
Create commandline prompt for weight
Run calculation
Look up BMI chart
Print results
'''

def welcome():
    print('Hi welcome to the BMI calculator.')


def request_height():
    height = 0
    return height


def request_weight():
    '''Commandline user input for weight

    Returns:
        int: Value representing user inputed weight as an int.

    '''
    while True:
        try:
            weight = int(input('What is your weight in pounds? >'))
            break
        except ValueError:
            print('That is not a number')
    return weight


def calculate_bmi(height_in_inches, weight_in_pounds):
    bmi = 23
    # TODO consider your units
    return bmi


def look_up_word(bmi): # TODO fix word
    if bmi >= 30:
        return 'Obese'
    if bmi >= 25:
        return 'Overweight'
    if bmi >= 19:
        return 'Normal weight'
    return 'Under weight'


def print_results(bmi, word):
    '''Prints the results of your BMI.

    Args:
        bmi (int): calculated body mass index score
        word (str): 

    '''
    print(word)# look up string formatting




if __name__ == '__main__':
    welcome()
    height = request_height()
    weight = request_weight()
    print(weight)
    bmi = calculate_bmi(height, weight)
    word = look_up_word(bmi)
    print_results(bmi, word)
