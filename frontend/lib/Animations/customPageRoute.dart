import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';


class CustomPageTransitionBuilder extends PageTransitionsBuilder {
  @override
  Widget buildTransitions<T>(
      PageRoute<T> route,
      BuildContext context,
      Animation<double> animation,
      Animation<double> secAnimation,
      Widget child) {
         //AnimationController _controller = AnimationController(duration: const Duration(milliseconds: 2000));
         animation = CurvedAnimation(parent: animation, curve: Curves.bounceInOut);
    return FadeTransition(opacity: animation, child: child);
  }
}
