import sys

emojiDictionary = {
    "A": [':regional_indicator_a:', ':a:', ':arrow_up_small:'],
    "B": [':regional_indicator_b:', ':b:'],
    "C": [':regional_indicator_c:', ':star_and_crescent:'],
    "D": [':regional_indicator_d:', ':leftwards_arrow_with_hook:'],
    "E": [':regional_indicator_e:', ':email:'],
    "F": [':regional_indicator_f:', ':flags:'],
    "G": [':regional_indicator_g:'],
    "H": [':regional_indicator_h:'],
    "I": [':regional_indicator_i:', ':information:', ':clock1230:'],
    "J": [':regional_indicator_j:', ':japan:'],
    "K": [':regional_indicator_k:'],
    "L": [':regional_indicator_l:', ':clock3:'],
    "M": [':regional_indicator_m:', ':m:', ':part_alternation_mark:', ':scorpio:'],
    "N": [':regional_indicator_n:', ':capricorn:'],
    "O": [':regional_indicator_o:', ':o2:', ':o:', ':no_entry_sign:'],
    "P": [':regional_indicator_p:', ':parking:'],
    "Q": [':regional_indicator_q:'],
    "R": [':regional_indicator_r:'],
    "S": [':regional_indicator_s:'],
    "T": [':regional_indicator_t:', ':cross:', ':orthodox_cross:'],
    "U": [':regional_indicator_u:'],
    "V": [':regional_indicator_v:'],
    "W": [':regional_indicator_w:'],
    "X": [':regional_indicator_x:', ':x:', ':negative_squared_cross_mark:'],
    "Y": [':regional_indicator_y:'],
    "Z": [':regional_indicator_z:', ':zzz:'],
    "0": [':zero:'],
    "1": [':one:', ':first_place:'],
    "2": [':two:', ':second_place:'],
    "3": [':three:', ':third_place:'],
    "4": [':four:'],
    "5": [':five:'],
    "6": [':six:'],
    "7": [':seven:'],
    "8": [':eight:', ':8ball:'],
    "9": [':nine:'],
}

emojiUnicodeMap = {
    ':regional_indicator_a:': r'\U0001F1E6',
    ':a:': r'\U0001F170',
    ':arrow_up_small:': r'\U0001F53C',
    ':regional_indicator_b:': r'\U0001F1E7',
    ':b:': r'\U0001F171',
    ':regional_indicator_c:': r'\U0001F1E8',
    ':star_and_crescent:': r'\U0000262A',
    ':regional_indicator_d:': r'\U0001F1E9',
    ':leftwards_arrow_with_hook:': r'\U000021A9',
    ':regional_indicator_e:': r'\U0001F1EA',
    ':email:': r'\U00002709',
    ':regional_indicator_f:': r'\U0001F1EB',
    ':flags:': r'\U0001F38F',
    ':regional_indicator_g:': r'\U0001F1EC',
    ':regional_indicator_h:': r'\U0001F1ED',
    ':regional_indicator_i:': r'\U0001F1EE',
    ':information:': r'\U00002139',
    ':clock1230:': r'\U0001F567',
    ':regional_indicator_j:': r'\U0001F1EF',
    ':japan:': r'\U0001F5FE',
    ':regional_indicator_k:': r'\U0001F1F0',
    ':regional_indicator_l:': r'\U0001F1F1',
    ':clock3:': r'\U0001F552',
    ':regional_indicator_m:': r'\U0001F1F2',
    ':m:': r'\U000024C2',
    ':part_alternation_mark:': r'\U0000303D',
    ':scorpio:': r'\U0000264F',
    ':regional_indicator_n:': r'\U0001F1F3',
    ':capricorn:': r'\U00002651',
    ':regional_indicator_o:': r'\U0001F1F4',
    ':o2:': r'\U0001F17E',
    ':o:': r'\U00002B55',
    ':no_entry_sign:': r'\U0001F6AB',
    ':regional_indicator_p:': r'\U0001F1F5',
    ':parking:': r'\U0001F17F',
    ':regional_indicator_q:': r'\U0001F1F6',
    ':regional_indicator_r:': r'\U0001F1F7',
    ':regional_indicator_s:': r'\U0001F1F8',
    ':regional_indicator_t:': r'\U0001F1F9',
    ':cross:': r'\U0000271D',
    ':orthodox_cross:': r'\U00002626',
    ':regional_indicator_u:': r'\U0001F1FA',
    ':regional_indicator_v:': r'\U0001F1FB',
    ':regional_indicator_w:': r'\U0001F1FC',
    ':regional_indicator_x:': r'\U0001F1FD',
    ':x:': r'\U0000274C',
    ':negative_squared_cross_mark:': r'\U0000274E',
    ':regional_indicator_y:': r'\U0001F1FE',
    ':regional_indicator_z:': r'\U0001F1FF',
    ':zzz:': r'\U0001F4A4',
    ':zero:': r'\U0000030',
    ':one:': r'\U0000031',
    ':first_place:': r'\U0001F947',
    ':two:': r'\U0000032',
    ':second_place:': r'\U0001F948',
    ':three:': r'\U0000033',
    ':third_place:': r'\U0001F949',
    ':four:': r'\U0000034',
    ':five:': r'\U0000035',
    ':six:': r'\U0000036',
    ':seven:': r'\U0000037',
    ':eight:': r'\U0000038',
    ':8ball:': r'\U0001F3B1',
    ':nine:': r'\U0000039',
}

def emojiConverter(input):
    # initialize empty list
    word = []

    # occurences dictionary
    occurrences = {}

    #string to be returned
    emoji_string = ""

    # check if input string is empty
    if not input:
        print("Input String is empty.")
        return

    # loop through each character of the input string
    for ch in input:
        # capitalize the characters
        upper_ch = ch.upper()

        if upper_ch in occurrences:
            occurrences[upper_ch] += 1
        else:
            occurrences[upper_ch] = 0

        # ask if the character exists in the dictionary and if the number of occurrences
        # inside the input word is less then the number of available options for said character
        if upper_ch in emojiDictionary and occurrences[upper_ch] < len(emojiDictionary[upper_ch]):
            # append the emoji that was not yet used in case we have more than 1 character of the same type in the word
            emoji_string += emojiDictionary[upper_ch][occurrences[upper_ch]]
            word.append(emojiDictionary[upper_ch][occurrences[upper_ch]])
        else:
            return "Not enough emoji's to represent the word"
    return emoji_string