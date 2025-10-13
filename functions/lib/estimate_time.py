#Returns the time in minutes to read text at 200 words a minute
 
def estimate_time(string):
    #user's words per minute reading speed
    words_per_minute = 200

    #RETURN 0 for empty strings, else divide number of words in string by words per minute
    if len(string) > 0:
        words = string.split(" ")
        return len(words) / words_per_minute
    return 0

#returns formatted response as a string
def format_time(number_of_minutes):
    return f"This will take about {number_of_minutes} minutes to read."