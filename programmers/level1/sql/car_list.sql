-- 네비게이션 옵션이 포함된 차 리스트를 내림차순으로 출력
SELECT * from car_rental_company_car where options like '%네비게이션%' order by car_id desc;
