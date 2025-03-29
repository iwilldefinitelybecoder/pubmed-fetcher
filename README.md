# PubMed Fetcher

## Overview
PubMed Fetcher is a command-line tool that allows users to search PubMed for research articles and retrieve relevant data programmatically. It is designed for researchers, developers, and data analysts who need to automate literature searches.

## Features
- Fetches research articles from PubMed based on user queries.
- Provides structured output in JSON format.
- CLI-based interaction for ease of use.
- Supports advanced search queries.

---

## Installation
### Prerequisites
- Python 3.13+
- Poetry (for dependency management)

### Steps to Install
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pubmed_fetcher.git
    cd pubmed_fetcher
    ```
2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```
3. Activate the virtual environment:
    ```sh
    poetry shell
    ```

---

## Usage
### Running the CLI
To search for research articles on a specific topic:
```sh
poetry run python src/cli.py "Machine Learning"
```

### Running Tests
Run unit tests using pytest:
```sh
poetry run pytest tests/
```


---

## How It Works
1. **CLI Execution:**
   - User provides a search term.
   - The CLI interacts with the PubMed API.
   - The results are fetched and displayed.

2. **PubMed API Interaction:**
   - Queries PubMed using `requests`.
   - Parses and formats the response.

3. **Output Handling:**
   - Results are printed in a readable format.
   - Can be exported as JSON.

---

## Troubleshooting
### Common Issues
- **CLI output is None:** Ensure you are running the command correctly with a valid query.
- **Encoding errors in Windows:** Run the following before executing the script:
  ```sh
  set PYTHONUTF8=1
  ```

---

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-new-feature
   ```
3. Commit changes:
   ```sh
   git commit -m "Add new feature"
   ```
4. Push and create a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For questions, reach out via GitHub Issues or email at `abhichandrav108@gmail.com`.

