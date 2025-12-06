# Pokémon API Client

A simple Python script that retrieves data from the public PokéAPI, handles network and API errors gracefully, and saves results to a CSV file.  
This project demonstrates real-world skills useful for Technical Support Engineering and Implementation roles, including API integration, error handling, automation, and basic data storage.

---

## Features

- Fetches Pokémon data from the PokéAPI using HTTP GET requests  
- Handles common errors:
  - API downtime  
  - Invalid Pokémon names  
  - Network/connectivity issues  
  - Slow responses (timeout handling)  
  - Invalid JSON responses  
- Extracts and stores relevant fields (name, height, weight, base experience)  
- Saves results into a structured CSV file  
- Clean, reusable functions for easy extension   

---

## Example Output

Sample content saved to `pokemon_data.csv`:

