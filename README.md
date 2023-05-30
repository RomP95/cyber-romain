
```bash
git clone https://github.com/RomP95/cyber-romain/
cd cyber-romain
chmod +x installation.sh
./installation.sh 
python3 main.py
```

Dans ce script nous avons le choix de faire plusieurs scans :
-	Scan offensif qui sera basé sur du nmap avec rapport de scan en envoi mail
-	Scan WEB lui sera basé sur Nikto avec rapport de scan en envoi mail
-	Récupérations des CVE
Pour ce script j’ai d’insister sur le côté « envoi de mail » et reporting en PDF car cela est très utile dans un SOC



Résultat du scan offensif sur « implicaction.eu »
Sur ce scan nous retrouvons :
-	La cible « implicaction.eu »
-	Le nmap en 7.93 avec la date et l’heure du lancement du scan
-	L’adresse Ip d’implicaction.eu 217.160.0.250
-	Les ports scannés et ouvert :
-	80/tcp(http) , 81/tcp(http), 443/tcp(https)
Envoi du rapport du scan web sur l’adresse e-mail en PDF

Pour l'envoi de mail j'ai utiliser la library "smtplib"
La bibliothèque "smtplib" en Python est utilisée pour envoyer des courriers électroniques via le protocole SMTP (Simple Mail Transfer Protocol). SMTP est le protocole standard utilisé pour l'envoi de courriers électroniques sur Internet.

La bibliothèque "smtplib" fournit une interface pour établir une connexion avec un serveur SMTP, envoyer des courriers électroniques et gérer les erreurs éventuelles lors de l'envoi.


Commentaires sur l'activation de la 2FA et la génération d'un mot de passe sécurisé : Les commentaires en début de fonction indiquent qu'il est nécessaire d'activer la 2FA (Two-Factor Authentication, ou authentification à deux facteurs) et de générer un mot de passe d'application sécurisé dans les paramètres de sécurité du compte Google. Les liens donnés renvoient à une question sur Stack Overflow qui traite du problème de l'incapacité d'envoyer des e-mails en utilisant des applications moins sécurisées. La solution proposée consiste à activer la 2FA et à générer un mot de passe d'application sécurisé.


Définition des variables "fromaddr" et "fromaddr_psswd" : Les deux lignes suivantes définissent les variables "fromaddr" et "fromaddr_psswd". "fromaddr" représente l'adresse e-mail de l'expéditeur et "fromaddr_psswd" représente le mot de passe associé à cette adresse e-mail. Dans cet exemple, l'adresse e-mail utilisée est "nelsonairu1200@gmail.com" et le mot de passe associé est "xrkmdkecskkvquie". Ces informations sont utilisées pour l'authentification lors de l'envoi de l'e-mail.


Scan offensif :
Résultat du scan offensif sur « implicaction.eu »
Sur ce scan nous retrouvons :
-	La cible « implicaction.eu »
-	Le nmap en 7.93 avec la date et l’heure du lancement du scan
-	L’adresse Ip d’implicaction.eu 217.160.0.250
-	Les ports scannés et ouvert :
-	80/tcp(http) , 81/tcp(http), 443/tcp(https)
Envoi du rapport du scan web sur l’adresse e-mail en PDF


Scan WEB :
Résultat du scan WEB sur le site « implicaction.eu »
Sur ce scan nous retrouvons :
-	Nikto en version v2.1.6
-	L’hostname « implicaction.eu »
-	L’adresse IP d’implicaction.eu » 217.160.0.250
-	Le port pour le site « 443 »
-	Le server utiliser pour le site « Apache »
-	L'en-tête X-XSS-Protection n'est pas défini. L'en-tête X-XSS-Protection est utilisé pour activer la protection contre les attaques de type cross-site scripting (XSS). Son absence peut indiquer un risque accru d'attaques XSS.
-	Le site utilise SSL (Secure Sockets Layer) et l'en-tête Strict-Transport-Security HTTP n'est pas défini, SSL (Secure Sockets Layer) est utilisé pour sécuriser la communication entre le serveur et le navigateur. L'en-tête Strict-Transport-Security permet de forcer une connexion sécurisée (HTTPS). Son absence peut indiquer un risque potentiel de downgrade de sécurité
-	Le site utilise SSL et l'en-tête Expect-CT n'est pas présent. Elle permet de vérifier si un certificat de transparence (CT) est requis pour le site. Son absence peut indiquer un risque potentiel lié à la vérification de la validité des certificats.
-	En-tête peu courant 'x-redirect-by' trouvé, avec le contenu : WordPress
-	Le site utilise SSL et l'en-tête Expect-CT n'est pas présent
-	L'en-tête Content-Encoding est défini sur "deflate", ce qui peut signifier que le serveur est vulnérable à l'attaque BREACH
-	Aucun répertoire CGI trouvé (utilisez l'option '-C all' pour vérifier tous les répertoires possibles) : Le scanner n'a trouvé aucun répertoire CGI, qui sont des répertoires où des scripts CGI peuvent être exécutés. Cette information peut être utile pour identifier d'éventuelles vulnérabilités liées à ces répertoires.
-	L'entrée '/wp-admin/' dans robots.txt a renvoyé un code HTTP non interdit ou de redirection (200) : Le fichier robots.txt est utilisé pour contrôler l'accès des robots d'exploration aux pages du site. L'entrée '/wp-admin




Pour les CVE j’ai utilisé la valeur « url = fhttps://cve.circl.lu/api/last/{num_cve}
Dans cette ligne, une variable "url" est définie en utilisant une f-string (une syntaxe de formatage de chaîne introduite dans Python 3.6+). La valeur de "url" est construite en concaténant la chaîne de base "https://cve.circl.lu/api/last/" avec la valeur de l'argument "num_cve". Cette URL est utilisée pour accéder à l'API du site CVE de CIRCL afin de récupérer les dernières informations sur les CVE (Common Vulnerabilities and Exposures).




