# Useful SQL Commands

* `alter user MYUSER account unlock` - unlock an account
* inline view query
		
			SELECT * 
			  FROM ( SELECT deptno, count(*) emp_count
			         FROM emp
			         GROUP BY deptno ) emp,
			       dept
			 WHERE dept.deptno = emp.deptno;
