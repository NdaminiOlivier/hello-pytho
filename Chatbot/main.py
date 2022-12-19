#ceci est mon premier chatbot
from nltk.chat.util import Chat,reflections
pairs= [
        ["Mon nom est (.*)",["Salut %1"]]

]
chat = Chat(pairs,reflections)
chat.converse()
