Java and JVM Tips
-----------------
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

+ run a junit test from the command line
```
java -cp .:/usr/share/java/junit.jar org.junit.runner.JUnitCore [test class name]
```

[1]: http://java.dzone.com/articles/visualvm-monitoring-remote-jvm

