# Personal Financial Analysis System.

A Data Science and Machine Learning system for personal financial analysis, providing dashboards, data visualizations, financial indicators, forecasting, and reports for a comprehensive view of an individual's financial situation.

## Technologies:

- SQL.
- PostgreSQL.
- Python.
    - Matplotlib.
    - NumPy.
    - Pandas.
    - Scikit-learn.
    - SQLAlchemy.
    - Flask.
- HTML/CSS.
- JavaScript.
- Excel.
- Docker.

## How to run.

### Prerequisites.

- [Docker](https://www.docker.com/).
- Docker Compose.

### Running the application.

#### 1. Clone this repository:

```bash
git clone https://github.com/devgustavosmota/personal_financial_analysis.git
cd personal_financial_analysis
```

#### 2. Environment variables:

Create a `.env` file based on `.env.example`.

```bash
cp .env.example .env
```

#### 3. Build and start the containers:

```bash
docker compose up --build
```

The application will be available at: http://localhost:5000

To stop the application:

```bash
docker compose down
```

## Status.

This project is currently under development.