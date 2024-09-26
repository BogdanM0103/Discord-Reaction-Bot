import sys

emojiDictionary = {
    "A": ['\U0001F1E6', '🅰️', '🔼'],
    "B": ['\U0001F1E7', '🅱️'],
    "C": ['\U0001F1E8', '☪️'],
    "D": ['\U0001F1E9', '↩️'],
    "E": ['\U0001F1EA', '✉️'],
    "F": ['\U0001F1EB', '🏁'],
    "G": ['\U0001F1EC'],
    "H": ['\U0001F1ED'],
    "I": ['\U0001F1EE', 'ℹ️', '🕧'],
    "J": ['\U0001F1EF', '🗾'],
    "K": ['\U0001F1F0'],
    "L": ['\U0001F1F1', '🕒'],
    "M": ['\U0001F1F2', 'Ⓜ️', '〽️', '♏'],
    "N": ['\U0001F1F3', '♑'],
    "O": ['\U0001F1F4', '🅾️', '⭕', '🚫'],
    "P": ['\U0001F1F5', '🅿️'],
    "Q": ['\U0001F1F6'],
    "R": ['\U0001F1F7'],
    "S": ['\U0001F1F8'],
    "T": ['\U0001F1F9', '✝️', '☦️'],
    "U": ['\U0001F1FA'],
    "V": ['\U0001F1FB'],
    "W": ['\U0001F1FC'],
    "X": ['\U0001F1FD', '❌', '✖️'],
    "Y": ['\U0001F1FE'],
    "Z": ['\U0001F1FF', '💤'],
    "0": ['0️⃣'],
    "1": ['1️⃣', '🥇'],
    "2": ['2️⃣', '🥈'],
    "3": ['3️⃣', '🥉'],
    "4": ['4️⃣'],
    "5": ['5️⃣'],
    "6": ['6️⃣'],
    "7": ['7️⃣'],
    "8": ['8️⃣', '🎱'],
    "9": ['9️⃣']
}


emojiList = [
    '🇦', '🅰️', '🔼',
    '🇧', '🅱️',
    '🇨', '☪️',
    '🇩', '↩️',
    '🇪', '✉️',
    '🇫', '🏁',
    '🇬',
    '🇭',
    '🇮', 'ℹ️', '🕧',
    '🇯', '🗾',
    '🇰',
    '🇱', '🕒',
    '🇲', 'Ⓜ️', '〽️', '♏',
    '🇳', '♑',
    '🇴', '🅾️', '⭕', '🚫',
    '🇵', '🅿️',
    '🇶',
    '🇷',
    '🇸',
    '🇹', '✝️', '☦️',
    '🇺',
    '🇻',
    '🇼',
    '🇽', '❌', '✖️',
    '🇾',
    '🇿', '💤',
    '0️⃣',
    '1️⃣', '🥇',
    '2️⃣', '🥈',
    '3️⃣', '🥉',
    '4️⃣',
    '5️⃣',
    '6️⃣',
    '7️⃣',
    '8️⃣', '🎱',
    '9️⃣'
]


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
            # emoji_string += emojiDictionary[upper_ch][occurrences[upper_ch]]
            word.append(emojiDictionary[upper_ch][occurrences[upper_ch]])
        else:
            return "Not enough emoji's to represent the word"
    return word