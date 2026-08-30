#Given an "out" string length 4, such as "<<>>", and a word, 
# return a new string where the word is in the middle of the out string, 
# e.g. "<<word>>".
#______________________________________#
# make_out_word('<<>>', 'Yay') → '<<Yay>>'
# make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
# make_out_word('[[]]', 'word') → '[[word]]'

def make_out_word(out:str, word:str):
    return out[:2] + word + out[2:]

out = "<<>>"
word = "Hello"
out_i = input()
word_i = input()

print(make_out_word(out, word))
print(make_out_word(out_i, word_i))