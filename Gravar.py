arquivo = open('arqText.txt', 'w')

arquivo.write('Curso Pyton \n')
arquivo.write('Aula Prática')
arquivo.close()

#leitura do arquivo de texto

leitura=open('arqText.txt', 'r')
print(leitura.read())
leitura.close()
