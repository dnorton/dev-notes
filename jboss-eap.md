JBoss EAP Notes
===============

Table of Content
----------------

* [CLI](#cli)
* [Tricks](#tricks)
  * [Turn on Access Logging](#turn-on-access-logging)
  * [Enable HTTPS connections](#enable-https-connector)

## CLI

+ `jboss_cli.sh --connect controller=myjboss-host:9999` -- connect to the JBoss CLI port
+ `[standalone@myjboss-host:9999 /]module remove --name=module_name` -- remove a module


## Tricks

### Turn on Access Logging

More info: <https://access.redhat.com/solutions/185383>

In `<virtual-server name="default-host>`, add this line:

```
<access-log pattern="%h %l %u %t %r %s %b %{Referer}i %{User-Agent}i %S %T" prefix="access_log_"/>
```

### Add a tricky system property
```
[standalone@dev2-qdsapp4:9999 /] /system-property=ldap_searchBase:add(value="DC=
test,OS=test2")
```

### Enable HTTPS connector

_[Redhat.com: Implement SSL Encryption](https://access.redhat.com/documentation/en-US/JBoss_Enterprise_Application_Platform/6.1/html/Security_Guide/Implement_SSL_Encryption_for_the_JBoss_Enterprise_Application_Platform_Web_Server1.html)_

1. Add the HTTPS connector  
  ```
  /profile=default/subsystem=web/connector=HTTPS/:add(socket-binding=https,scheme=https,protocol=HTTP/1.1,secure=true)
  ```
2. Configure the keystore  
  ```
  /profile=default/subsystem=web/connector=HTTPS/ssl=configuration:add(name=https,certificate-key-file="${jboss.server.config.dir}/keystore.jks",password=SECRET, key-alias=KEY_ALIAS)
  ```
  
or just edit the _standalone.xml_ directly:

```
<connector name="http" protocol="HTTP/1.1" scheme="http" socket-binding="http"  redirect-port="8443" />
 
  <connector name="https" scheme="https" protocol="HTTP/1.1" socket-binding="https" enable-lookups="false" secure="true">
<ssl name="foo-ssl" password="secret" protocol="TLSv1" key-alias="foo" certificate-key-file="../standalone/configuration/foo.keystore" />
  </connector>
```

