import unicodedata

# Define the input and output file paths


# Open the input and output files
with open(r'C:\Users\HP\OneDrive\Desktop\uniqsansk.txt', mode="r", encoding="utf-8") as f_in, \
     open(r'C:\Users\HP\OneDrive\Desktop\sansletspi.txt', mode="w", encoding="utf-8") as f_out:

    # Loop through each line in the input file
    for line in f_in:
        # Loop through each character in the line
        prev_char = ""
        for char in line:
            # Check if the character is a Sanskrit letter
            if '\u0900' <= char <= '\u097F':
                # Combine dependent vowel signs with the previous consonant
                if '\u093E' <= char <= '\u094C' or char == '\u0902' or char == '\u0903':
                    if prev_char and unicodedata.category(chr(ord(prev_char))) == '\u0900'or '\u0901'or '\u0902' or '\u0903' or '\u093A' or '\u093B' or '\u093C' or '\u093D' or '\u093E' or '\u093F' or '\u0940' or '\u0941' or '\u0942'or '\u0943' or '\u0944' or '\u0945' or '\u0946' or '\u0947' or '\u0948' or '\u0949' or '\u094A' or '\u094B' or '\u094C' or '\u094D' or '\u094E' or '\u094F' or '\u0950' or '\u0951' or '\u0952' or '\u0953' or '\u0954' or '\u0955'or '\u0956' or '\u0957' or '\u0970' or '\u0971':
                        combined_char = prev_char + char
                        f_out.write(combined_char + '\n')
                    else:
                        f_out.write(prev_char + '\n')
                        f_out.write(char + '\n')
                else:
                    # Write the character to the output file
                    f_out.write(char + '\n')
                prev_char = char
            else:
                # Write the character to the output file
                f_out.write(char)
                prev_char = ""
