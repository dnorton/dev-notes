Gradle Notes
------------

home: [gradle.org](https://gradle.org)

generate a new build.gradle from an existing `pom.xml`

```gradle
gradle init --type pom
```
 
Add a Manifest file to the jar to make it runnable:
```gradle
jar {
    manifest {
        attributes 'Main-Class': 'com.foo.bar.MainClass'
    }
}
```

stop gradle daemon:
```bash
gradle -stop
```

Run a group of tests[*](https://stackoverflow.com/questions/22505533/how-to-run-only-one-test-class-on-gradle):
```bash
gradle test --tests '*LocalIT*'
```
