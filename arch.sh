#!/bin/bash

# Root directory of the project
mkdir -p job_scraping_project
cd job_scraping_project || exit

# Create data directories
mkdir -p data/raw
mkdir -p data/processed

# Create notebooks directory
mkdir -p notebooks

# Create src directory and subdirectories
mkdir -p src/scrapers
mkdir -p src/api

# Create tests directory
mkdir -p tests

# Create ui directory and subdirectories
mkdir -p ui/templates
mkdir -p ui/static/css
mkdir -p ui/static/js

# Create config directory
mkdir -p config

# Create logs directory
mkdir -p logs

# Create required files
touch data/raw/.gitkeep
touch data/processed/.gitkeep
touch notebooks/.gitkeep
touch src/scrapers/indeed_scraper.py
touch src/scrapers/linkedin_scraper.py
touch src/scrapers/twitter_scraper.py
touch src/api/linkedin_api.py
touch src/api/twitter_api.py
touch src/data_preprocessing.py
touch src/database.py
touch src/analysis.py
touch tests/test_scrapers.py
touch tests/test_api.py
touch tests/test_data_preprocessing.py
touch tests/test_database.py
touch tests/test_analysis.py
touch ui/templates/.gitkeep
touch ui/static/css/.gitkeep
touch ui/static/js/.gitkeep
touch ui/app.py
touch ui/dashboard.py
touch config/config.yaml
touch config/credentials.yaml
touch logs/.gitkeep
touch requirements.txt
touch README.md
touch setup.py

# Print success message
echo "Project structure created successfully."

