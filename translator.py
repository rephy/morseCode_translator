class Translator:

    def __init__(self):

        self.translations = [
            ['a', '.-'],
            ['b', '-...'],
            ['c', '-.-.'],
            ['d', '-..'],
            ['e', '.'],
            ['f', '..-.'],
            ['g', '--.'],
            ['h', '....'],
            ['i', '..'],
            ['j', '.---'],
            ['k', '-.-'],
            ['l', '.-..'],
            ['m', '--'],
            ['n', '-.'],
            ['o', '---'],
            ['p', '.--.'],
            ['q', '--.-'],
            ['r', '.-.'],
            ['s', '...'],
            ['t', '-'],
            ['u', '..-'],
            ['v', '...-'],
            ['w', '.--'],
            ['x', '-..-'],
            ['y', '-.--'],
            ['z', '--..'],
            ['1', '.----'],
            ['2', '..---'],
            ['3', '...--'],
            ['4', '....-'],
            ['5', '.....'],
            ['6', '-....'],
            ['7', '--...'],
            ['8', '---..'],
            ['9', '----.'],
            ['0', '-----'],
            ['.', '.-.-.-'],
            [',', '--..--'],
            ['?', '..--..'],
            ['\'', '.---.'],
            ['!', '-.-.--'],
            ['/', '-..-.'],
            ['(', '-.--.'],
            [')', '-.--.-'],
            ['&', '.-...'],
            [':', '---...'],
            [';', '-.-.-.'],
            ['=', '-...-'],
            ['+', '.-.-.'],
            ['-', '-....-'],
            ['_', '..--.-'],
            ['"', '.-..-.'],
            ['$', '...-..-'],
            ['@', '.--.-.']
        ]

    def to_morse(self, original):

        new = ""

        for char in original:
            found_match = False
            for translation in self.translations:
                if translation[0] == char:
                    new += f"{translation[1]} "
                    found_match = True
            if not found_match:
                if char != " ":
                    new += char + " "
                else:
                    new += "/ "

        return new

    def from_morse(self, original):

        new = ""

        for char in original.split(" "):
            found_match = False
            for translation in self.translations:
                if translation[1] == char:
                    new += f"{translation[0]}"
                    found_match = True
            if not found_match:
                if char != "/":
                    new += char
                else:
                    if char == "/":
                        new += " "

        return new