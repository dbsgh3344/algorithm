select ps.firstName,ps.lastName,ad.city,ad.state 
from person as ps left join address as ad 
on ps.personid = ad.personid