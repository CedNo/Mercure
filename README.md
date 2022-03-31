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

- **Branchement Photoresistor et LED**
![Photoresistor](/Schema%20branchement/image/Photoresistor.png)

- **Branchement Accéléromètre**

![Accelerometre](/Schema%20branchement/image/accelerometre.png)

## Instruction pour l'installation et les branchements des pièces
1. Désassembler la voiture téléguidée et retirer toutes les composantes qui ne serviront plus
2. Tester chacune des pièces au Raspberry Pi pour s'assurer qu'elles fonctionnent bien
3. Une fois les vérifications terminées trouver un emplacement pour votre Raspberry Pi
![Raspberry Pi_emplacement](/Image_Mercure/raspberryPi.jpg)
5. Installer votre Raspberry Pi dans la voiture
6. Trouver un emplacement pour le sonar (capteur de distance) à l'avant du véhicule
7. Faire les modifications nécessaire, le mettre en place et installer vos fils
8. Identifier vos cables
![Sonar_inst](/Image_Mercure/sonar.jpg)
7. Trouver un emplacement pour le photoresistor
8. Faire les modifications nécessaire et le mettre en place
![Photoresistor_inst](/Image_Mercure/photoresistor_inst.png)
9. Relier les lumières du véhicule avec le photoresistor vous pouvez vous fier au schéma des branchements pour comprendre le filage
10. Identifier vos cables
![Lumieres_inst](/Image_Mercure/lumieres_inst.png)
11. Relier le servo-moteur au Raspberry Pi
12. Trouver un emplacement pour carte L298N (Le L298N est une carte de moteur à double pont en H qui permet le contrôle de la vitesse et de la direction de deux moteurs à courant continu en même temps.)
![L298N_inst](/Image_Mercure/L298N.jpg)
14. Relier le moteur de la voiture à la carte L298N en se fiant au schéma de branchement
15. Identifier vos cables
16. Brancher la batterie de la voiture à la carte L298N
17. Installer l'accéléromètre sur la voiture et installer vos cables
![Accelerometre_inst](/Image_Mercure/accelerometre.jpg)
18. Faire passer vos cables jusqu'au Raspberry Pi pour chaque module
![Acces_cable](/Image_Mercure/cable_management.jpg)
19. Trouver un emplacement à la camera
20. Faire les modifications nécessaires et installer la caméra
![Camera_inst](/Image_Mercure/camera.jpg)
21. Une fois les composantes installées remonter la voiture<br/>
Voici notre résultat final
![voiture final](/Image_Mercure/final.jpg)

## Code pour faire fonctionner la voiture
**Prendre note que nous avons du suivre un cours de ROS sur Udemy pour comprendre le fonctionnement de l'environnement ROS**
Une fois que votre Raspberry pi est prêt et que votre voiture est terminée. Vous pouvez télécharger les scripts dans le dossier Scripts et les mettres dans votre Raspberry pi.

1. Pour faire fonctionner les scripts vous allez devoir vous créer un nouveau package ROS ou vous pouvez directement prendre notre package ROS dans github<br/>
  cd ~/ros_catkin_ws/src<br/>
  catkin_create_pkg dev_merc1 std_msgs rospy roscpp<br/>
2. Ensuite, vous devez build le package<br/>
  cd ~/ros_catkin_ws/src<br/>
catkin_make<br/>
3. Ajouter votre workspace à votre environnement ROS <br/>
  . ~/ros_catkin_ws/devel/setup.bash<br/>
4. Ajouter les scripts dans le dossier /src de votre package ROS (Facultatif si vous avez le package ROS) <br/>
  cd ~/ros_catkin_ws/src/nom_package/src <br/>
  cd ~/ros_catkin_ws/src/dev_merc1/src <br/>
5. Assurer vous que vos scripts sont exécutable dans le dossier src <br/>
  cd ~/ros_catkin_ws/src/dev_merc1/src<br/>
  chmod +x nomDuScript.py<br/>
6. Créer un fichier ROS launch pour partir tous les scripts (Facultatif si vous avez le package ROS)<br/>
  cd ~/ros_catkin_ws/src/dev_merc1<br/>
  mkdir launch<br/>
7. Copier le fichier mercure.launch dans ce dossier (Facultatif si vous avez le package ROS)<br/>
8. Rendre le ficher exécutable<br/>
  chmod +x mercure.launch<br/>
9. Ensuite, vous devez mettre le fichier AI sur votre bureau disponible dans scripts sur Github
9. Mainteant vous pouvez utiliser la commande suivante pour lancer les scripts<br/>
  roslaunch nom_package nom_ficher_launcher.launch<br/>
  roslaunch dev_merc1 mercure.launch<br/>
10. Maintenant que les scripts fonctionnent, il vous faut l'application MercureApp sur votre téléphone céllulaire pour faire fonctionner la voiture.<br/>
https://github.com/CedNo/MercureApp <br/>
11. Installer Android Studio<br/>
12. Cloner le projet<br/>
13. Installer l'appli sur votre voiture<br/>
14. Amuser vous<br/>


