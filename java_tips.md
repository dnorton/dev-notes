Java and JVM Tips
-----------------

+ Turn on JMX Remote Debugging

<code>
yourJavaCommand... -Dcom.sun.management.jmxremote 
-Dcom.sun.management.jmxremote.ssl=false 
-Dcom.sun.management.jmxremote.authenticate=false 
-Dcom.sun.management.jmxremote.port=1098
</code>

  

#### References

`http://java.dzone.com/articles/visualvm-monitoring-remote-jvm`
