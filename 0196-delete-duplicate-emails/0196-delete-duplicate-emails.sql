# Write your MySQL query statement below
delete p 
from Person p 
inner join Person p2 
    on  p.Email = p2.Email 
    and  p.Id > p2.Id;