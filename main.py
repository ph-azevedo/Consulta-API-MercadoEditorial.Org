import requests
import json
import locale
arquivo = input('Digite o nome do arquivo da planilha: ')
locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
print('######################################################')
print('###Consulta de livros na API do MercadoEditoral.Org###')
print('######################################################')
print()
isbn = input('Digite o ISBN: ')
if len(isbn) != 13:
    print('ERRO - ISBN deve ter 13 dígitos.')
    exit()
request = requests.get(f'https://api.mercadoeditorial.org/api/v1.2/book?isbn={isbn}')
request_json = request.json()
if (request_json['status'])['code'] != 200:
    print('Livro não está no MercadoEditorial.Org')
    exit()
lista_dados = request_json['books']
dict_catalograficos = lista_dados[0]
class MEGet:
    def get_titulo():
        titulo = dict_catalograficos['titulo']
        return titulo

    def get_ano():
        ano = dict_catalograficos['ano_edicao']
        return ano

    def get_editora():
        editora = (dict_catalograficos['selo'])['nome_do_selo_editorial']
        return editora
    def get_preco():
        preco = dict_catalograficos['preco']
        valor_formatado = locale.currency(float(preco))
        return valor_formatado

    def get_edicao():
        edicao = dict_catalograficos['edicao']
        return edicao

    def get_subtitulo():
        subtitulo = dict_catalograficos['subtitulo']
        return subtitulo


print()
print()
print(f'ISBN: {isbn}')
print(f'Título: {MEGet.get_titulo()} - {MEGet.get_subtitulo()}')
print(f'Editora: {MEGet.get_editora()}')
print(f'Ano de Lançamento: {MEGet.get_ano()}')
print(f'Edição: {MEGet.get_edicao()} Ed.')
print(f'Preço: R{MEGet.get_preco()}')
