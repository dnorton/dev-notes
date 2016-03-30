Gradle Notes
------------

home: [gradle.org](https://gradle.org)

* `gradle init --type pom` -- generate a new build.gradle from an existing `pom.xml`

Add a Manifest file to the jar to make it runnable:
```
jar {
    manifest {
        attributes 'Main-Class': 'com.foo.bar.MainClass'
    }
}
```
