import sys
from Tkinter import *


class Criptografy:
	def __init__(self):
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
		self.textInputLabel = Label(self.textInputFrame, text='Insira um texto: ')
		self.criptButton	= Button(self.textInputFrame, text='Criptografar', font='Arial 12', command=self.cripto)

		""" Define a caixa de texto Resposta"""
		self.textResponseFrame = Frame(self.textFrame)
		self.textResponseField = Text(self.textResponseFrame, height='20', width='40')
		self.textResponseLabel = Label(self.textResponseFrame, text='texto criptografado: ')
		self.decriptButton	   = Button(self.textInputFrame, text='Decriptografar', font='Arial 12', command='')


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


	def cripto(self):
		originalText = self.textInputField.get('1.0', 'end')
		criptedText = originalText
		self.textResponseField.delete('1.0', 'end')
		self.textResponseField.insert(END, criptedText)
		print originalText



app = PyCriptoApp('800x600')
