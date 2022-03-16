# Mercure
Voiture autonome pour le cours de projet d'intégration phase II et Domaine d'exploration technologique phase II

## Matériel requis
- [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) (min 4GB RAM)
- [Raspberry Pi camera](https://www.amazon.ca/-/fr/SainSmart-Objectifs-fish-eye-Raspberry-Arduino/dp/B00N1YJKFS/ref=sr_1_15?keywords=raspberry+pi+camera&qid=1647363658&sprefix=raspberry+pi+came%2Caps%2C57&sr=8-15)
- [IOT kit](https://www.amazon.ca/-/fr/d%C3%A9marrage-Raspberry-tutoriels-d%C3%A9taill%C3%A9s-dexp%C3%A9rimentation/dp/B06W54L7B5/ref=sr_1_15?keywords=iot+kit&qid=1647363695&sprefix=iot+k%2Caps%2C59&sr=8-15) (Doit comprendre: cablage, résistance, sonar, accéléromètre, photoresistor)
- [Voiture téléguidée](https://www.amazon.ca/-/fr/perseids-Voiture-tout-terrain-t%C3%A9l%C3%A9command%C3%A9e-vitesse/dp/B08F3DY6RC/ref=sr_1_17?crid=2768RHPZXIO62&keywords=rc%2Bcar%2Bjeep&qid=1647363604&sprefix=rc%2Bcar%2Bjee%2Caps%2C71&sr=8-17&th=1)
- [L298N](https://www.amazon.ca/Moteur-contr%C3%B4leur-H-bridge-disques-contr%C3%B4le/dp/B07G81G3BP/ref=sr_1_2_sspa?keywords=l298n&qid=1647363362&sprefix=%2Caps%2C42&sr=8-2-spons&psc=1&smid=A36ZH2MCHPKXUA&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVlJPOVU1TlpJRVgyJmVuY3J5cHRlZElkPUEwODM2MDM2WVM2TlVINEk3QzdYJmVuY3J5cHRlZEFkSWQ9QTA2OTM3OTkxNUJaR08zSDdKNTA3JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==) Carte contrôleur de moteur
- Ruban adhésif (couleur bleu idéalement)
- Fer à souder
- Fil pour soudure
- Panneau stop (Jouet ou impression 3D)

## Logiciel requis
- [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- [Image Raspbian Buster](https://www.raspberrypi.com/software/operating-systems/)
- [ROS](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Kinetic%20on%20the%20Raspberry%20Pi)
- [OpenCV](https://qengineering.eu/install-opencv-4.5-on-raspberry-pi-4.html)
- [Mosquitto](https://xperimentia.com/2015/08/20/installing-mosquitto-mqtt-broker-on-raspberry-pi-with-websockets/)
- [Fritzing](https://fritzing.org/download/)

## Exemple schéma branchement
Voici la liste de nos branchements

Pour voir plus en détail les branchements tous les fichiers sont à votre disposition dans le dossier **Schema branchement**. (Vous devez télécharger Fritzing pour les consulters)


Branchement moteur pour les roues
![Motor](/Schema%20branchement/Motor.png)
