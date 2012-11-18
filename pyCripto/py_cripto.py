# -*- coding: utf-8 -*-

import sys
from Tkinter import *


class Criptografy:
	def __init__(self):
		self.alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
		self.number = ['0','1','2','3','4','5','6','7','8','9']
		self.special = [ [["Á", "À", "Ã", "Â"], "A"], [["É", "È", "Ê"], "E"], [["Í", "Ì"], "I"], [["Ó", "Ò", "Ô", "Õ"], "O"], [["Ú", "Ù", "Ü"], "U"], [["Ç"], "C"] ]
		self.key = 0

	""" Verifica os letras com caracteres especiais e subustitui-las"""
	def SpecialCharReplace(self, word=''):		
		word = word.upper()
		word = word.encode(encoding='UTF-8', errors='strict')			
		for i, xlist in enumerate(self.special):
			for yindice, ylist in enumerate(xlist):
				for zlist in ylist:
					if zlist == word:							
						print(zlist)
						print(xlist[1])
						return xlist[1]
		return 	word			


	""" Função para criptografar e decriptografar o texto"""
	def cript(self,action, text, key):
		self.key = key
		text = text.upper()
		text = str(text)
		newText = ''

		""" Loop para percorrer o texto original"""
		for wordText in text:
			""" Chama função para subustituir os caracteres especiais"""
			wordText = self.SpecialCharReplace(wordText)		
			
			""" contator para pegar o key das letras"""
			count = 0
			
			""" Contador para pegar o key dos numeros"""
			countN = 0
			
			""" Loop para percorrer a lista do alfabeto"""
			for wordAlpha in self.alphabet:

				""" Compara a letra do texto com a do alfabeto"""
				if wordText == wordAlpha:
					""" Verifica a ação. Se for 'cript' então codifica a letra """
					if action == 'cript':

						""" soma o valor da chave com o indice da letra """
						soma = count+self.key
						""" Se a soma for maior q 25 subtrai o total de letras, para voltar ao key 0 """
						if soma > 25:
							countSoma = soma - 26
							newText += self.alphabet[0+countSoma]
						else:
							newText += self.alphabet[soma]

					""" Verifica a ação. Se for 'decript' então decodifica a letra """
					if action == 'decript':
						soma = count-self.key
						if soma < 0:
							soma = 26
						newText += self.alphabet[soma]
				count += 1


			""" Verifica os numeros """
			for number in self.number:
				if wordText == number:
					if action == 'cript':
						soma = countN+self.key
						if soma > 9:
							countSoma = soma - 9
							newText += self.number[0+countSoma]
						else:
							newText += self.number[soma]
					if action == 'decript':
						soma = countN-self.key
						if soma < 0:
							soma = 10
						newText += self.number[soma]
				countN += 1

			if wordText == ' ':
				newText += ' '

		return newText

	def decript(self):
		pass	







class PyCriptoApp:
	def __init__(self, size):
		self.root = Tk()
		self.root.title('PyCripto Beta')
		self.root.geometry(size)
		
		self.createForm()
		self.root.mainloop()


	def createForm(self):
		""" Frame que contera o formulario """
		self.formFrame = Frame(self.root)

		""" Definie o campo input para a Key """
		self.keyFrame 	= Frame(self.formFrame)
		self.keyVar		= StringVar(self.keyFrame)
		self.keyLabel	= Label(self.keyFrame, text='Chave: ')
		self.keyField	= Entry(self.keyFrame, textvar=self.keyVar)

		""" Define a caixa de texto de input """
		self.textFrame = Frame(self.formFrame)

		self.textInputFrame = Frame(self.textFrame)
		self.textInputField = Text(self.textInputFrame, height='20', width='40')
		self.textInputLabel = Label(self.textInputFrame, text='Texto origonal: ')
		self.criptButton	= Button(self.textInputFrame, text='Criptografar', font='Arial 12', command=self.cript)

		""" Define a caixa de texto Resposta"""
		self.textResponseFrame = Frame(self.textFrame)
		self.textResponseField = Text(self.textResponseFrame, height='20', width='40')
		self.textResponseLabel = Label(self.textResponseFrame, text='texto criptografado: ', justify='left')
		self.decriptButton	   = Button(self.textInputFrame, text='Decriptografar', font='Arial 12', command=self.decript)


		""" Exibe os elementos na tela """
		self.formFrame.pack(expand=True, fill='both')

		self.keyFrame.pack(side='top', fill='y', pady='10')
		self.keyLabel.pack(side='left')
		self.keyField.pack(side='left')

		self.textFrame.pack(side='top', pady= '0')

		self.textInputFrame.pack(side='left')
		self.textInputLabel.pack(side='top')
		self.textInputField.pack(side='left')
		self.criptButton.pack(side='top')

		self.textResponseFrame.pack(side='right')
		self.textResponseLabel.pack(side='top')
		self.textResponseField.pack(side='left')
		self.decriptButton.pack(side='bottom')



	def cript(self):
		key = int(self.keyField.get())

		criptoObj = Criptografy()

		originalText = self.textInputField.get('1.0', 'end')

		criptedText = criptoObj.cript('cript', originalText, key)

		self.textResponseField.delete('1.0', 'end')
		self.textResponseField.insert(END, criptedText)


	def decript(self):
		key = int(self.keyField.get())

		criptoObj = Criptografy()		

		criptText = self.textResponseField.get('1.0', 'end')

		decriptedText = criptoObj.cript('decript', criptText, key)

		self.textInputField.delete('1.0', 'end')
		self.textInputField.insert(END, decriptedText)





app = PyCriptoApp('800x500')
