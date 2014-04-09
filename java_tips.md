Java and JVM Tips
-----------------

+ Turn on [JMX Remote Debugging][1]


        yourJavaCommand... -Dcom.sun.management.jmxremote   
        -Dcom.sun.management.jmxremote.ssl=false   
        -Dcom.sun.management.jmxremote.authenticate=false   
        -Dcom.sun.management.jmxremote.port=1098  

+ Get a Thread Dump using `jstack`

        
        sudo jstack -F -l {pid} > ~/{file_name} 2>&1

+ Debug SOAP messages  
    * Run the Java Web Start client at https://code.google.com/p/tcpmon/

+ Add a file to an existing jar

        jar uf <jar_file> <file>

[1]: http://java.dzone.com/articles/visualvm-monitoring-remote-jvm

