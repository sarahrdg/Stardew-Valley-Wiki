from aldeao import *

class SimulacaoVila:
    def __init__(self):
        self.npcs = {} 

    def criar_vila(self):
        print("--- Povoando a Vila... ---")
        
        # 1. Aldeão não casável
        haley = aldeao("Haley", 14, "Girassol", "Pão")
        self.npcs[haley.nome] = haley

        # 2. Candidatos a Casamento
        abigail = CandidatoCasamento("Abigail", 13, "Ametista", "Argila")
        self.npcs[abigail.nome] = abigail

        sebastian = CandidatoCasamento("Sebastian", 10, "Lágrima Congelada", "Alho")
        self.npcs[sebastian.nome] = sebastian
        
        print("Vila pronta. Total de NPCs:", len(self.npcs))

    def main(self):
        self.criar_vila()

        while True:
            print("\n=== Interagindo na Vila ===")
            print("NPCs disponíveis:", ", ".join(self.npcs.keys()))
            print("1. Falar com NPC")
            print("2. Dar Presente")
            print("3. Mostrar Status de Casamento")
            print("4. Sair")
            
            escolha = input("Escolha a ação: ")
            
            if escolha == "1":
                nome = input("Com quem você quer falar? ")
                npc = self.npcs.get(nome)
                if npc:
                    npc.falar()
                else:
                    print("NPC não encontrado.")

            elif escolha == "2":
                nome = input("Para quem você quer dar o presente? ")
                npc = self.npcs.get(nome)
                if npc:
                    presente = input(f"Qual presente você dará para {nome}? (Ex: Ametista, Pão, Girassol) ")
                    npc.receber_presente(presente)
                else:
                    print("NPC não encontrado.")
            
            elif escolha == "3":
                nome = input("De qual Candidato você quer ver o status? ")
                npc = self.npcs.get(nome)
                # Verifica se existe E se é um CandidatoCasamento
                if isinstance(npc, CandidatoCasamento):
                    npc.mostrar_status()
                else:
                    print(f"{nome} não é um candidato(a) a casamento.")

            elif escolha == "4":
                print("Saindo da Vila...")
                break
            
            else:
                print("Opção inválida.")

if __name__ == "__main__":
    simulacao = SimulacaoVila()
    simulacao.main()
