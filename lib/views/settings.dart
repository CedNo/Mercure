import 'dart:developer';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'home.dart';

class Settings extends StatefulWidget {
  const Settings({Key? key}) : super(key: key);

  @override
  _SettingsState createState() => _SettingsState();
}

class _SettingsState extends State<Settings> {

  final _formKey = GlobalKey<FormState>();

  TextEditingController ipController = TextEditingController();
  TextEditingController portController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: <Widget>[
          TextFormField(
            controller: ipController,
            validator: (value) {
              if (value == null || value.isEmpty) {
                return value;
              }
              return null;
            },
          ),
          TextFormField(
            controller: portController,
            validator: (value) {
              if (value == null || value.isEmpty) {
                return value;
              }
              return null;
            },
          ),
          ElevatedButton(
            onPressed: () {
              if (_formKey.currentState!.validate()) {
                ScaffoldMessenger.of(context).showSnackBar(
                  const SnackBar(content: Text('Sauvegarde des informations...')),
                );

                Home.webSocketURL = 'ws://' + ipController.text + ':' + portController.text;
                log(Home.webSocketURL);
              }
            },
            child: const Text('Sauvegarder'),
          ),
        ],
      ),
    );
  }
}
