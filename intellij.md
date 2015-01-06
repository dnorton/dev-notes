## IntelliJ

* [Debug Maven test in IntelliJ](http://stackoverflow.com/questions/6573289/intellij-idea-debugger-skips-breakpoints-when-debugging-maven-tests)

### IntelliJ Shortcuts

+ `Ctl + Plus/Minus` -- expand/collapse code folding
+ `Ctl + W` -- smart select. Continue to type W to expand the selection.
+ `Alt + F1` + `Enter` -- jump to the file in the Project View
+ `Ctl + Alt + Left` -- go back to last point (useful if traversing a call stack)
+ `Ctl + P` -- show method parameters
+ `Ctl + Alt + H` -- [show call hierarchy](https://www.jetbrains.com/idea/help/building-call-hierarchy.html)

### Debugging

+ Add this to breakpoint to only stop every 10th item

```java
myList.size() % 10 == 0
```
