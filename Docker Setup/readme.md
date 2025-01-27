# Docker Setup
To containerize the application, a Dockerfile is provided for easy setup and deployment.

## 1. Create a Docker Image
Make sure Docker is installed on your machine. To build the Docker image for the application, follow these steps:

### i. Create a `Dockerfile` (if not already present)
Dockerfile defines the steps needed to create a containerized environment for your Flask application, including setting up the Python environment, installing dependencies, and configuring the app to run on port 5000.
### ii. Create `requirements.txt` file
The `requirements.txt` file is a plain text file that lists all the Python packages and dependencies that your project requires. These packages will be installed when setting up the environment (for example, inside a Docker container or a virtual environment). Each package is listed on a new line, often with a specific version number to ensure compatibility and reproducibility.

## 2. Build the Docker Image
In the project directory, run:
```
bash
docker build -t quiz-api .
```
This command will create a Docker image named `quiz-api`.

## 3. Running the Docker Container
Once the image is built, you can run the Flask application in a container with the following command:

```bash
docker run -p 5000:5000 quiz-api
```
This will start the Flask application in a Docker container, accessible at `http://localhost:5000/`.

## 4. Testing the API
After starting the Flask application, you can test it using tools like curl, Postman, or directly through your browser.
Below given is curl command that you can run in your command promt. Make sure to navigate to your working directory before running this command.
```bash
curl -X POST -F "student_data=@student_data.json" http://localhost:5000/upload-student-data
```
This will upload a JSON file containing student data for analysis.
