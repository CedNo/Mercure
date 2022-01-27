import 'package:flutter/material.dart';
import 'package:mercure/ressources/constants.dart';
import 'package:mercure/ressources/routing.dart';
import 'package:mercure/themes/MercureTheme.dart';

class App extends StatefulWidget {
  const App({Key? key}) : super(key: key);

  final String title = 'Best Memes';

  @override
  State<StatefulWidget> createState() => AppState();
}

class AppState extends State<App> {

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Mercure',
      theme: MercureTheme.theme,
      initialRoute: homeRoute,
      onGenerateRoute: Routing.generateRoute,
    );
  }
}