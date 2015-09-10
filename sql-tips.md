# Useful SQL Commands

* `alter user MYUSER account unlock` - unlock an account
* inline view query
```sql		
SELECT * 
  FROM ( SELECT deptno, count(*) emp_count
         FROM emp
         GROUP BY deptno ) emp,
       dept
 WHERE dept.deptno = emp.deptno;
```

## Oracle specific
* _plsql_ check to see if a column exists before adding

```sql
select count(*) into vRowCount
	from DBA_TAB_COLUMNS
    	where OWNER = '{owner}'
	and TABLE_NAME = '{table}'
	and COLUMN_NAME = '{column}' ;

-- Create the new column
IF vRowCount <= 0 THEN
```

* `tnsping mysid` -- check that a SID exists in your configured `tnsnames.ora`
* kill a session -- _todo: fill this out_


```sql
select username, user#, sid, serial#, inst_id from gv$session where machine =
 
SQL> ALTER SYSTEM KILL SESSION 'sid,serial#' IMMEDIATE;
```

* who locked an account - <https://community.oracle.com/thread/1016170>
```sql
select OS_USERNAME, USERNAME , USERHOST, RETURNCODE, TIMESTAMP
from dba_audit_session
where to_date(TIMESTAMP, 'DD-Mon-YY') in (select to_date(TIMESTAMP, 'DD-Mon-YY')
from dba_audit_session
where to_date(TIMESTAMP,'DD-Mon-YY') = to_date(sysdate, 'DD-Mon-YY'))
and RETURNCODE = 28000;
```

* `to_date` usage - see [more examples](http://www.techonthenet.com/oracle/functions/to_date.php)

```sql
TO_DATE('2003/07/09', 'yyyy/mm/dd')
```

* use `dba_errors` to find SQL issues:

```sql
select name,sequence,line,position,text
from dba_errors
where owner='{schema}'
and name='{object_name}';  -- like a package name for instance
```

* change user password

```sql
ALTER USER user_name IDENTIFIED BY new_password;
```
