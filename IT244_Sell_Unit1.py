#Take the sentences and turn them into pseudocode variables

Sent1=" Python was created in the 1890's by Guido van Rossum. "
Sent2=" Python is maintained as an 'open source' project by a group that is called the Python Software Foundation. "
Sent3=" He is affectionately known as Python's \"Benevolent Dictator for Life.\" "
Sent1 = Sent1.lstrip()
Sent2 = Sent2.lstrip()
Sent3 = Sent3.lstrip()
Sent1 = Sent1.replace("1890", "1990")

SentAll = Sent1 + Sent2 + Sent3

print(SentAll)