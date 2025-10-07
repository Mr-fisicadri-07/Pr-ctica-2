# creamos variable, asignamos clase str y pedimos input al usuario
sentence_input = str(input("Please enter a sentence: "))
# creamos variable, usamos metodo split para separar palabras y crear lista
sentence_list = sentence_input.split(" ")
# usamos funcion reversed para invertir orden de lista
inverted_list = reversed(sentence_list)
# usamos metodo join para unir lista en string y asignamos variable
inverted_sentence = " ".join(inverted_list)
# imprimimos resultado
print(inverted_sentence)
