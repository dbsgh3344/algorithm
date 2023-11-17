select 
    emp.name as Employee 
from 
    employee as emp 
join 
    (select * from employee) as emp2 
on emp.managerId = emp2.id 
where emp.salary > emp2.salary;