### Get list of numbers from each row in text file. Sum the first and last number in the list and the sum total of all rows in the document

TEXT_NUMBERS = [
    (0,"zero"),
    (1,"one"),
    (2,"two"),
    (3,"three"),
    (4,"four"),
    (5,"five"),
    (6,"six"),
    (7,"seven"),
    (8,"eight"),
    (9,"nine"),
]

def getCalDoc(file_name:str=None) -> list:
    if file_name is None: raise AttributeError("No calibration document provided")
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines

def printLines(lines:list=None):
    if lines is None: raise AttributeError("input lines not received")
    for line in lines:
        print(line)

def getNumsInString(string:str) -> list:
    numbers = []

    # Add text string numbers to list with position
    for num in TEXT_NUMBERS:
        pos = 0
        str_ctr = 0
        while pos >= 0:
            if str_ctr == 0: 
                pos = string.find(num[1])
            else:
                pos = string.find(num[1], pos+len(num[1]))
            if pos >= 0:
                numbers.append({
                    "position": pos,
                    "number": num[0]
                })
            str_ctr += 1
                

    # Add integers to list with position
    for idx, _ in enumerate(string):
        
        try:
            num = int(_)
            is_num = True
        except:
            is_num = False
        
        if is_num: 
            numbers.append({
            "position": idx,
            "number": num
                })
        

    # Order numbers list by position
    numbers = sorted(numbers, key=lambda x:x['position'])
    numbers = [ _["number"] for _ in numbers ]
    return numbers

if __name__ == "__main__":

    ### Get filename of calibration document
    cal_doc_path = input("Please enter the filepath of the calibration document: ")

    ### Load document
    lines = getCalDoc(cal_doc_path)

    ### Print number of lines
    print(f"Length of input: {len(lines)}")

    ### Loop through lines and get numbers
    total = 0
    for idx, line in enumerate(lines):

        numbers = getNumsInString(line)

        first = numbers[0]
        last = numbers[-1]
        
        num_str = f"{first}{last}"
        num_int = int(num_str)

        total += num_int

        print(f"Line #{idx} has {len(numbers)} numbers: {numbers} num: {num_int} line: {line}")
        print(f"Running total: {total}")

    print(f"Final total: {total}")
    