<h1 align="center">
 Cloud Reliability Team Project
</h1>

<p align='center'>This repo contains the files for my final project at Makers Academy as part of the Cloud/DevOps Engineering specialism track.</p>

## Project Overview

In this project, our team was commissioned by a organization that delivers software and services to several veterinary hospitals. Our primary goal was to enhance the reliability of their existing application, HOSP, while ensuring its core functionality remained intact. Additionally, we undertook the responsibility of implementing various improvements and incorporating new features to elevate the overall user experience.


## The HOSP system
Unfortunately we didnt have access to the source code due to a licensing issue, but we did have access to the load balancer on AWS and the API documentation.</br>
![HOSP Diagram](/diagrams/HOSP-diagram.jpg)



## Approach and Investigation

Our initial focus was on enhancing the system's reliability. To address user-reported issues, we delved into the problem by utilizing Amazon CloudWatch to analyse the application logs. Through this investigation, we discovered a significant volume of failed API requests occurring at the server endpoints. This crucial insight allowed us to pinpoint the root causes of the issues users were experiencing.


