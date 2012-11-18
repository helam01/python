# -*- coding: utf-8 -*-

import sys
from Tkinter import *


class Criptografy:
	def __init__(self):
		self.alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
		self.special = [ [["Á", "À", "Ã", "Â"], "A"], [["É", "È", "Ê"], "E"], [["Í", "Ì"], "I"], [["Ó", "Ò", "Ô", "Õ"], "O"], [["Ú", "Ù", "Ü"], "U"] ]
		self.key = 0
		print len(self.alphabet)

	def cript(self,action, text, key):
		self.key = key
		text = text.upper()
		newText = ''

		for wordText in text:
			count = 0
			for wordAlpha in self.alphabet:
				if wordText == wordAlpha:				

					if action == 'cript':
						soma = count+self.key
						if soma > 25:
							countSoma = soma - 26
							newText += self.alphabet[0+countSoma]
						else:
							newText += self.alphabet[soma]
					if action == 'decript':
						soma = count-self.key
						if soma < 0:
							soma = 26
						newText += self.alphabet[soma]

					print wordText, count, newText	
				count += 1	

				

			if wordText == ' ':
				newText += ' '
				print wordText, count, newText

		print newText
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
		self.textInputLabel = Label(self.textInputFrame, text='Texto Origonal: ')
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

		print originalText
		print key


	def decript(self):
		key = int(self.keyField.get())

		criptoObj = Criptografy()		

		criptText = self.textResponseField.get('1.0', 'end')

		decriptedText = criptoObj.cript('decript', criptText, key)

		self.textInputField.delete('1.0', 'end')
		self.textInputField.insert(END, decriptedText)

		print originalText
		print key



app = PyCriptoApp('800x600')
