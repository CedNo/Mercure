import 'dart:developer';
import 'dart:io';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class Statistiques extends StatefulWidget {
  var channel;

  Statistiques({Key? key, required this.channel}) : super(key: key);

  @override
  _StatistiquesState createState() => _StatistiquesState(channel);
}

class _StatistiquesState extends State<Statistiques> with AutomaticKeepAliveClientMixin {
  _StatistiquesState(this.channel);

  var channel;

  @override
  Widget build(BuildContext context) {
    super.build(context);

    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(5.0),
        child: Column(
          children: [
            StreamBuilder(
              stream: channel.stream,
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

                  log(snapshot.data.toString());

                  String _distance = snapshot.data.toString();

                  return GridView.count(
                    primary: false,
                    padding: const EdgeInsets.all(20),
                    crossAxisSpacing: 10,
                    mainAxisSpacing: 10,
                    crossAxisCount: 2,
                    children: <Widget>[
                      //Vitesse

                      //Distance parcourue
                      Center(
                        child: Text(_distance),
                      ),
                    ],
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
            TextButton(
                onPressed: () {
                  channel.sink.add('TEST');
                },
                child: const Text("Test")),
          ],
        ),
      ),
    );
  }

  @override
  bool get wantKeepAlive => true;
}
