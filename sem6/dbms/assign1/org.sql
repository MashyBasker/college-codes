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

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign1/Employee.txt' into table `Employee`;

create table if not exists `Department` (
    `Dname` varchar(255) not null,
    `Dnumber` INT not null primary key,
    `Mgr_ssn` INT not null,
    `Mgr_start_date` DATE not null
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign1/Department.txt' into table `Department`;

create table if not exists `Dept_Locations` (
    `Dnumber` INT not null,
    `Dlocation` varchar(255) not null primary key
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign1/Dept_Locations.txt' into table `Dept_Locations`;

create table if not exists `Project` (
    `Pname` varchar(255) not null,
    `Pnumber` varchar(255) not null primary key,
    `Plocation` TEXT not null,
    `Dnum` INT not null
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign1/Project.txt' into table `Project`;

create table if not exists `Works_On` (
    `Essn` INT not null primary key,
    `Pno` varchar(255) not null,
    `Hours` INT not null
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign1/Works_On.txt' into table `Works_On`;

create table if not exists `Dependent` (
    `Essn` INT not null primary key,
    `Dependent_name` varchar(255),
    `Sex` CHARACTER,
    `Bdate` DATE,
    `Relationship` TEXT
);

load data local infile '/home/okabe/projects/college-codes/sem6/dbms/assign1/Dependent.txt' into table `Dependent`;

-- Setup all the foreign key relations: 
-- This is at the end because of the circular foreign key relationship
-- in the Employee and Department tables
alter table `Employee` add constraint fk_dept_no foreign key (`Dno`) references `Department`(`Dnumber`);
alter table `Department` add constraint fk_mgr_ssn foreign key (`Mgr_ssn`) references `Employee`(`Ssn`);
alter table `Dept_Locations` add constraint fk_dept_loc_dept_no foreign key (`Dnumber`) references `Department`(`Dnumber`);
alter table `Project` add constraint fk_proj_dept_no foreign key (`Dnum`) references `Department`(`Dnumber`);
alter table `Works_On` add constraint fk_works_essn_no foreign key (`Essn`) references `Employee`(`Ssn`);
alter table `Works_On` add constraint fk_works_proj_no foreign key (`Pno`) references `Project`(`Pnumber`);
alter table `Dependent` add constraint fk_dependent_essn_no foreign key (`Essn`) references `Employee`(`Ssn`);


-- Command to see relationships between the tables:
-- SELECT 
--   `TABLE_SCHEMA`,                          -- Foreign key schema
--   `TABLE_NAME`,                            -- Foreign key table
--   `COLUMN_NAME`,                           -- Foreign key column
--   `REFERENCED_TABLE_SCHEMA`,               -- Origin key schema
--   `REFERENCED_TABLE_NAME`,                 -- Origin key table
--   `REFERENCED_COLUMN_NAME`                 -- Origin key column
-- FROM
--   `INFORMATION_SCHEMA`.`KEY_COLUMN_USAGE`  -- Will fail if user don't have privilege
-- WHERE
--   `TABLE_SCHEMA` = SCHEMA()                -- Detect current schema in USE 
--   AND `REFERENCED_TABLE_NAME` IS NOT NULL;