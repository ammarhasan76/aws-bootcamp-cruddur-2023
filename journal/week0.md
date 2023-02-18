# Week 0 — Billing and Architecture

10/FEB/2023
Completed remaining outstanding preparatory steps - all accounts and config steps

11/FEB/2023
Completed watching livestream on YouTube
https://www.youtube.com/watch?v=SG8blanhAOg&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=12

***NOTE: ill for a few days***

16/FEB/2023 
Completed watching Chirag's Week 0 - Spend Considerations (Pricing Basics & Free Tier)
https://www.youtube.com/watch?v=OVw3RrlP-sI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=13
Study Notes:

    AWS Bill Walkthrough
        Root user or IAM user with billing perms
        Pricing varies according to region
        Bills in menu(in USD and local ccy)
        Free Tier in menu - all listed (Current, forecasted usage)

    Billing Alerts (CloudWatch Alarm & Budget)
        Billing preference menu
        Some options
            PDF invoice by email
            Fre tier usage alerts
            Receive billing alerts
        Clicking on manage billing alert -> (US-East-1) -> CloudWatch -> create alert -> choose options -> SNS topic -> email
        or
        Clicking on Budgets -> Create Budget (Global) -> will alert when threshold of spending crossed (% based)
        
    Cost Explorer
        Cost Management -> Cost Explorer
        Cost Management -> Reports

    Calculate AWS estimates cost of service
        Pricing - use calc variables (service, instance size, region etc) on the public AWS calculator website then calc a manual estimate 	and compare to the site (730hr vs 744hrs)

    Check AWS Credits (voucher)
        Billing -> Credits (redeem if you have)

    Cost allocation tags
        Clicking on Cost Alloc Tags -> Activate tags for cost acvitites

    Free forever vs free for 12m
        AWS Free Tier public website
        Filter by Always Free vs 12m free vs trials

18/FEB/2023
Completed watching Ashish's Week 0 - Security Considerations (AWS Organizations & AWS IAM Tutorial For Beginners)
https://www.youtube.com/watch?v=4EMWBYVggQI&list=PLBfufR7vyJJ7k25byhRXJldB5AiwgNnWv&index=15
Study Notes: 
    Cyber Security = Technology risk the business may be exposed to
    Cloud Security = protect data, apps, services in your Cloud envrionments from internal and external security threats
    1. Reduce impact of breach
    2. Protect networks, apps, services from data theft
    3. Reduce human error
    Cloud/Cloud security - takes practice due to complexity, new services, threat actors improving capability

    Enable MFA for root account - already done!
    MFA important as compromised domain admin account = game over
    Can double check byu going to main profile -> secruity credentials and review root user config

    Create an OU
    

