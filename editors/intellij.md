# IntelliJ Tips and Tricks

~~as of IntelliJ 14.0.3~~

🚧 _under review for 2022.1.3_

## Table of Contents

- [shortcuts](#intellij-shortcuts)
- [projects](#project-tricks)
- [debugging](#debugging)
- [references](#references)

### IntelliJ Shortcuts

🤌 _replace `Ctl` with `⌘ (Cmd)` for MacOS_

- `Ctl + Plus/Minus` -- expand/collapse code folding
- `Ctl + Backspace` -- delete current line
- `Ctl + W` -- smart select. Continue to type W to expand the selection. `⌥ + Up/Down` for MacOs
- `⌘ + 1` -- go to Project View
- `Ctl + Alt + Left/Right` -- go back or forward to last point (useful if traversing a call stack)
- `Ctl + P` -- show method parameters
- `Ctl + B` -- go to declaration (for any element in a class)
- `Ctl + Alt + H` -- [show call hierarchy](https://www.jetbrains.com/idea/help/building-call-hierarchy.html)
- `Ctl + N` -- go to a class file in the project :star:
- `Ctl + Shift + N` -- go to any file in the project :star:
- `Ctl + E` -- show recent files
- `Ctl + Shift + K` -- git push
- `Ctl + Ctl` -- _run anything_

_Thanks to [Trisha Gee](http://trishagee.github.io/post/stuff_i_learnt_about_intellij/) for these shortcuts below_

- `Ctl + Shift + A` -- navigate directly to an action/option (e.g., collapse/expand)
- `Ctl + Shift + Enter` -- [statement completion](https://confluence.jetbrains.com/display/IntelliJIDEA/Code+Completion#CodeCompletion-4.Statementcompletion)
- `Ctl + Shift + S` -- open `settings` menu
- `Ctl + Shift + Alt + S` -- open `project structure` menu
- `!` -- [negating completion](https://confluence.jetbrains.com/display/IntelliJIDEA/Code+Completion#CodeCompletion-5.Negatingcompletion)
- `Ctl + F12` -- navigate w/i a class

_Refactoring_

- `Ctl + Alt + M` -- extract selected code into a new method
- `Ctl + O` -- generate override method(s)

Selection Menu

- `Option + F1` and then `1` for `Project view`

### Project Tricks

- To open a Gradle project for the first time: `"Open"` -> Navigate to `build.gradle` file
- [turn off IntelliJ tabs](http://hadihariri.com/2014/06/24/no-tabs-in-intellij-idea/)
- `Ctl + Shift + [0-9]` -- set a numbered bookmark
- `Ctl + [0-9]` -- jump to numbered bookmark

### Debugging

- [Debug Maven test in IntelliJ](http://stackoverflow.com/questions/6573289/intellij-idea-debugger-skips-breakpoints-when-debugging-maven-tests)
- [Cleaning System Cache](https://www.jetbrains.com/idea/help/cleaning-system-cache.html) -- to manually delete system cache, go to `%userprofile%\.IntelliJ##\system`
- Add this to breakpoint to only stop every 10th item
- [Run Inspections Offline](https://www.jetbrains.com/idea/help/running-inspections-offline.html) :thumbsup:

```java
myList.size() % 10 == 0
```

- `Ctl + F8` -- toggle breakpoint
- `Shift + F9` -- Run Debug

### References

1. http://trishagee.github.io/
2. https://www.jetbrains.com/idea/docs/IntelliJIDEA_ReferenceCard.pdf
3. http://www.radcortez.com/my-most-useful-intellij-idea-keyboard-shortcuts/
4. https://medium.com/@andrey_cheptsov/top-20-navigation-features-in-intellij-idea-ed8c17075880?source=most-recommended
