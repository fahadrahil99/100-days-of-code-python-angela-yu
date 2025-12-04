from base64 import encode

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt():
    original_text = text
    shift_amount = shift


# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.
    index_of_letters_1 = []
    for a in original_text:
        index_of_letters = ""
        index_of_letters += str(alphabet.index(a))
        index_of_letters = int(index_of_letters)
        index_of_letters += shift_amount
        index_of_letters = index_of_letters % len(alphabet)
        index_of_letters_1.append(str(index_of_letters))
        # if index_of_letters > 25 :
        #     case2= index_of_letters - 26
        #     index_of_letters_1.append(str(case2))
        # else :
        #     index_of_letters = str(index_of_letters)
        #     index_of_letters_1.append(index_of_letters)




    final_encrypted = ""
    for a in index_of_letters_1:
        final_encrypted += alphabet[int(a)]
    print(final_encrypted)















# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt()

