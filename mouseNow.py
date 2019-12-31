# Author: Tri Do
# Date: 12/30/19
# Description: Determine where the mouse pointer is located.

#! python3
# mouseNow.py - Displays the mouse cursor's current position.

import pyautogui
print('Press Ctrl-C to quit.')

try:
    while True:
        #TODO: Get the print the mouse coordinates.

        x, y = pyautogui.position()     # Uses multiple assignment trick where the x and y are given values of the
        # two integers returned from the tuple from pyautogui.position()

        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)        # right justify regardless of the
        # amount of space required up to 4 digits.

        print(positionStr, end='')         # end='' prevents a newline character from being added to the end of the
        # printed line.

        print('\b' * len(positionStr), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone')