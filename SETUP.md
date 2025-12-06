# Setup & Implementation Guide – Pokémon API Client

This guide explains how to install, configure, and run the Pokémon API Client so that users can reliably fetch Pokémon data and save it to a CSV file. The goal is to provide clear, step-by-step onboarding instructions similar to real-world technical implementation workflows.

---

## 1. Prerequisites

Before starting, make sure you have:

- Python 3.8 or higher installed  
- Git (recommended for cloning the repository)  
- A stable internet connection (the script retrieves data from the PokéAPI)

Check your Python version:

python --version  
or  
python3 --version  

---

## 2. Downloading the Project

### Option A — Clone from GitHub (recommended)

git clone https://github.com/<your-username>/pokemon-api-client.git  
cd pokemon-api-client  

### Option B — Download ZIP

1. Go to the GitHub repository page  
2. Click **Code → Download ZIP**  
3. Extract the folder  
4. Open a terminal inside the extracted folder  

---

## 3. (Optional) Create a Virtual Environment

Using a virtual environment keeps dependencies isolated.

Create the environment:

python -m venv venv  

Activate it:

**Windows:**  
venv\Scripts\activate  

**macOS / Linux:**  
source venv/bin/activate  

---

## 4. Install Dependencies

Install the required package:

pip install requests  

If pip is unrecognized:

python -m pip install requests  
or  
pip3 install requests  

---

## 5. Configuration

By default, the script fetches data for three Pokémon:

names = ["pikachu", "bulbasaur", "charmander"]

To customize which Pokémon are fetched:

1. Open **pokemon_api.py**  
2. Find the `names` list near the bottom  
3. Replace or add Pokémon names (all lowercase), for example:

names = ["snorlax", "mewtwo", "gengar"]

---

## 6. Running the Script

From the project directory, run:

python pokemon_api.py

If everything is set up correctly, the script will:

1. Fetch data for each Pokémon  
2. Print results in the terminal  
3. Save structured data to **pokemon_data.csv**

---

## 7. Verifying Output

After running the script:

- A file named **pokemon_data.csv** should appear in the project directory
- It should contain the following columns:
  - name
  - height
  - weight
  - base_experience
- The terminal should show printed Pokémon data for each name

Open the CSV using:

- Excel  
- Google Sheets  
- VS Code  
- Any text editor  

If the CSV does not appear:

- Check for terminal errors  
- Ensure at least one Pokémon name is valid  
- Confirm you're inside the project folder when running the script  

---

## End of Setup Guide

Your Pokémon API Client is now fully installed and ready for use.



