def introducao():
    """Exibe a introdução do jogo e a premissa."""
    print("Bem-vindo ao Sombras da Velha República, um RPG de texto baseado na era da Velha República do universo Star Wars!")
    print("\nNeste jogo, você assume o papel de um herói em Dantooine, uma colônia da República ameaçada pelo Lorde Sith Darth Valthor.")
    print("Sua missão é deter Valthor e salvar a colônia, enfrentando escolhas que levam a finais diferentes: bom, ruim ou ambíguo.")
    print("\nPrepare-se para sua aventura em uma galáxia muito, muito distante...")
    print("-" * 60) # Linha divisória para separar seções

def escolher_classe():
    """Permite ao jogador escolher uma classe e retorna a classe selecionada."""
    classes_validas = {
        "1": "Cavaleiro Jedi (Maestria com Sabre)",
        "2": "Cônsul Jedi (Controle da Força)",
        "3": "Contrabandista (Tiro Preciso)",
        "4": "Trooper da República (Táticas Militares)"
    }

    while True:
        print("\nEscolha sua classe:")
        for key, value in classes_validas.items():
            print(f"{key} - {value}")

        escolha = input("Digite o número da sua classe: ").strip()

        if escolha in classes_validas:
            print(f"\nVocê escolheu: {classes_validas[escolha]}!")
            return classes_validas[escolha]
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 4.")

def capitulo_um(classe):
    """Primeiro capítulo da aventura, com escolhas iniciais baseadas na classe."""
    print("\n" + "=" * 60)
    print("CAPÍTULO 1: O Chamado em Dantooine")
    print("=" * 60)
    print(f"\nComo um(a) {classe}, você sente a sombra de Darth Valthor se estender sobre Dantooine.")
    print("Boatos de seus acampamentos se espalham pela colônia, e a necessidade de agir é iminente.")

    if "Jedi" in classe:
        print("\nSua conexão com a Força é forte. Você sente uma perturbação profunda.")
        print("Você pode tentar buscar holocrons antigos para aumentar seu conhecimento ou confrontar um acampamento Sith próximo.")
        print("1 - Buscar Holocrons Jedi")
        print("2 - Invadir Acampamento Sith")
        escolha = input("O que você faz? ").strip()
        return escolha
    elif "Contrabandista" in classe:
        print("\nSeus contatos no submundo indicam que Valthor está interessado em um artefato.")
        print("Você pode tentar negociar informações com um espião local ou recrutar alguns mercenários aliados.")
        print("1 - Negociar com Espião")
        print("2 - Recrutar Aliados")
        escolha = input("O que você faz? ").strip()
        return escolha
    elif "Trooper" in classe:
        print("\nSeu treinamento militar te diz que é hora de ação. O reconhecimento é crucial.")
        print("Você pode explorar cavernas de cristais para entender as fontes de poder de Valthor ou organizar uma equipe para um ataque coordenado.")
        print("1 - Explorar Cavernas de Cristais")
        print("2 - Organizar Ataque Coordenado")
        escolha = input("O que você faz? ").strip()
        return escolha
    return "0" # Retorna "0" caso a classe não se encaixe nas condições (não deveria acontecer)

def resultado_capitulo_um(classe, escolha):
    """Determina o resultado do Capítulo 1 e retorna um status para o próximo capítulo."""
    if "Jedi" in classe:
        if escolha == "1":
            print("\nVocê se aventura em ruínas antigas e encontra um holocron que revela segredos sobre Valthor. Seu conhecimento da Força aumenta!")
            return "conhecimento"
        elif escolha == "2":
            print("\nVocê lidera um ataque ousado a um acampamento Sith. A batalha é difícil, mas você obtém informações cruciais sobre os planos de Valthor.")
            return "informacao_sith"
    elif "Contrabandista" in classe:
        if escolha == "1":
            print("\nVocê se encontra com um espião astuto e, após uma negociação tensa, adquire dados valiosos sobre os movimentos de Valthor.")
            return "dados_valiosos"
        elif escolha == "2":
            print("\nVocê convence um grupo de mercenários a se juntar à sua causa. Sua força cresce, mas a lealdade deles é incerta.")
            return "aliados_duvidosos"
    elif "Trooper" in classe:
        if escolha == "1":
            print("\nVocê explora as profundezas das cavernas de cristais, descobrindo uma fonte de energia sombria utilizada por Valthor. Uma estratégia é formulada.")
            return "estrategia_formulada"
        elif escolha == "2":
            print("\nVocê organiza um ataque surpresa a um posto avançado Sith. A operação é um sucesso, enfraquecendo as linhas inimigas.")
            return "inimigo_enfraquecido"
    
    print("\nSuas escolhas levaram a um beco sem saída. Valthor avança sem oposição.")
    return "derrota" # Caso a escolha seja inválida ou leve a um resultado neutro/ruim

def capitulo_dois(status_anterior):
    """Segundo capítulo da aventura, influenciado pelas ações anteriores."""
    print("\n" + "=" * 60)
    print("CAPÍTULO 2: Confronto e Consequências")
    print("=" * 60)

    if status_anterior == "conhecimento":
        print("\nCom o conhecimento do holocron, você entende a fraqueza de Valthor e elabora um plano para atraí-lo.")
        print("Você decide enfrentá-lo em um local de poder da Força ou desmantelar seu ritual principal.")
        print("1 - Confrontar Valthor em local de poder")
        print("2 - Desmantelar ritual Sith")
        escolha = input("Qual sua estratégia final? ").strip()
        return escolha
    elif status_anterior == "informacao_sith":
        print("\nAs informações do acampamento Sith revelam a localização de Valthor. Você se prepara para o ataque final.")
        print("Você pode lançar um ataque direto e decisivo ou tentar uma tática de guerrilha para desorientá-lo.")
        print("1 - Lançar Ataque Direto")
        print("2 - Usar Tática de Guerrilha")
        escolha = input("Como você o enfrenta? ").strip()
        return escolha
    elif status_anterior == "dados_valiosos":
        print("\nOs dados obtidos do espião mostram que Valthor está vulnerável em um determinado momento.")
        print("Você pode usar essa informação para um golpe rápido e preciso ou tentar chantageá-lo para que se retire.")
        print("1 - Executar Golpe Rápido")
        print("2 - Tentar Chantagear Valthor")
        escolha = input("Qual a sua abordagem? ").strip()
        return escolha
    elif status_anterior == "aliados_duvidosos":
        print("\nSeus aliados mercenários estão inquietos. Valthor se aproxima, e eles exigem mais pagamento ou fugirão.")
        print("Você pode pagar um alto preço para mantê-los ou tentar motivá-los com uma promessa de glória.")
        print("1 - Pagar os Mercenários")
        print("2 - Motivar com Glória")
        escolha = input("Como você mantém sua força? ").strip()
        return escolha
    elif status_anterior == "estrategia_formulada":
        print("\nCompreendendo as fontes de energia de Valthor, você tem uma estratégia para desativá-las antes do confronto.")
        print("Você pode tentar sabotar as fontes de cristal antes do ataque ou usar seu conhecimento para enfraquecer Valthor durante a batalha.")
        print("1 - Sabotar Fontes de Cristal")
        print("2 - Enfraquecer Valthor na Batalha")
        escolha = input("Qual a sua tática final? ").strip()
        return escolha
    elif status_anterior == "inimigo_enfraquecido":
        print("\nO inimigo está enfraquecido pelos seus ataques anteriores. É a hora de desferir o golpe final.")
        print("Você pode liderar uma carga total para a vitória ou armar uma armadilha para capturar Valthor.")
        print("1 - Liderar Carga Total")
        print("2 - Armar Armadilha para Valthor")
        escolha = input("Qual sua decisão? ").strip()
        return escolha
    
    # Caso um status_anterior inesperado chegue aqui (erro ou derrota no Cap. 1)
    return "0"

def final(classe, status_anterior, escolha_final):
    """Determina e exibe um dos três finais possíveis: Bom, Ruim ou Ambíguo."""
    print("\n" + "=" * 60)
    print("O DESTINO DE DANTOINE")
    print("=" * 60)

    # Lógica para o Final Bom
    if ("Jedi" in classe and status_anterior == "conhecimento" and escolha_final == "1") or \
       ("Contrabandista" in classe and status_anterior == "dados_valiosos" and escolha_final == "1") or \
       ("Trooper" in classe and status_anterior == "estrategia_formulada" and escolha_final == "1"):
        print("\nCom astúcia e poder, você derrota Darth Valthor e liberta Dantooine de sua escuridão!")
        print("Os cidadãos o saúdam como um verdadeiro herói. A paz retorna à colônia.")
        print("\nFINAL BOM: A Força está com você. A galáxia respira aliviada.")
        return "bom"
    
    # Lógica para o Final Ruim
    elif ("Jedi" in classe and status_anterior == "informacao_sith" and escolha_final == "2") or \
         ("Contrabandista" in classe and status_anterior == "aliados_duvidosos" and escolha_final == "1") or \
         ("Trooper" in classe and status_anterior == "inimigo_enfraquecido" and escolha_final == "2"):
        print("\nSuas táticas falham, ou seus aliados o traem. Darth Valthor contra-ataca com ferocidade.")
        print("Dantooine sucumbe à escuridão, e sua missão termina em derrota. A galáxia lamenta.")
        print("\nFINAL RUIM: A escuridão venceu. A esperança se apaga.")
        return "ruim"

    # Lógica para o Final Ambíguo
    else:
        print("\nVocê consegue deter Darth Valthor, mas o custo é alto, ou o futuro de Dantooine permanece incerto.")
        print("Vitórias parciais ou sacrifícios deixam uma marca na colônia. A luta continua em outras frentes.")
        print("\nFINAL AMBÍGUO: A vitória veio, mas a paz ainda está distante.")
        return "ambiguo"

def jogar_novamente():
    """Pergunta ao jogador se deseja jogar novamente."""
    while True:
        resposta = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")

# --- Loop Principal do Jogo ---
if __name__ == "__main__":
    while True:
        introducao()
        
        classe_escolhida = escolher_classe()
        
        status_cap_1 = capitulo_um(classe_escolhida)
        # Se o status do capítulo 1 for "derrota", o jogo termina ou oferece tentar novamente
        if status_cap_1 == "derrota":
            print("\nVocê falhou em sua primeira tarefa e a colônia foi comprometida. A aventura termina aqui.")
            if not jogar_novamente():
                break
            else:
                continue # Reinicia o loop principal do jogo
        
        status_cap_2 = resultado_capitulo_um(classe_escolhida, status_cap_1)
        
        # Se o resultado do capítulo 1 foi uma derrota, não prossegue para o capítulo 2
        if status_cap_2 == "derrota":
            print("\nSeus esforços foram em vão no primeiro confronto. Darth Valthor consolidou seu poder.")
            if not jogar_novamente():
                break
            else:
                continue # Reinicia o loop principal do jogo

        escolha_final = capitulo_dois(status_cap_2)
        
        # Se a escolha final foi "0", indica um caminho inesperado ou derrota no cap 2
        if escolha_final == "0":
            print("\nSuas últimas ações não foram suficientes para deter Valthor. Dantooine caiu.")
            if not jogar_novamente():
                break
            else:
                continue

        final_jogo = final(classe_escolhida, status_cap_2, escolha_final)
        
        if not jogar_novamente():
            break

    print("\nObrigado por jogar Sombras da Velha República!")
