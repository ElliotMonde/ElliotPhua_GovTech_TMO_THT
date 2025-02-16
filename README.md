
# Elliot Phua TMO THT

Hi, my name is [Elliot Phua](https://www.linkedin.com/in/elliotphua/). This is my submission for the GovTech TMO THT 2025, **Question 2 - REST APIs**.

## Outline

The application is a GPA monitoring tool to view the cumulative grades of students within a timeframe between semester 1 to semester 8. The grading system used is out of 5.0. There is also a feature to update a student's assigned teacher.

## Deployment

The backend service is deployed using Railway.app . This is the [base url](elliotphuagovtechtmotht-production.up.railway.app) of the APIs. There is also a frontend interface deployed through Vercel to [try out the app here](https://elliot-phua-gov-tech-tmo-tht.vercel.app/). It might take a few seconds to fetch the data on page load.

The database is managed on Neon PostgreSQL.

![Screenshot of deployment](image.png)
## Table of Content

- [Elliot Phua TMO THT](#elliot-phua-tmo-tht)
  - [Outline](#outline)
  - [Deployment](#deployment)
  - [Table of Content](#table-of-content)
  - [Set-up Instructions](#set-up-instructions)
    - [Download the files](#download-the-files)
  - [Considerations \& Design Decisions](#considerations--design-decisions)
  - [Assumptions](#assumptions)

## Set-up Instructions
This section will guide you through setting up and running the backend application.
### Download the files
On your terminal, git clone
## Considerations & Design Decisions

```YAML
API URL: {Base URL}/students
Method: GET
Response: 
```

```YAML
API URL: {Base URL}/student/{student_id}
Method: PATCH
Request Body:
Response: 
```

```YAML
API URL: {Base URL}/students-grades?earliest_semester={earliest_semester}&latest_semester={latest_semester}
Method: GET
Response: 
```

## Assumptions
