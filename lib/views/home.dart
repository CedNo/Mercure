import 'dart:async';
import 'dart:developer';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:mercure/main.dart';
import 'package:mercure/views/settings.dart';
import 'package:mercure/views/statistiques.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  static String webSocketURL = "ws://192.168.0.27:65000";

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {

  var channel;
  late Socket socket;

  bool channelIsConnected = false;

  //Le véhicule est en marche
  bool powerOn = false;

  //L'index de la page actuelle
  int _selectedIndex = 0;

  //Controlleur pour changer de page
  final PageController _pageController = PageController();

  //Les différents écrans
  late List<Widget> _screens;

  //Allume ou éteind le véhicule
  void togglePower(bool isOn) {
    setState(() {
      //Start le véhicule
      powerOn = isOn;
    });

    if(isOn){
      channel.sink.add('PowerOn');
    }
    else {
      channel.sink.add('PowerOff');
    }
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
    _screens = [
      Center(child:
        ElevatedButton(
          child: Text('Connexion'),
          onPressed: () {
          _connectToSocket();
        },
      )),
      Center(child: CircularProgressIndicator()),
      Settings(),
    ];
  }

  void _connectToSocket() async {
    log("Connecting");

    setState(() {
      _screens = [
        Center(child: CircularProgressIndicator()),
        Center(child: CircularProgressIndicator()),
        Settings(),
      ];
    });

    try{

      //socket = await Socket.connect("192.168.0.27", 65000);

      channel = await WebSocketChannel.connect(
        Uri.parse('ws://192.168.0.27:65000'),
      );

      log("Connected");

      channelIsConnected = true;

      _screens = [
        Statistiques(channel: channel,),
        Center(child: CircularProgressIndicator()),
        Settings(),
      ];
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
              onChanged: channelIsConnected ? (bool value) { togglePower(value); } : null,
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