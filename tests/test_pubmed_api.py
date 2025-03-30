import pytest
import requests
from unittest.mock import patch
from src.pubmed_fetcher.pubmed_api import fetch_pubmed_papers

def test_fetch_pubmed_benchmark(benchmark):
    result = benchmark(fetch_pubmed_papers, "AI in Healthcare", max_results=5)
    assert isinstance(result, list)

@patch("pubmed_api.requests.get")
def test_fetch_pubmed_success(mock_get):
    """Test successful API response."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.content = b"<root><PubmedArticle></PubmedArticle></root>"  # Mock valid XML

    result = fetch_pubmed_papers("AI in Healthcare", max_results=5)

    assert result is not None
    assert isinstance(result, list)


@patch("pubmed_api.requests.get")
def test_fetch_pubmed_api_failure(mock_get):
    """Test API failure (400 Bad Request)."""
    mock_get.return_value.status_code = 400
    mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()

    result = fetch_pubmed_papers("AI in Healthcare", max_results=5)

    assert result == [] 
