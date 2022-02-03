import 'dart:async';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:mercure/main.dart';
import 'package:mercure/views/statistiques.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {

  static late Socket socket;

  List<Widget> screen = <Widget>[const CircularProgressIndicator()];

  void dataHandler(data){
    print(new String.fromCharCodes(data).trim());
  }

  void errorHandler(error, StackTrace trace){
    print(error);
  }

  void doneHandler(){
    socket.destroy();
  }

  Socket getSocket() {
    return socket;
  }

  //Le véhicule est en marche
  bool powerOn = false;

  //L'index de la page actuelle
  int _selectedIndex = 0;

  //Controlleur pour changer de page
  final PageController _pageController = PageController();

  //Les différents écrans
  final List<Widget> _screens = [

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
    screen = <Widget>[CircularProgressIndicator()];

    _connectToSocket();
  }

  void _connectToSocket() async {
    debugPrint("Connecting");
    socket = await Socket.connect("192.168.0.27", 9999);
    debugPrint("Connected");
    socket.listen(dataHandler,
        onError: errorHandler,
        onDone: doneHandler,
        cancelOnError: false);

    setState(() {
      screen = <Widget>[
          StreamBuilder(
          stream: socket,
          builder: (context, snapshot) {
            /// We are waiting for incoming data data
            if (snapshot.connectionState == ConnectionState.waiting) {
              return const Center(
                child: CircularProgressIndicator(),
              );
            }

            /// We have an active connection and we have received data
            if (snapshot.connectionState == ConnectionState.active &&
                snapshot.hasData) {
              return Center(
                child: Text(
                  '${snapshot.data}}',
                  style: const TextStyle(
                    color: Colors.redAccent,
                    fontSize: 24.0,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              );
            }

            /// When we have closed the connection
            if (snapshot.connectionState == ConnectionState.done) {
              return const Center(
                child: Text(
                  'No more data',
                  style: TextStyle(
                    color: Colors.red,
                  ),
                ),
              );
            }

            /// For all other situations, we display a simple "No data"
            /// message
            return const Center(
              child: Text('No data'),
            );
          },
        ),
      ];

    });
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
        children: screen,
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