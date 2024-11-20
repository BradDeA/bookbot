def main():
    with open('books/frankenstein.txt') as f:
        contents = f.read()
        
    def count_words(text):
        count = 0
        for i in text.split():
            count += 1
        return count
    
    def characters(text):
        chars = {}
        for i in text.lower():
            if i.isalpha():
                if i not in chars:
                    chars[i] = 1
                else:
                    chars[i] += 1
        return chars
    
    def report(count, chars):
        print('--- Begin report of books/frankenstein.txt ---')
        print(f'{count} words found in the document\n')
        for entry in chars:
            print(f'The {entry[0]} character was found {chars[entry]} times')
        print('--- End report ---')

    total_words = count_words(contents)
    char_dict = characters(contents)
    report(total_words, char_dict)

main()