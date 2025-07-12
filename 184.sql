SELECT Department.Name AS Department , Employee.Name AS Employee, Salary FROM Employee JOIN Department ON Employee.DepartmentId=Department.Id

WHERE (DepartmentId,Salary) IN


(SELECT departmentId, MAX(salary) FROM Employee
GROUP BY DepartmentId)