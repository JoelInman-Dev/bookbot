def main():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()

            word_count = count_text(file_contents)
            report_data = count_chars(file_contents)
            report(report_data, word_count)

def count_text(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    letters = {}
    words = text.split()
    keys = []
    for word in words:
        for char in word:
            if len(keys) >= 1:
                if char in keys:
                    count = letters.get(char)
                    letters[char] = (count + 1)
            else:
                letters[char] = 1
        keys = letters.keys()
    return letters

def report(data, word_count):
    dataset = []
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    for char in data:
        dataset.append({"name": char, "num": data[char]})
    sorted_data = sorted(dataset, key=lambda x: x["num"], reverse=True)
    for d in sorted_data:
        print(f"The '{d['name']}' character was found {d['num']} times")
    print("--- End report ---")
        
def sort_on(dict):
    return dict["num"]

main()
