Java/JVM Notes
==============

Table of Contents
-----------------

* [Debugging](#debugging)
* [Security](#security)
* [Resources](#resources)
      * [Java 8](#java-8)    
      * [Libraries](#libraries)
      * [DesignPatterns](#design-patterns)
* [Detailed Notes](#detailed-notes)


## Debugging

+ [Turn on Debugger](http://stackoverflow.com/questions/138511/what-are-java-command-line-options-to-set-to-allow-jvm-to-be-remotely-debugged)

        * java 1.5+
                
                -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=1044
        
        * java 1.4
                
                -Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=1044

+ Turn on [JMX Remote Debugging][1]


        yourJavaCommand... -Dcom.sun.management.jmxremote   
        -Dcom.sun.management.jmxremote.ssl=false   
        -Dcom.sun.management.jmxremote.authenticate=false   
        -Dcom.sun.management.jmxremote.port=1098  

+ Get a Thread Dump using `jstack`
```
sudo jstack -F -l {pid} > ~/{file_name} 2>&1
```

+ Debug SOAP messages  
    * Run the Java Web Start client at https://code.google.com/p/tcpmon/

+ Add a file to an existing jar
```
jar uf <jar_file> <file>
```

+ run a [junit test](https://github.com/junit-team/junit/wiki/Getting-started) from the command line
```
java -cp .:/usr/share/java/junit.jar org.junit.runner.JUnitCore [test class name]
```

## Security

+ test an SSL connection - [SSLPoke.java](https://gist.github.com/4ndrej/4547029)

### Keytool

- [Most Common keytool commands](https://www.sslshopper.com/article-most-common-java-keytool-keystore-commands.html)

* `keytool -list -keystore cacerts` -- list the certificates in the `cacerts` file. You will need to know the keystore pwd.
 
### Secure Password Storage

* http://blog.jerryorr.com/2012/05/secure-password-storage-lots-of-donts.html -- uses Java SE6 to generate secure pwd

## Resources

### Java 8

- [java8-tutorial](https://github.com/winterbe/java8-tutorial)

### Libraries

- [awesome-java](https://github.com/akullpp/awesome-java)

### Design Patterns

- [java-design-patterns](https://github.com/iluwatar/java-design-patterns)

## Detailed Notes
:100: _go to [Google Drive: Java Notes](https://docs.google.com/document/d/1P68nAfkay0KGi7elw56HflUxoxhCy96uTXtI0ToiImY/edit?usp=sharing) for notes on the JVM, useful libraries, language information, etc._

[1]: http://java.dzone.com/articles/visualvm-monitoring-remote-jvm

