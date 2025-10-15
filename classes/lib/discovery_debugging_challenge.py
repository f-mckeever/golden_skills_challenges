def get_most_common_letter(text):
    counter = {}
    for char in text:
        #Counter should only include letters
        letters = "qwertyuiopasdfghjklzxcvbnm"

        if char in letters:
            counter[f'{char}'] = counter.get(char, 0) + 1
        

    #Sort counter by most common letter -> use [::-1] to get it in descending order
    letter = sorted(counter.items(), key=lambda item: item[1])[::-1][0][0]
    
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
