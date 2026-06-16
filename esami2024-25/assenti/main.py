# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~


def leggi_prenotati(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return {parts[0]: parts[1:] for line in file if (parts := line.split())}

def leggi_consegne(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.split("_")[2].replace("S", "") for line in file.readlines()]
    
def check_assenti(prenotati, consegne):
    return {prenotazione : prenotati[prenotazione] for prenotazione in prenotati if not prenotazione in consegne}

def print_assenti(assenti, appello):
    print(f"Assenti al {appello}o appello: ")
    for matricola, nome in assenti.items():
        cognome = nome[0]
        altri_nomi = " ".join(nome[1:])
        
        print(f"{matricola:<8} {cognome:<15} {altri_nomi}")

def print_sempre_assenti(assenti):
    print("Matricole degli studenti che non si sono mai presentati a un appello: ")
    for matricola in assenti:
        
        print(f"{matricola:<8}")

def run():
    sempre_assenti = list()
    for i in range(3):
        appello = i+1
        assenti = check_assenti(leggi_prenotati(f"prenotati_appello{appello}.txt"), leggi_consegne(f"consegne_appello{appello}.txt"))
        sempre_assenti = assenti if appello == 1 else [matricola for matricola in assenti if matricola in sempre_assenti]
        print_assenti(assenti, appello)
    print_sempre_assenti(sorted(sempre_assenti))

        

run()