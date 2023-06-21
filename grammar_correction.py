from gingerit.gingerit import GingerIt
text = input("ENTER A SENTENCE >>: ")
corrected_text = GingerIt().parse(text)
print(corrected_text['result'])