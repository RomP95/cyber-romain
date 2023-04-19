import subprocess
import os
import socket
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from fpdf import FPDF 

def target_choix():
    global target
    target = input("Indiquer le nom de domaine que vous avez choisi comme cible : ")

#Fonction qui va résoudre le domaine cible (target) afin d'obtenir son IP
def domaine_resolver(target):
    try:
        global ip
        ip = socket.gethostbyname(target)
        with open('output.txt', 'w') as f:
            f.write(f"Le nom de domaine {target} correspond à l'adresse IP {ip}\n")
        return ip
    except socket.gaierror:
        print("Erreur: impossible de résoudre le nom de domaine.")
        return None

#Fonction NMAP qui va lancer sur la machine un nmap -sV
def nmap():
    commande = ["nmap", "-sV", target]
    with open('output.txt', 'w') as f:
        resultat_nmap = subprocess.run(commande, text=True, check=True, stdout=f)
    
    with open('output.txt', 'r') as f:
        print(f.read())

def nikto():
    commande = ["nikto", "--host", target]
    with open('output.txt', 'w') as f:
        resultat_nikto = subprocess.run(commande, text=True, check=True, stdout=f)
    
    with open('output.txt', 'r') as f:
        print(f.read())

#Fonction va convertir notre output.txt en pdf pour le rapport final
def pdf():
    pdf = FPDF()      
    pdf.add_page()  
    pdf.set_font("Arial", size = 11)
    f = open("output.txt", "r") 

    for x in f: 
        pdf.cell(95,5, txt = x, ln = 1, align = '') 
    pdf.output("result.pdf")

#Fonction qui va envoyer un mail avec le rapport en PJ
def envoie_mail():

    #Activer 2FA
    #Généner mot de passe apps sécurisés dans sécurité du compte google
    #https://stackoverflow.com/questions/72547853/unable-to-send-email-in-c-sharp-less-secure-app-access-not-longer-available/72553362#72553362
    fromaddr = "nelsonairu1200@gmail.com"
    fromaddr_psswd = "xrkmdkecskkvquie"

    toaddr = input("Renseigner l'adresse à laquelle vous souhaiter envoyer le rapport (PDF) : ")

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "RAPPORT SCAN - ROMAIN PERRI"

    body = "Bonjour, vous trouverez le rapport en pièce jointe"

    msg.attach(MIMEText(body, 'plain'))

    filename = "result.pdf"
    attachment = open("result.pdf", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, fromaddr_psswd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

def cve():
    import requests
    from tabulate import tabulate

    def get_latest_cve(num_cve):
        url = f"https://cve.circl.lu/api/last/{num_cve}"
        response = requests.get(url)

        if response.status_code == 200:
            cves = response.json()
            cve_list = []

            for cve in cves:
                cve_list.append([cve["id"], cve["Published"]])

            print(tabulate(cve_list, headers=["ID", "Date"], tablefmt="grid"))
        else:
            print(f"Erreur lors de la requête : {response.status_code}")
    get_latest_cve("10")



print("Que voulez faire ?")
print("1. Scan offensif")
print("2. Scan Web")
print("3. Récupération des failles critiques 'up-to-date'")

reponse = input("Entrez votre réponse (1, 2, ou 3) : ")

# Vérifier que la réponse est valide
if reponse not in ['1', '2', '3']:
    print("Réponse invalide. Veuillez répondre en choisissant 1, 2, ou 3.")
else:
    # Convertir la réponse en un entier
    reponse = int(reponse)

    if reponse == 1:
        os.system("clear")
        target_choix()
        domaine_resolver(target)
        nmap()
        pdf()
        envoie_mail()
    elif reponse == 2:
        os.system("clear")
        target_choix()
        domaine_resolver(target)
        nikto()
        pdf()
        envoie_mail()

    elif reponse == 3:
        os.system("clear")
        cve()
