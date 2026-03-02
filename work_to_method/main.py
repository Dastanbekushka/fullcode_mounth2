
import voice
import colors
import test

def lottery(arr):
    result = []
    c = test.numbers(3)
    for i in c:
        if 7 == i:
            result.append(i)
    arr = result

    return arr
finish = lottery([])

def winner(arr):
    if len(arr) == 1:
        voice.speak("Вы выиграли 100 долларов")
        return colors.color(arr)
    elif len(arr) == 2:
        voice.speak("Вы выиграли 200 долларов")
        return colors.color(arr)
    elif len(arr) == 3:
        voice.speak("Вы выиграли 300 долларов")
        return colors.color(arr)
    else:
        return voice.speak("Вы проиграли!")
print(winner(finish))

f"wjefkjebg"



