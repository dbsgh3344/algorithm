# num값을 shift하여 새로운 컬럼으로 추가한 가상테이블 정의
with a as (
  select num,lead(num) over() as l_1, lead(num,2) over() as l_2
  from logs
  )

select distinct t.ans as ConsecutiveNums
from (
  select case when l_1 = num and l_2 = num then num else null end ans from a
  ) as t where t.ans is not null;