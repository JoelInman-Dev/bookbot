def main():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()

            count_text(file_contents)

def count_text(text):
    words = text.split()
    print(len(words))

main()
