import 'package:flutter/material.dart';
import './Animations/customPageRoute.dart';
import './screens/loginScreen.dart';
import './screens/signupScreen.dart';
import 'package:google_fonts/google_fonts.dart';
import 'screens/welcomeScreen.dart';
import 'screens/signupScreen.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    final textTheme = Theme.of(context).textTheme;
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        textTheme:GoogleFonts.latoTextTheme(textTheme).copyWith(
           headline1: GoogleFonts.montserrat(textStyle: textTheme.bodyText1),
         ),
        visualDensity: VisualDensity.adaptivePlatformDensity,
        pageTransitionsTheme: PageTransitionsTheme(
          builders: {
            TargetPlatform.android: CustomPageTransitionBuilder(),
          }
        ),
      ),
      debugShowCheckedModeBanner: false,
      home: WelcomeScreen(),
      routes: {
        SignUpScreen.routeName : (ctx)=> SignUpScreen(),
        LoginScreen.routeName : (ctx) => LoginScreen(),

      },
    );
  }
}

