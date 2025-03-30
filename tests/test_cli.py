import subprocess



def test_cli_help():
    """Test CLI help message."""
    result = subprocess.run(["python", "src/pubmed_fetcher/cli.py", "--help"], capture_output=True, text=True)
    assert "usage:" in result.stdout
    assert "Fetch research papers from PubMed." in result.stdout

def test_cli_execution():
    """Test CLI execution with a query."""
    result = subprocess.run(
        ["python", "src/pubmed_fetcher/cli.py", "Machine Learning"],
        capture_output=True,
        text=True,
        encoding="utf-8"  # Ensure Unicode compatibility
    )

    print(f"STDOUT: {result.stdout}")  # Debugging output
    print(f"STDERR: {result.stderr}")  # Debugging output
    assert result.returncode == 0, f"CLI execution failed: {result.stderr}"
    assert result.stdout, "CLI output is None"
    assert "Searching PubMed for:" in result.stdout
