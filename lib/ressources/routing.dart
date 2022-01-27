import 'package:flutter/material.dart';
import 'package:mercure/views/home.dart';

import 'constants.dart';

class Routing {
  static Route<dynamic> generateRoute (RouteSettings settings) {
    switch (settings.name) {
      case homeRoute: return PageRouteBuilder(pageBuilder: (_, __, ___) => const Home());
    //case messagesRoute: return PageRouteBuilder(pageBuilder: (_, __, ___) => Memes());
      default:
        return MaterialPageRoute(
            builder: (_) => Scaffold(
              body: Center(
                  child: Text('404 : No route defined for ${settings.name}')),
            )
        );
    }
  }
}