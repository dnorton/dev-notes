# Useful SQL Commands

* `alter user MYUSER account unlock` - unlock an account
* inline view query
		
			SELECT * 
			  FROM ( SELECT deptno, count(*) emp_count
			         FROM emp
			         GROUP BY deptno ) emp,
			       dept
			 WHERE dept.deptno = emp.deptno;

* check to see if a column exists before adding

		select count(*) into vRowCount
			from DBA_TAB_COLUMNS
	    		where OWNER = '{owner}'
			and TABLE_NAME = '{table}'
	        	and COLUMN_NAME = '{column}' ;
		
		-- Create the new column
		IF vRowCount <= 0 THEN

* `tnsping mysid` -- check that a SID exists in your configured `tnsnames.ora`
* kill a session -- _todo: fill this out_


```sql
select username, user#, sid, serial#, inst_id from gv$session where machine =
 
SQL> ALTER SYSTEM KILL SESSION 'sid,serial#' IMMEDIATE;
```

* `to_date` usage - see [more examples](http://www.techonthenet.com/oracle/functions/to_date.php)

```
TO_DATE('2003/07/09', 'yyyy/mm/dd')
```

* use `dba_errors` to find SQL issues:

```
select name,sequence,line,position,text
from dba_errors
where owner='{schema}'
and name='{object_name}';  -- like a package name for instance
```
