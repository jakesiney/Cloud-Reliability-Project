<h1 align="center">
Reliability Project
</h1>

<p align='center'>This repo contains the files for my final project at Makers Academy as part of the Cloud/DevOps Engineering specialism track.</p>

## Project Overview

In this project, our team was commissioned by a organization that delivers software and services to several veterinary hospitals. Our primary goal was to enhance the reliability of their existing application, HOSP, while ensuring its core functionality remained intact. Additionally, we undertook the responsibility of implementing various improvements and incorporating new features to elevate the overall user experience.


## The HOSP system
Unfortunately we didnt have access to the source code due to a licensing issue, but we did have access to the load balancer on AWS and the API documentation.</br>
![HOSP Diagram](/diagrams/HOSP-diagram.jpg)



## Approach and Investigation

Our initial focus was on enhancing the system's reliability. To address user-reported issues, we delved into the problem by utilizing Amazon CloudWatch to analyse the application logs. Through this investigation, we discovered a significant volume of failed API requests occurring at the server endpoints. This crucial insight allowed us to pinpoint the root causes of the issues users were experiencing.


## Implementation of NGINX Reverse Proxy Server

To tackle the challenge of failed API requests, we implemented an NGINX reverse proxy server deployed on an AWS EC2 instance. This strategic deployment was designed to automatically retry the failed requests, resulting in a remarkable reduction in the overall number of failures. By leveraging this solution, we effectively enhanced the system's resilience and ensured a smoother user experience.

![dashboard](/diagrams/dashboard.png)


## Implemented Improvements

With the system's reliability significantly enhanced, we shifted our focus to implementing several crucial improvements:

1. **Enhanced Security with HTTPS:**
   To reinforce the system's security, we prioritized implementing the HTTPS protocol. This crucial step involved deploying an AWS CloudFront CDN and enforcing encrypted communication across all traffic. By transitioning to HTTPS, we significantly enhanced data privacy and ensured the safeguarding of sensitive information exchanged within the system.

    Collaborating closely with corporate IT, we planned the migration process. Our objective was to minimize downtime during the transition to the new domain. We directed traffic to the new HTTPS-enabled domain, maintaining uninterrupted service for users while fortifying the system's overall security.

2. **X-Ray Results Integration:**
   Responding to a specific request from hospital nurses, we introduced a feature enabling the saving of X-Ray results directly within the patient notes. Previously, these results were not archived on the HOSP server, and this enhancement streamlined the process, providing a comprehensive patient record. To achieve this, we developed a sophisticated solution leveraging AWS Lambda and Python. We crafted a Lambda function capable of capturing the API response from the screening server. Subsequently, the function initiated a new POST request back to the patient notes endpoint. This request was meticulously designed, incorporating the patient ID within the header and encapsulating the X-Ray results as a structured JSON payload all while making sure the original request was delivered back to user.

3. **Audit Trail Functionality:**
   To bolster system transparency and security, we developed an audit trail feature. This functionality allowed system administrators to track and monitor all user activities. By providing an overview of user interactions, it became easier to identify any potential security breaches promptly and take necessary actions. The audit trail feature was implemented using an AWS Lambda function. We established a new API route, designed to query AWS Athena using a specific SQL command against a CloudWatch database. The results of this query were then sent back as a unique URL, allowing them to download the audit trail as a CSV file for detailed analysis.

These improvements collectively elevated the system's functionality, user experience, and security standards, ensuring a robust and seamless operation for both hospital staff and patients.








