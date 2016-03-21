IntelliJ Tips and Tricks
========================
_as of IntelliJ 14.0.3_

## Table of Contents
* [shortcuts](#intellij-shortcuts)
* [projects](#project-tricks)
* [debugging](#debugging)
* [references](#references)


### IntelliJ Shortcuts

_replace `Ctl` with `Cmd` for OSX :apple:_

+ `Ctl + Plus/Minus` -- expand/collapse code folding
+ `Ctl + W` -- smart select. Continue to type W to expand the selection.
+ `Alt + F1` + `Enter` -- jump to the file in the Project View
+ `Ctl + Alt + Left/Right` -- go back or forward to last point (useful if traversing a call stack)
+ `Ctl + P` -- show method parameters
+ `Ctl + B` -- go to declaration (for any element in a class)
+ `Ctl + Alt + H` -- [show call hierarchy](https://www.jetbrains.com/idea/help/building-call-hierarchy.html)
+ `Ctl + N` -- go to a class file in the project :star:
+ `Ctl + Shift + N` -- go to any file in the project :star:
+ `Ctl + E` -- show recent files
 
_Thanks to [Trisha Gee](http://trishagee.github.io/post/stuff_i_learnt_about_intellij/) for these shortcuts below_

+ `Ctl + Shift + A` -- navigate directly to an action/option
+ `Ctl + Shift + Enter` -- [statement completion](https://confluence.jetbrains.com/display/IntelliJIDEA/Code+Completion#CodeCompletion-4.Statementcompletion)
+ `Ctl + Shift + S` -- open `settings` menu
+ `Ctl + Shift + Alt + S` -- open `project structure` menu
+ `!` -- [negating completion](https://confluence.jetbrains.com/display/IntelliJIDEA/Code+Completion#CodeCompletion-5.Negatingcompletion)
+ `Ctl + F12` -- navigate w/i a class
 
_Refactoring_

+ `Ctl + Alt + M` -- extract selected code into a new method

### Project Tricks
+ To open a Gradle project for the first time: `"Open"` -> Navigate to `build.gradle` file
+ [turn off IntelliJ tabs](http://hadihariri.com/2014/06/24/no-tabs-in-intellij-idea/)
+ `Ctl + Shift + [0-9]` -- set a numbered bookmark
+ `Ctl + [0-9]` -- jump to numbered bookmark

### Debugging
+ [Debug Maven test in IntelliJ](http://stackoverflow.com/questions/6573289/intellij-idea-debugger-skips-breakpoints-when-debugging-maven-tests)
+ [Cleaning System Cache](https://www.jetbrains.com/idea/help/cleaning-system-cache.html) -- to manually delete system cache, go to `%userprofile%\.IntelliJ##\system`
+ Add this to breakpoint to only stop every 10th item
+ [Run Inspections Offline](https://www.jetbrains.com/idea/help/running-inspections-offline.html) :thumbsup:

```java
myList.size() % 10 == 0
```

### References
1. http://trishagee.github.io/
2. https://www.jetbrains.com/idea/docs/IntelliJIDEA_ReferenceCard.pdf
3. http://www.radcortez.com/my-most-useful-intellij-idea-keyboard-shortcuts/
4. https://medium.com/@andrey_cheptsov/top-20-navigation-features-in-intellij-idea-ed8c17075880?source=most-recommended

