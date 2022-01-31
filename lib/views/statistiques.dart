import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'home.dart';

class Statistiques extends StatefulWidget {
  const Statistiques({Key? key}) : super(key: key);

  @override
  _StatistiquesState createState() => _StatistiquesState();
}

class _StatistiquesState extends State<Statistiques> with AutomaticKeepAliveClientMixin {
  @override
  Widget build(BuildContext context) {
    super.build(context);

    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(5.0),
        child: GridView.count(
          crossAxisCount: 2,
          children: <Widget>[
            StreamBuilder(
              stream: Home.getChannel().stream,
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
          ],
        ),
      ),
    );
  }

  @override
  bool get wantKeepAlive => true;
}
