import 'dart:async';
import 'dart:developer';
import 'dart:io';

import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';
import 'package:mercure/main.dart';
import 'package:mercure/views/statistiques.dart';

class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {

  late Socket socket;

  //Le véhicule est en marche
  bool powerOn = false;

  //L'index de la page actuelle
  int _selectedIndex = 0;

  //Controlleur pour changer de page
  final PageController _pageController = PageController();

  //Les différents écrans
  List<Widget> _screens = [
    CircularProgressIndicator(),
    CircularProgressIndicator(),
    CircularProgressIndicator(),
  ];

  //Allume ou éteind le véhicule
  void togglePower(bool isOn) {
    setState(() {
      //Start le véhicule
      powerOn = isOn;
    });
  }

  //Action déclancher lorsqu'on change de page
  void _onPageChanged(int index){
    setState(() {
      _selectedIndex = index;
    });
  }

  //Action lorsqu'on clique sur les différents onglets de la barre de navigation
  void _onItemTapped(int selectedIndex) {
    _pageController.jumpToPage(selectedIndex);
  }

  @override
  void initState() {
    _connectToSocket();
  }

  void _connectToSocket() async {
    log("Connecting");

    try{

      socket = await Socket.connect("192.168.0.27", 65000);

      log("Connected");
      log("Socket" + socket.toString());

      setState(() {
        _screens = [
          Statistiques(socket: socket,),
          Statistiques(socket: socket,),
          Statistiques(socket: socket,),
        ];
      });

      log("Connected");
    }
    catch(error) {
      log(error.toString());
    }
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        title: const Text(
            'Mercure',
          style: TextStyle(
            fontFamily: 'BreeSerif',
            fontSize: 24,
          ),
        ),
        actions: <Widget>[
          // Icone de courrant
          const Icon(Icons.flash_on_outlined),
          // Switch pour allumer ou éteindre le véhicule
          Switch(
              value: powerOn,
              onChanged: (bool value) {
                togglePower(value);

              },
            activeTrackColor: Colors.lightGreen,
            activeColor: Colors.green,
            inactiveThumbColor: Colors.red,
            inactiveTrackColor: Colors.redAccent,
          ),
        ],
        elevation: 0,
      ),
      body: PageView(
        controller: _pageController,
        children: _screens,
        onPageChanged: _onPageChanged,
        physics: const NeverScrollableScrollPhysics(),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.auto_graph),
            label: 'Statistiques',
            tooltip: 'Statistiques',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.car_repair),
            label: 'Véhicule',
            tooltip: 'Véhicule',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.settings),
            label: 'Paramètres',
            tooltip: 'Paramètres',
          ),
        ],
        currentIndex: _selectedIndex,
        onTap: _onItemTapped,
      ),
    );
  }
}