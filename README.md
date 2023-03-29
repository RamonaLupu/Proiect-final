# Proiect-Final-
BDD testing framework

In calitate de client al agentiei de turism Karpaten vom incerca:

1. Ne logam desi nu avem cont - nu ne va lasa, va da eroarea "Date de autentificare invalide."

2. Ne vom face cont dar lasam campul pentru nume gol - va da eroarea "Va rog introduceti numele dvs."

3. Ne vom inregistra cu succes

4. Vom cauta oferte de vacanta in Turcia cu plecare de pe 2 aeroporturi si verificam daca avem macar 5 oferte pentru fiecare.

# Set - up

Chrome: https://www.google.com/chrome/

         - web browserul folosit 

Python: https://www.python.org/downloads/

         - limbajul de programare
         
IDE-ul Pycharm: https://www.jetbrains.com/pycharm/download/ (Community)

        - editor de cod
        
In terminalul de la Pycharm vom instala (cu pip install) librariile externe:

-> Selenium

-> Webdriver-manager/webdrivermanager

-> Behave

         - o librărie BDD care va interpreta și rula testele scrise în Gherkin
         
-> Behave-html-formatter

         - ne ajută să generăm rapoarte BDD
         
# Clonare si rulare

 Pentru a importa un proiectul din github in calculator copiem url-ul din github, deschidem Git bash here in locatia unde vrem sa il copiem si introducem comanda –”git https://github.com/RamonaLupu/Proiect-Final-.git”.
 
 Pentru a rula fisierele BDD in terminalul de la Pycharm folosim  comanda – “ bevave –f behave-report.html

In urma rularii fisierelor, in terminal ne va aparea daca testele au fost passed sau failed. Si daca avem teste failed care sunt acestea.

Dar se va genera si un fisier cu raportul in format HTML care poate fi deschis cu ce browser dorim.

![image](https://user-images.githubusercontent.com/119336026/226827646-dd2a5875-896f-4b3d-89a8-5aa17a6d3f63.png)






