import 'package:flutter/material.dart';

class MercureTheme {

  //Couleurs
  static const Color _mainLightBlue = Colors.lightBlue;

  static ThemeData theme = ThemeData(
    appBarTheme: const AppBarTheme(
      color: _mainLightBlue,
      titleTextStyle: TextStyle(
        color: Colors.white,
      ),
    ),
    bottomNavigationBarTheme: const BottomNavigationBarThemeData(
      selectedItemColor: _mainLightBlue,
      showSelectedLabels: false,
      showUnselectedLabels: false,
    ),
  );
}