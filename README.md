# CSCI5409 Term Assignment

This repository contains the code for a basic e-commerce web application developed as a term assignment for the CSCI5409 course. The project is structured into two main directories: `frontend` and `backend`, alongside important configuration and documentation files at the root level.

## Project Structure

- **frontend/**: Contains the React application setup using Vite and styled with ShadCN. This part of the project is responsible for the user interface of the e-commerce platform.
- **backend/**: Hosts the serverless backend implementation, including AWS Lambda functions for product listing and order processing, integrated with other AWS services like API Gateway, S3, and SNS.
- **cloudformation.yaml**: AWS CloudFormation template for provisioning the infrastructure required for the project.
- **TermAssignment2024W.pdf**: The assignment document detailing the project requirements, objectives, and evaluation criteria.

## Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- Node.js (v14 or later)
- npm or yarn
- AWS CLI (configured with your AWS account)
- An AWS account with appropriate permissions to create and manage the resources defined in `cloudformation.yaml`

## Setup Instructions

### Deploying the Backend

1. Navigate to the `backend` directory:
   ```sh
   cd backend
   ```
2. Deploy the AWS infrastructure using CloudFormation:
   ```sh
   aws cloudformation deploy --template-file ../cloudformation.yaml --stack-name <YOUR_STACK_NAME> --capabilities CAPABILITY_IAM
   ```
3. Update any necessary configurations in your Lambda function code based on the resources created by CloudFormation.

### Setting Up the Frontend

1. Navigate to the `frontend` directory:
   ```sh
   cd frontend
   ```
2. Install the dependencies:
   ```sh
   npm install
   ```
   or if you're using yarn:
   ```sh
   yarn
   ```
3. Start the development server:
   ```sh
   npm run dev
   ```
   or with yarn:
   ```sh
   yarn dev
   ```

The application should now be running and accessible at `http://localhost:3000`.

## Usage

Navigate to `http://localhost:3000` in your web browser to view the e-commerce platform. You can browse products, add them to your cart, and simulate a checkout process that calculates totals, applies discounts and taxes, and sends a receipt via email.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with any enhancements, bug fixes, or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
