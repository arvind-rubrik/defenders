insert into compliance_rule_results(rule_id, provider, region,  result,
message, timestamp) values (1, 'aws', 'us-west-2', 'PASS','anant.mahajan has Password enabled but MFA disabled', '2019-06-07T22');
insert into compliance_rule_results(rule_id, provider, region, result,
message, timestamp) values (1, 'aws', 'us-west-2', 'FAIL','anant.mahajan has Password enabled but MFA disabled', '2019-06-07T22');
