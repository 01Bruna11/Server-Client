class PessoasInputStream:
    def __init__(self, input_stream):
        self.input_stream = input_stream

    def ler_pessoas(self):
        dados = self.input_stream.read().decode('utf-8')
        return dados
