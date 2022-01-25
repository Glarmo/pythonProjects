# basic terminal movement
import time, sys
indent = 0
indentIncrease = True
try:
    while True:
        print (' ' * indent, end='')
        print("********")
        time.sleep(0.05)
        if indentIncrease:
            indent = indent + 1
            if indent > 50:
                indentIncrease = False
        else:
            indent = indent - 1
            if indent < 1:
                indentIncrease = True
except KeyboardInterrupt:
    sys.exit()
