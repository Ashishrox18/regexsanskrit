import codecs
import unicodedata

# Function to check if a character is a Devanagari letter or not
def is_devanagari(char):
    return 'DEVANAGARI' in unicodedata.name(char)

# Open the input file containing Sanskrit words in Devanagari script
with codecs.open(r'C:\Users\HP\OneDrive\Desktop\uniqsansk.txt', 'r', 'utf-8') as f:
    lines = f.readlines()

# Remove whitespace and newlines from each line and split into individual words
words = [line.strip().split() for line in lines]

# Flatten the list of words
words = [word for sublist in words for word in sublist]

# Open the output file to write the letters
with codecs.open(r'C:\Users\HP\OneDrive\Desktop\sanspli.txt', 'w', 'utf-8') as f:
    # Loop over each word in the list of words
    for word in words:
        # Loop over each character in the word
        for char in word:
            # If the character is a Devanagari letter, write it to the output file
            if is_devanagari(char):
                f.write(char + '\n ')
            # If the character is an ottakshara, write it to the output file
            elif char in ['\u0900', '\u0901', '\u0902', '\u0903', '\u0904','\u0905', '\u0906', '\u0907', '\u0908', '\u0909','\u090A', '\u090B', '\u090C', '\u090D', '\u090E','\u090F',
                          '\u0910', '\u0911', '\u0912', '\u0913', '\u0914','\u0915', '\u0916', '\u0917', '\u0918', '\u0919','\u091A', '\u091B', '\u091C', '\u091D', '\u091E','\u091F',
                          '\u0920', '\u0921', '\u0922', '\u0923', '\u0924','\u0925', '\u0926', '\u0927', '\u0928', '\u0929','\u092A', '\u092B', '\u092C', '\u092D', '\u092E','\u092F',
                          '\u0930', '\u0931', '\u0932', '\u0933', '\u0934','\u0935', '\u0936', '\u0937', '\u0938', '\u0939','\u093A', '\u093B', '\u093C', '\u093D', '\u093E','\u093F',
                          '\u0940', '\u0941', '\u0942', '\u0943', '\u0944','\u0945', '\u0946', '\u0947', '\u0948', '\u0949','\u094A', '\u094B', '\u094C', '\u094D', '\u094E','\u094F',
                          '\u0950', '\u0951', '\u0952', '\u0953', '\u0954','\u0955', '\u0956', '\u0957', '\u0958', '\u0959','\u095A', '\u095B', '\u095C', '\u095D', '\u095E','\u095F',
                          '\u0960', '\u0961', '\u0962', '\u0963', '\u0964','\u0965', '\u0966', '\u0967', '\u0968', '\u0969','\u096A', '\u096B', '\u096C', '\u096D', '\u096E','\u096F',
                          '\u0970', '\u0971', '\u0972', '\u0973', '\u0974','\u0975', '\u0976', '\u0977', '\u0978', '\u0979','\u097A', '\u097B', '\u097C', '\u097D', '\u097E','\u097F']:
                f.write(char + ' \n')
        # Write a newline character after each word is processed
        f.write('\n')
