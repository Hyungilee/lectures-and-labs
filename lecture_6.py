print("Hello")

def validate(prompt, lower_bound: int, upper_bound: int) -> int:
    while True: 
        answer = int(input(prompt))
        if lower_bound < answer < upper_bound:
            return answer
        else:
            print(f"The year input must be greater than {lower_bound} and less than {upper_bound}")