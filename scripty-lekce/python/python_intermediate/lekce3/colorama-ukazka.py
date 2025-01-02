# import colorma module
from colorama import init, Fore, Back, Style

# Initialize Colorama
init()

# Print text with different colors and styles
print(Fore.RED + 'This text is red')
print(Back.GREEN + 'This text has a green background')
print(Style.BRIGHT + 'This text is bright')
print(Style.RESET_ALL + 'Back to normal text')