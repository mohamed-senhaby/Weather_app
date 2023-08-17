# Headquarter Weather FastAPI Application

This FastAPI application fetches and displays weather information for a specified headquarters' location using the Open-Meteo API. Users can access the weather data, including the current temperature and time, and optionally include information about maximum temperature and apparent temperature for the day.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (version 3.6 or higher)
- FastAPI (install using `pip install fastapi`)
- Requests library (install using `pip install requests`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/headquarter-weather-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd headquarter-weather-app
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

   The application will start and will be accessible at `http://localhost:8000` in your web browser.

2. To access weather information, open your web browser or use a tool like `curl` or Postman and navigate to:

   - Current Weather: `http://localhost:8000/headquarter-weather`
   - Current Weather with Maximum Information: `http://localhost:8000/headquarter-weather?include_maximum=True`

   The API responses will be in JSON format.

### API Endpoint

- Endpoint: `/headquarter-weather`
- Query Parameters:
  - `include_maximum`: (optional) Set to `True` to include maximum temperature and apparent temperature information for the day.

### Project Structure

- `main.py`: The main FastAPI application script that defines the API endpoint and handles requests.
- `requirements.txt`: Contains the list of required Python packages.
- `README.md`: This README file providing project information.

### Contributing

Contributions are welcome! If you find any issues or want to add features, feel free to submit a pull request.

