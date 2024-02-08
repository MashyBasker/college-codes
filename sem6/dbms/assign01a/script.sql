drop database organization;
create database organization;
use organization;

SET foreign_key_checks = 0;

create table if not exists `Employee` (
  `Fname` varchar(255) not null,
  `Minit` varchar(255),
  `Lname` varchar(255),
  `Ssn` INT not null primary key,
  `Bdate` DATE not null,
  `Address` TEXT not null,
  `Sex` CHARACTER not null,
  `Salary` INT not null,
  `Super_ssn` INT not null references `Employee`(`Ssn`),
  `Dno` INT not null
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign01a/Employee.txt' into table `Employee`;

create table if not exists `Department` (
    `Dname` varchar(255) not null,
    `Dnumber` INT not null primary key,
    `Mgr_ssn` INT not null,
    `Mgr_start_date` DATE not null
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign01a/Department.txt' into table `Department`;

create table if not exists `Dept_Locations` (
    `Dnumber` INT not null,
    `Dlocation` varchar(255) not null primary key
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign01a/Dept_Locations.txt' into table `Dept_Locations`;

create table if not exists `Project` (
    `Pname` varchar(255) not null,
    `Pnumber` varchar(255) not null primary key,
    `Plocation` TEXT not null,
    `Dnum` INT not null
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign01a/Project.txt' into table `Project`;

create table if not exists `Works_On` (
    `Essn` INT not null primary key,
    `Pno` varchar(255) not null,
    `Hours` INT not null
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign01a/Works_On.txt' into table `Works_On`;

create table if not exists `Dependent` (
    `Essn` INT not null primary key,
    `Dependent_name` varchar(255),
    `Sex` CHARACTER,
    `Bdate` DATE,
    `Relationship` TEXT
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign01a/Dependent.txt' into table `Dependent`;