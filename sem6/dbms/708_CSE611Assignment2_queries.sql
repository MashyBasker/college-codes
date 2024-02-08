-- 1
SET SERVEROUTPUT ON;
DECLARE
    v_employee_id Employees.EMPLOYEE_ID%TYPE;
    v_salary Employees.SALARY%TYPE;
    v_commission_pct Employees.COMMISSION_PCT%TYPE;
    v_incentive NUMBER;

    CURSOR employee_cursor IS
        SELECT EMPLOYEE_ID, SALARY, COMMISSION_PCT
        FROM Employees;

BEGIN
    -- Calculate and display incentive for employee with ID 110
    SELECT SALARY, COMMISSION_PCT
    INTO v_salary, v_commission_pct
    FROM Employees
    WHERE EMPLOYEE_ID = 110;

    v_incentive := v_salary * v_commission_pct;

    DBMS_OUTPUT.PUT_LINE('Incentive for Employee 110: $' || v_incentive);

    -- Calculate and display incentive for all employees
    FOR emp_rec IN employee_cursor LOOP
        v_incentive := emp_rec.SALARY * emp_rec.COMMISSION_PCT;
        DBMS_OUTPUT.PUT_LINE('Incentive for Employee ' || emp_rec.EMPLOYEE_ID || ': $' || v_incentive);
    END LOOP;
END;

--2
SET SERVEROUTPUT ON size 30000; 
DECLARE
sal NUMBER; eid NUMBER;
PROCEDURE new_sal ( sal_a IN OUT NUMBER, incr_a NUMBER
) IS
BEGIN sal_a := sal_a + incr_a;
END;
BEGIN
SELECT EMPLOYEE_ID,SALARY
INTO eid,sal
FROM EMPLOYEES
WHERE EMPLOYEE_ID = 122;
DBMS_OUTPUT.PUT_LINE(eid||'s OLD SALARY = ' || sal); new_sal(sal, 1500);
DBMS_OUTPUT.PUT_LINE(eid||'s NEW SALARY = ' || sal);
END;

-- 3
-- SET SERVEROUTPUT ON size 30000;
DECLARE
incent_per NUMBER := 10; h_date DATE; sal NUMBER; incentive DECIMAL; ename VARCHAR2(40); PROCEDURE incent( h1_date DATE, sal1 NUMBER
) IS
incent_per NUMBER := 10;
BEGIN
IF h1_date < DATE '2000-01-01' AND sal1 > 40000 THEN
incent_per := 20; END IF; incentive := incent_per/100*sal1;
END;
BEGIN
FOR i in (
SELECT (first_name||' '||last_name) as empname,HIRE_DATE, SALARY
INTO ename,h_date, sal
FROM Employees) LOOP ename := i.empname; h_date := i.HIRE_DATE;
sal := i.SALARY; incent(h_date,sal);
DBMS_OUTPUT.PUT_LINE(ename||' recieves an incentive of '||incentive);
END LOOP;
END;

-- 4
-- SET SERVEROUTPUT ON;
DECLARE
eid_count NUMBER; d_id NUMBER := 5;
BEGIN
SELECT COUNT(EMPLOYEE_ID)
INTO eid_count
FROM Employees
WHERE DEPARTMENT_ID = d_id;
DBMS_OUTPUT.PUT_LINE(eid_count||' employees works under Department #'||d_id);
IF eid_count < 100 THEN
DBMS_OUTPUT.PUT_LINE('There are '||(100-eid_count)||' vacancies');
ELSE
DBMS_OUTPUT.PUT_LINE('There are NO vacancies');
END IF;
END;


-- 5
SET SERVEROUTPUT ON;
DECLARE eid Employees.EMPLOYEE_ID%TYPE; dt1 Employees.HIRE_DATE%TYPE; get_day VARCHAR2(15);
BEGIN
FOR i IN(
SELECT EMPLOYEE_ID,HIRE_DATE
INTO eid,dt1
FROM Employees) LOOP eid := i.EMPLOYEE_ID; dt1 := i.HIRE_DATE; get_day := RTRIM(TO_CHAR(dt1, 'DAY')); IF get_day = 'SATURDAY' THEN
dt1 := dt1+2;
DBMS_OUTPUT.PUT_LINE('Employee #'||eid||' hire date modified to '|| dt1); ELSIF get_day = 'SUNDAY' THEN
dt1 := dt1+1;
DBMS_OUTPUT.PUT_LINE('Employee #'||eid||' hire date modified to '|| dt1);
END IF;
UPDATE Employees
SET HIRE_DATE = dt1
WHERE EMPLOYEE_ID = eid;
END LOOP;
END;


-- 6
-- SET SERVEROUTPUT ON;
DECLARE eid Employees.EMPLOYEE_ID%TYPE; sal Employees.SALARY%TYPE; mid_sal Employees.SALARY%TYPE;
BEGIN SELECT AVG(SALARY) INTO mid_sal FROM Employees;
FOR i IN
(SELECT E1.EMPLOYEE_ID,E1.SALARY
INTO eid,sal
FROM Employees E1) LOOP eid := i.EMPLOYEE_ID; sal := i.SALARY;
IF mid_sal <= sal THEN
UPDATE Employees
SET SALARY = sal * 1.08
WHERE EMPLOYEE_ID = eid;
DBMS_OUTPUT.PUT_LINE('Employee #'||eid||' salary modified to '|| sal);
ELSE
DBMS_OUTPUT.PUT_LINE('Employee #'||eid||' has salary less than '||
ROUND(mid_sal, 2));
END IF;
END LOOP;
END;



-- 7
-- SET SERVEROUTPUT ON;
DECLARE eid Employees.EMPLOYEE_ID%TYPE; h_date Employees.HIRE_DATE%TYPE; sal Employees.SALARY%TYPE;
BEGIN
FOR i IN(
SELECT EMPLOYEE_ID,SALARY,HIRE_DATE
INTO eid,sal,h_date
FROM Employees)
LOOP
eid := i.EMPLOYEE_ID; sal := i.SALARY; h_date := i.HIRE_DATE;
IF sal > 40000 and h_date < DATE '2015-01-01' THEN
DBMS_OUTPUT.PUT_LINE('Employee #'||eid||' has done rather well in rather short time');
ELSIF sal > 30000 and h_date < DATE '2013-01-01' THEN
DBMS_OUTPUT.PUT_LINE('Employee #'||eid||' has found a stable rise in the company and is reliable');
ELSIF h_date > DATE '2005-01-01' THEN
DBMS_OUTPUT.PUT_LINE('Employee #'||eid||' is highly commited to the company');
ELSIF h_date < DATE '2019-01-01' THEN
DBMS_OUTPUT.PUT_LINE('Employee #'||eid||' is too new to be judged');
ELSE
DBMS_OUTPUT.PUT_LINE('Employee #'||eid||' requires manual review');
END IF;
END LOOP;
END;
