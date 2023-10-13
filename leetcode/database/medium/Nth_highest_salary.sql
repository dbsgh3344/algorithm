CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT

BEGIN
        
        declare test int;
        set N = N-1;
        select distinct salary into test from employee order by salary desc limit 1 offset N;
        RETURN (test);
END