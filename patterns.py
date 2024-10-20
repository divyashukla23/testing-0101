import pyfiglet
def main():
    text = input("Enter some text: ")
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)
if __name__ == "__main__":
    main()
