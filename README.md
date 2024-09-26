# Data Projects
Additional information from the remote branch.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```
    git clone https://github.com/artemis1005/data-projects.git
    ```

2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Run the data pipeline:
    ```
    python src/data_pipeline.py
    ```

4. To build and run using Docker:
    ```
    docker build -t data-pipeline .
    docker run data-pipeline
    ```

## Future Plans
- Add machine learning models for other datasets.
- Implement a Flask app to serve predictions.
- Integrate Airflow or Prefect for orchestrating the data pipeline.
