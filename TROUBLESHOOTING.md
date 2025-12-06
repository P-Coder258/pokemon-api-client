# Troubleshooting Guide – Pokémon API Client

This guide lists common issues users may encounter when running the Pokémon API Client and explains how to resolve them. These troubleshooting steps reflect real-world support workflows and error patterns.

---

## 1. Error: `ModuleNotFoundError: No module named 'requests'`

**Symptom:**  
Running `python pokemon_api.py` shows:

ModuleNotFoundError: No module named 'requests'

**Cause:**  
The `requests` library is not installed.

**Fix:**

pip install requests  
or  
python -m pip install requests  
or  
pip3 install requests  

---

## 2. Error: `Network error: Could not connect to API.`

**Symptom:**  
The script prints:

Network error: Could not connect to API.

**Possible Causes:**

- No internet connection  
- Network firewall blocking the request  
- PokéAPI is temporarily down  

**Fix:**

1. Check your internet connection  
2. Try opening this in your browser:  
   https://pokeapi.co/api/v2/pokemon/pikachu  
3. If the website is down, try again later  
4. If you're on school/work WiFi, try a different network  

---

## 3. Error: `HTTP Error` or `Error: Could not fetch data for '<name>'`

**Symptom:**  
The script prints:

HTTP Error: 404 Client Error  
or  
Error: Could not fetch data for 'somepokemon'

**Cause:**  
Invalid or misspelled Pokémon name.

**Fix:**

- Ensure all names are lowercase  
- Verify the name exists (example: pikachu, bulbasaur, charmander)  
- Test with a known-valid name to confirm  

---

## 4. Error: `Error: API returned invalid JSON.`

**Symptom:**  
The script prints:

Error: API returned invalid JSON.

**Cause:**  
PokéAPI returned HTML or invalid JSON (usually during downtime).

**Fix:**

1. Visit the API URL in a browser  
2. Check if JSON displays correctly  
3. If it's an error page, wait and try again later  

---

## 5. Error: `FileNotFoundError: [Errno 2] No such file or directory: 'pokemon_data.csv'`

**Symptom:**  
The script runs, but the CSV file can’t be found.

**Possible Causes:**

- Script failed before writing the CSV  
- All Pokémon names were invalid  
- You ran the script from a different folder  

**Fix:**

1. Verify at least one valid Pokémon name is in the list  
2. Re-run the script and check for terminal errors  
3. Ensure you are inside the project folder:

ls  
(Windows: dir)

You should see:
- pokemon_api.py  
- pokemon_data.csv (after running)

---

## 6. Error: `PermissionError: [Errno 13] Permission denied`

**Symptom:**  
The script prints a permission error when trying to create or write files.

**Cause:**  
You are trying to save files in a protected folder.

**Fix:**

- Move the project to a user-friendly location, like Desktop or Documents  
- Re-run the script from that folder  

---

## 7. Error: `Timeout` or Slow Responses

**Symptom:**  
The script prints:

Error: The request timed out.

**Possible Causes:**

- Slow internet  
- API server is slow  
- API endpoint under heavy load  

**Fix:**

1. Try again in a few seconds  
2. Increase timeout in `pokemon_api.py`:

requests.get(url, timeout=10)

---

## 8. Script Exits Without Saving CSV

**Possible Causes:**

- All API calls failed  
- No valid Pokémon data was returned  
- Script exited early due to an error  

**Fix:**

1. Add temporary print statements inside the loop to track progress  
2. Try using only one name:

names = ["pikachu"]

3. Ensure the API URL loads in a browser  

---

## 9. General Debugging Tips

- Add print statements to track:
  - Which names are being processed  
  - The API URL being used  
  - Response status codes  
- Use try/except blocks around suspicious code  
- Ask: “What changed since the last time this worked?”  
- Re-run the script with a fresh virtual environment if necessary  

---

## 10. Still Having Issues?

If none of the above fixes resolve the error:

- Copy the full error message  
- Note the Pokémon names you used  
- Describe the steps you took  

Provide those details to your support/engineering contact or file an issue on GitHub.

---

## End of Troubleshooting Guide
