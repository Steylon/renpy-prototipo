# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:
    play sound "prepare_your_swords.mp3"
    scene bg esterior_condominio with fade
    "Manoel, porteiro do Condomínio Jaqueira, 
    acaba de chegar no turno da manhã. "
    "Observando a 
    saída dos moradores para irem ao trabalho, ele
    vê um homem chegando à portaria."
    "..."
    scene bg cabine with dissolve
    show jaime normal at right with dissolve
    Jaime "Bom dia! Meu nome é Jaime, sou encanador, vim consertar a pia da moradora do bloco B, apartamento 206."
    show manoel normal at left with dissolve:
        yalign 0.3
        xalign 0.3
    Manoel "Interfonei para o apartamento, mas ninguém o atendeu."
    "Observando que o homem estava vestido como encanador"
    "O porteiro imaginou que ele estava a trabalho.)"
    hide jaime with dissolve
    hide manoel with dissolve


    #menu escolha

label deixar_ou_nao:
    menu:
        "Aprovar a entrada de Jaime baseado em suas  vestimentas de encanador?":
            Manoel "Pela sua roupa vejo que está a trabalho. Sendo assim, me de sua identificação e pode subir"
            jump bad_end
        "Não permitir a entrada de Jaime?": 
            with dissolve
            Manoel "Infelizmente não vou deixar você subir, tente voltar mais tarde, somente com a presença dos moradores vamos poder te ajudar!"
            with dissolve
            "Você fez a escolha correta!"
            jump deixar_ou_nao
    return


# final ruim.

label bad_end:
    
    "Duas horas depois..." with dissolve 
    "O síndico desce desesperado! A moradora do bloco B, apartamento 206, foi rendida e roubada por um assaltante." with dissolve 
    show fernando normal with dissolve
    Andre "Manoel, recebi uma denuncia séria! Uma moradora disse que foi rendida no próprio apartamento e teve vários itens de valor roubados." with dissolve
    Andre " Acabei de ver aqui no livro de presenças que você deixou um homem subir algumas horas antes." with dissolve
    Andre "Vamos ver as imagens da câmera de segurança para você identificar se era o mesmo homem." with dissolve 
    with dissolve
    hide fernando
    menu:
        "Aceitar o pedido de André para verificar as cameras.":
            "Resposta correta, mesmo que leve a uma conclusão de que você teve culpa por agir de 
            forma negligente deve se cooperar para descobrir quem é o verdadeiro culpado."
            jump cameras
        "Não aceitar o pedido.":
            " ..."

    return

label cameras:
    scene bg cameras with fade
    "Manoel observou que o assaltante era o suposto encanador que deixou subir sem autorização,"
    "Ele sabia que isso era algo muito grave e que haveria consequências." with dissolve

    # final
    scene bg delegacia
    show manoel normal at right with dissolve
    show fernando normal at left with dissolve:
        yalign 1.7
   
    "Depois de ir à delegacia junto ao síndico e a moradora, Manoel foi demitido " with dissolve
    return
