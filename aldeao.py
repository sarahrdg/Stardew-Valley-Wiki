class aldeao:
    def __init__(self, nome, aniversario, ama, odeia):
        self.nome = nome
        self.aniversario = aniversario
        self.ama = ama
        self.odeia = odeia


    def falar(self):
        return f"Olá nova(o) fazendeira(o), meu nome é {self.nome}. Meu aniversário é em {self.aniversario}. Eu amo {', '.join(self.ama)} e odeio {', '.join(self.odeia)}."
    
    def receber_presente(self, presente: str):
        if presente.lower() == self.ama.lower():
            print(f"[{self.nome}]: Uau! {presente} é exatamente o que eu amo! Muito obrigado!")
            return 2  # Retorna pontuação positiva (ex: +2 corações)
        elif presente.lower() == self.odeia.lower():
            print(f"[{self.nome}]: Ah... {presente}? Eu realmente não gosto disso. Desculpe.")
            return -1 # Retorna pontuação negativa (ex: -1 coração)
        else:
            print(f"[{self.nome}]: Obrigado pelo {presente}. É um presente ok.")
            return 1 # Retorna pontuação neutra (ex: +1 coração)
        

class CandidatoCasamento(aldeao):
    # Atributos: coracoes: int, max_coracoes: int
    def __init__(self, nome: str, aniversario: int, ama: str, odeia: str, max_coracoes: int = 10):
        # Chamada ao construtor da classe Pai (aldeao)
        super().__init__(nome, aniversario, ama, odeia)
        self.coracoes = 0 # Sempre começa em zero
        self.max_coracoes = max_coracoes
    
    # Sobrescreve o método receber_presente para atualizar os corações
    def receber_presente(self, presente: str):
        pontuacao = super().receber_presente(presente) # Pega a pontuação do aldeao pai
        
        self.coracoes += pontuacao
        
        # Garante que os corações não ultrapassem o máximo ou fiquem negativos
        if self.coracoes > self.max_coracoes:
            self.coracoes = self.max_coracoes
        if self.coracoes < 0:
            self.coracoes = 0

        self.mostrar_status()
        return pontuacao

    # Método para mostrar o status de relacionamento
    def mostrar_status(self):
        coracoes_cheios = '❤️' * self.coracoes
        coracoes_vazios = '🤍' * (self.max_coracoes - self.coracoes)
        print(f"Status de Amizade com {self.nome}: {coracoes_cheios}{coracoes_vazios} ({self.coracoes}/{self.max_coracoes})")
