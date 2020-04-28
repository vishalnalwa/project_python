inp = input('Please enter temperature\n')
try:
    fahr = float(inp)
    cel = (fahr-32.0) * 5.0/9.0
    print(cel)
except:
    print("Dont mess with me ,please enter a valid temperature")
