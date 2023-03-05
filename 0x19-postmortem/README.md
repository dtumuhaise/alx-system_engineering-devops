# 0x19. Postmortem

# 0. My first postmortem

## Issue Summary:
GuitarShopPro experienced a partial outage on March 3, 2023, from 1:00 PM to 3:00 PM (EAT). During the outage, users experienced slow page load times and unresponsiveness, affecting approximately 75% of our user base. The root cause of the outage was a network connectivity issue with our cloud service provider.

## Timeline:
- 1:00 PM (EAT): Monitoring alerts showed a significant increase in response time, and engineers were immediately alerted.
- 1:05 PM (EAT): Engineers began investigating the issue, checking server logs and system metrics to identify the root cause.
- 1:15 PM (EAT): Assumptions were made that the issue might be related to high traffic or a potential DDoS attack.
- 1:30 PM (EAT): After further investigation, it was discovered that the root cause was a network connectivity issue with our cloud service provider.
- 2:00 PM (EAT): The issue was escalated to senior engineers to work with the cloud service provider to resolve the issue.
- 3:00 PM (EAT): After two hours of downtime, the issue was resolved, and full functionality of the web application was restored.

## Root Cause and Resolution:
The root cause of the outage was identified as a network connectivity issue with our cloud service provider. One of the primary data centers used by GuitarShopPro to host the web application experienced a power outage, causing a disruption in our services. The issue was further compounded by a misconfiguration in our failover mechanisms, which failed to switch traffic to our secondary data center, resulting in a complete outage. To resolve the issue, our engineering team worked closely with our cloud service provider to address the network connectivity issue and to implement a fix for the misconfiguration in our failover mechanisms.

## Corrective and Preventative Measures:
To prevent a similar incident from happening in the future, GuitarShopPro will be implementing the following corrective and preventative measures:

- Improving our failover mechanisms: We will review and improve our failover mechanisms to ensure that they are reliable and can effectively switch traffic to our  secondary data center in the event of a disruption.
- Implementing redundancy: We will explore options for implementing redundancy within our cloud infrastructure to ensure that we have backup resources in the event of a disruption.
- Monitoring and alerting: We will implement more robust monitoring and alerting systems to quickly identify and respond to any potential disruptions in our services.

## Conclusion:
We apologize for any inconvenience or frustration caused by the outage. GuitarShopPro takes this incident seriously and is committed to providing the highest levels of availability and reliability for our users. If you have any questions or concerns, please do not hesitate to contact our support team at support@guitarshoppro.com.