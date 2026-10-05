alter table partner add column if not exists credit_limit numeric(12,2);
--update partner set city = case id
                    --when 1 then 'mumbai'
                    --when 2 then 'pune'
                    --when 3 then 'delhi'
                    --end
                    --where id in (1,2,3);

select id,name,city,credit_limit from partner order by id;

UPDATE partner
SET city = CASE id
    WHEN 1 THEN 'Mumbai'
    WHEN 2 THEN 'Pune'
    WHEN 3 THEN 'Delhi'
    WHEN 4 THEN 'Mumbai'
    WHEN 5 THEN 'Ahmedabad'
    WHEN 6 THEN 'Pune'
    WHEN 7 THEN 'Delhi'
    WHEN 8 THEN 'Bengaluru'
    WHEN 9 THEN 'Mumbai'
    WHEN 10 THEN 'Ahmedabad'
    ELSE city
END
WHERE id BETWEEN 1 AND 10;

select id,name,city,credit_limit from partner order by id;

update partner set credit_limit = case id
      when 1 then 200000
      when 2 then 800000
      when 3 then 970089
      when 4 then 1289340
      when 5 then 278340
      when 6 then 280384
      when 7 then 389025
      when 8 then 23483
      when 9 then 278394
      when 10 then 273894
      else credit_limit end where id BETWEEN 1 and 10;


select id,name,city,credit_limit from partner order by id;
--group by
select city,count(*) as partner_count from partner group by city order by partner_count desc;
--sum 
select city,count(*) as partner_count,sum (credit_limit) as total_credit from partner group by city order by  total_credit desc