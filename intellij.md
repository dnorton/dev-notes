## IntelliJ

* [Debug Maven test in IntelliJ](http://stackoverflow.com/questions/6573289/intellij-idea-debugger-skips-breakpoints-when-debugging-maven-tests)

### IntelliJ Shortcuts

_for the most part, replace `Ctl` with `Cmd` for OSX_

+ `Ctl + Plus/Minus` -- expand/collapse code folding
+ `Ctl + W` -- smart select. Continue to type W to expand the selection.
+ `Alt + F1` + `Enter` -- jump to the file in the Project View
+ `Ctl + Alt + Left/Right` -- go back to last point (useful if traversing a call stack)
+ `Ctl + P` -- show method parameters
+ `Ctl + B` -- go to declaration (for any element in a class)
+ `Ctl + Alt + H` -- [show call hierarchy](https://www.jetbrains.com/idea/help/building-call-hierarchy.html)
 
_Thanks to [Trisha Gee](http://trishagee.github.io/post/stuff_i_learnt_about_intellij/) for these shortcuts below_
+ `Ctl + Shift + A` -- navigate directly to an action/option
+ `Ctl + Shift + Enter` -- [statement completion](https://confluence.jetbrains.com/display/IntelliJIDEA/Code+Completion#CodeCompletion-4.Statementcompletion)
+ `Ctl + Shift + S` -- open =settings= menu
+ `Ctl + Shift + Alt + S` -- open =project structure= menu
+ `!` -- [negating completion](https://confluence.jetbrains.com/display/IntelliJIDEA/Code+Completion#CodeCompletion-5.Negatingcompletion)
+ `Ctl + F12` -- navigate w/i a class


### Debugging

+ Add this to breakpoint to only stop every 10th item

```java
myList.size() % 10 == 0
```

### References
1. http://trishagee.github.io/
2. https://www.jetbrains.com/idea/docs/IntelliJIDEA_ReferenceCard.pdf
3. http://www.radcortez.com/my-most-useful-intellij-idea-keyboard-shortcuts/
