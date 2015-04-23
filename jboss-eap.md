JBoss EAP Notes
===============

## CLI

`jboss_cli.sh --connect controller=myjboss-host:9999` -- connect to the JBoss CLI port

## Tricks

### Turn on Access Logging

More info: <https://access.redhat.com/solutions/185383>

In `<virtual-server name="default-host>`, add this line:

```
<access-log pattern="%h %l %u %t %r %s %b %{Referer}i %{User-Agent}i %S %T" prefix="access_log_"/>
```
