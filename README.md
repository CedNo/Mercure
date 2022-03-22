# Mercure
Voiture autonome pour le cours de projet d'intégration phase II et Domaine d'exploration technologique phase II

## Matériel requis
- [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) (min 4GB RAM)
- [Micro SD](https://www.amazon.ca/-/fr/SanDisk-SDSQXA1-128G-GN6MN-Carte-m%C3%A9moire-microSDXC/dp/B082WP62DV/ref=asc_df_B082WP62DV/?tag=cafrdeshadgo-20&linkCode=df0&hvadid=459547836665&hvpos=&hvnetw=g&hvrand=8851779057536802210&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9000552&hvtargid=pla-898437604698&psc=1) (min 32GB)
- [Raspberry Pi camera](https://www.amazon.ca/-/fr/SainSmart-Objectifs-fish-eye-Raspberry-Arduino/dp/B00N1YJKFS/ref=sr_1_15?keywords=raspberry+pi+camera&qid=1647363658&sprefix=raspberry+pi+came%2Caps%2C57&sr=8-15)
- [IOT kit](https://www.amazon.ca/-/fr/d%C3%A9marrage-Raspberry-tutoriels-d%C3%A9taill%C3%A9s-dexp%C3%A9rimentation/dp/B06W54L7B5/ref=sr_1_15?keywords=iot+kit&qid=1647363695&sprefix=iot+k%2Caps%2C59&sr=8-15) (Dois comprendre: câblage, résistance, sonar, accéléromètre, photoresistor)
- [Voiture téléguidée](https://www.amazon.ca/-/fr/perseids-Voiture-tout-terrain-t%C3%A9l%C3%A9command%C3%A9e-vitesse/dp/B08F3DY6RC/ref=sr_1_17?crid=2768RHPZXIO62&keywords=rc%2Bcar%2Bjeep&qid=1647363604&sprefix=rc%2Bcar%2Bjee%2Caps%2C71&sr=8-17&th=1)
- [L298N](https://www.amazon.ca/Moteur-contr%C3%B4leur-H-bridge-disques-contr%C3%B4le/dp/B07G81G3BP/ref=sr_1_2_sspa?keywords=l298n&qid=1647363362&sprefix=%2Caps%2C42&sr=8-2-spons&psc=1&smid=A36ZH2MCHPKXUA&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVlJPOVU1TlpJRVgyJmVuY3J5cHRlZElkPUEwODM2MDM2WVM2TlVINEk3QzdYJmVuY3J5cHRlZEFkSWQ9QTA2OTM3OTkxNUJaR08zSDdKNTA3JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==) Carte contrôleur de moteur
- [Power bank](https://www.amazon.ca/-/fr/Batterie-compacte-PowerCore-batteries-technologie/dp/B0194WDVHI/ref=sr_1_6?crid=3V3TPE8KR7TOD&keywords=power+bank+anker&qid=1647986060&s=electronics&sprefix=power+bank+a%2Celectronics%2C60&sr=1-6)
- Ruban adhésif (couleur bleue idéalement)
- Fer à souder
- Fil pour soudure
- Panneau-stop (Jouet ou impression 3D)

## Logiciels requis
- [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- [Image Raspbian Buster](https://www.raspberrypi.com/software/operating-systems/)
- [ROS](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi)
- [OpenCV](https://qengineering.eu/install-opencv-4.5-on-raspberry-pi-4.html)
- [Mosquitto](https://xperimentia.com/2015/08/20/installing-mosquitto-mqtt-broker-on-raspberry-pi-with-websockets/)
- [Fritzing](https://fritzing.org/download/)

## Instruction téléchargement des logiciels
(Les liens de téléchargement sont dans la section logiciel requis)
1. Télécharger Raspberry Pi Imager 
2. Télécharger l'image Raspbian Buster
3. Flasher votre carte micro SD avec l'image de Buster avec Raspberry Pi Imager
4. Insérer la carte dans votre Raspberry pi et faire la configuration initiale (On vous recommande fortement d'activer VNC et SSH)
5. Faire les mises à jour
6. Débuter l'installation de ROS (Vous pouvez vous référer directement au wiki de ROS sinon il y a votre disposition un fichier **Commande_Installation.txt** avec toutes les commandes que nous avons exécuté)
7. Une fois que l'installation de ROS est complétée, installer OpenCV
8. Une fois que l'installation d'OpenCV est complétée, installer Mosquitto

## Exemple schéma branchement
Voici la liste de nos branchements

Pour voir plus en détail les branchements, tous les fichiers sont à votre disposition dans le dossier **Schema branchement**. (Vous devrez télécharger Fritzing pour les consulter)


- **Branchement moteur pour les roues**
![Motor](/Schema%20branchement/image/Motor.png)

- **Branchement servo moteur pour la direction**
![Servo_Motor](/Schema%20branchement/image/Servo_Motor.png)

- **Branchement Sonar(capteur de distance)**
![Sonar](/Schema%20branchement/image/Sonar.png)

- **Branchement Photoresistor**
![Photoresistor](/Schema%20branchement/image/Photoresistor.png)

## Instruction pour l'installation et les branchements des pièces
1. Désassembler la voiture téléguidée
2. Tester chacune des pièces dans le Raspberry Pi pour s'assurer qu'ils fonctionnent bien
3. Une fois les vérifications terminé trouver un emplacement pour votre Raspberry Pi
4. Installer votre Raspberry Pi 
5. Trouver un emplacement pour le sonar (capteur de distance) à l'avant du véhicule
6. Faire les modifications nécessaire pour le mettre en place

8. 
