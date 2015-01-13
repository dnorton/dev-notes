## IntelliJ

* [Debug Maven test in IntelliJ](http://stackoverflow.com/questions/6573289/intellij-idea-debugger-skips-breakpoints-when-debugging-maven-tests)

### IntelliJ Shortcuts

+ `Ctl + Plus/Minus` -- expand/collapse code folding
+ `Ctl + W` -- smart select. Continue to type W to expand the selection.
+ `Alt + F1` + `Enter` -- jump to the file in the Project View
+ `Ctl + Alt + Left` -- go back to last point (useful if traversing a call stack)
+ `Ctl + P` -- show method parameters
+ `Ctl + Alt + H` -- [show call hierarchy](https://www.jetbrains.com/idea/help/building-call-hierarchy.html)
 
__Thanks to [Trisha Gee](http://trishagee.github.io/post/stuff_i_learnt_about_intellij/) for these shortcuts below__
+ `Ctl + Shift + A` -- navigate directly to an action/option
+ `Ctl + Shift + Enter` -- [statement completion](https://confluence.jetbrains.com/display/IntelliJIDEA/Code+Completion#CodeCompletion-4.Statementcompletion)
+ `Ctl + Shift + S` -- open =settings= menu
+ `Ctl + Shift + Alt + S` -- open =project structure= menu
+ `!` -- [negating completion](https://confluence.jetbrains.com/display/IntelliJIDEA/Code+Completion#CodeCompletion-5.Negatingcompletion)


### Debugging

+ Add this to breakpoint to only stop every 10th item

```java
myList.size() % 10 == 0
```

### References
1. http://trishagee.github.io/
