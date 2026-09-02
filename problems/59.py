from common.paths import get_data_path

INPUT_FILE = get_data_path("0059_cipher.txt")
OUTPUT_FILE = get_data_path("0059_candidates.txt")

cipher = [
    int(value)
    for value in INPUT_FILE.read_text(encoding="utf-8").strip().split(",")
]

def compute(cipher):
    possiblecodes = []
    for x in range(97,123):
        for y in range(97, 123):
            for z in range(97,123):
                password = chr(x) + chr(y) + chr(z)
                count = 0
                decrypt = []
                for i in cipher:
                    temp = i^(ord(password[count % 3]))
                    if AcceptableChar(temp) == False:
                        break
                    else:
                        count += 1
                        decrypt.append(temp)
                if len(decrypt) == len(cipher):
                    finaltext = "".join(chr(x) for x in decrypt)
                    print(finaltext)
                    total = sum(decrypt)
                    possiblecodes.append((total, password))     
    return possiblecodes

def AcceptableChar(char):
    if char < 32:
        return False
    elif char > 122:
        return False
    elif 60 <= char <= 62:
        return False
    elif char == 64 or char == 42:
        return False
    elif 36 <= char <= 38:
        return False
    else:
        return True

print(compute(cipher))