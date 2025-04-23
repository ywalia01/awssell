# AWSSell - A Full-Stack E-Commerce Web Application

## Project Overview

**AWSSell** is a full-stack e-commerce web application designed to provide a reliable, secure, and scalable online shopping experience. The application allows users to browse products, add them to their cart, and securely complete transactions. The platform integrates various AWS services, such as DynamoDB, Lambda, API Gateway, and SNS, to offer seamless scalability, security, and high availability.

## Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- [AWS Services Used](#aws-services-used)
- [Deployment Model](#deployment-model)
- [Security and Cost Efficiency](#security-and-cost-efficiency)
- [Setup and Deployment](#setup-and-deployment)
- [Usage](#usage)
- [Contact](#contact)

## Introduction

**AWSSell** is designed to provide an efficient and secure online shopping experience. The application allows users to search for products, add items to their cart, and complete purchases. After a successful transaction, users receive an electronic receipt via email. This project is built with the goal of ensuring speed, scalability, and security, with AWS services enabling these features.

## Architecture

![AWSSell Architecture](https://github.com/user-attachments/assets/422df1de-2752-463f-9b2c-21e2f207fca0)

### Purpose and Functionality

- **Product Browsing**: Users can search for products and view detailed descriptions.
- **Shopping Cart**: Products can be added to the cart for purchase.
- **Secure Transactions**: Users can complete their purchases securely and receive receipts via email.

### Target Audience

AWSSell targets a broad user base seeking an intuitive and secure online shopping experience. It is especially designed for individuals who value convenience and security while shopping online.

### Performance Targets

- **Speed and Efficiency**: Ensure fast load times and responsive performance.
- **Scalability**: Handle traffic spikes during peak shopping seasons.
- **Security**: Implement robust measures to protect user data and transactions.
- **User Experience**: Focus on creating an intuitive, seamless shopping experience.

## AWS Services Used

### Core Services

- **Amazon DynamoDB**: A fully managed NoSQL database used to store product and transaction data.
- **AWS Lambda**: A serverless compute service used for backend processing and logic handling.
- **Amazon API Gateway**: Manages and secures APIs, facilitating frontend-backend communication.
- **Amazon SNS**: Sends email notifications to users upon successful transactions.
- **AWS Secrets Manager**: Stores sensitive configuration data, like database credentials.

### Additional Services

- **Amazon EC2**: Hosts the frontend application for serving static content.
- **Amazon S3**: Stores static assets such as images and CSS files.

## Architecture

The architecture leverages AWS services to provide a secure and scalable infrastructure:

1. **Frontend Deployment**: The user interface is hosted on an EC2 instance.
2. **Backend Logic**: AWS Lambda handles backend logic, triggered by API Gateway requests.
3. **Data Storage**: Product and user transaction data is stored in DynamoDB.
4. **Notifications**: SNS sends emails to users post-transaction.

## Deployment Model

AWSSell uses a **Serverless Architecture** with managed services. Key advantages of this deployment model include:

- **Scalability**: The system scales automatically based on traffic.
- **Cost-Effectiveness**: Pay only for the resources used with the pay-as-you-go model.
- **Speed of Deployment**: Quick provisioning of resources and service updates.
- **Access to Advanced Services**: Utilize services like Lambda, DynamoDB, and API Gateway.

## Security and Cost Efficiency

### Security Measures

- **Data Security at Rest**: DynamoDB and AWS Secrets Manager ensure data encryption at rest.
- **Data Security in Transit**: All communication between the frontend and backend is encrypted using HTTPS.
- **Access Control**: Fine-grained IAM roles and policies control access to AWS services, following the principle of least privilege.

### Cost Efficiency

- **Serverless and Managed Services**: Lambda and other AWS services scale based on demand, reducing costs during idle periods.
- **CloudFormation**: Automates resource provisioning, ensuring repeatable and cost-effective deployments.

## Setup and Deployment

### Prerequisites

- AWS account
- AWS CLI configured
- Docker (for containerizing the application)
- Node.js and npm (for frontend development)

### Deployment Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ywalia01/csci5409-term-assign.git
   cd csci5409-term-assign
   ```

2. **Build and Deploy the Backend**:

   - Deploy Lambda functions using AWS CloudFormation.
   - Set up API Gateway and DynamoDB for handling requests.

3. **Deploy the Frontend**:

   - Host the React-based frontend on an EC2 instance or use AWS Amplify for simplified deployment.

4. **Set Up SNS for Notifications**:

   - Configure SNS to send transactional emails to users.

5. **Test the Application**:
   - Upload a product to DynamoDB and complete a transaction to verify the process.

## Usage

Once deployed, users can:

1. Browse products and add them to their cart.
2. Complete the checkout process by providing an email address.
3. Receive a confirmation email with transaction details.

## Contact

For more information, feel free to contact me at yashbest005@gmail.com.
