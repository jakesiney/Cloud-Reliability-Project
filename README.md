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
   One of the first enhancements involved securing the incoming traffic by implementing HTTPS protocol. This ensured encrypted communication, enhancing data privacy and safeguarding sensitive information exchanged within the system.

2. **X-Ray Results Integration:**
   Responding to a specific request from hospital nurses, we introduced a feature enabling the saving of X-Ray results directly within the patient notes. Previously, these results were not archived on the HOSP server, and this enhancement streamlined the process, providing a comprehensive patient record.

3. **Audit Trail Functionality:**
   To bolster system transparency and security, we developed an audit trail feature. This functionality empowered system administrators to track and monitor all user activities comprehensively. By providing an overview of user interactions, it became easier to identify any potential security breaches promptly and take necessary actions.

These improvements collectively elevated the system's functionality, user experience, and security standards, ensuring a robust and seamless operation for both hospital staff and patients.