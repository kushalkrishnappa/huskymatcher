"""
This module contains protocols (interfaces) for the huskymatcher.
"""

from typing import Protocol, List


class LLMProvider(Protocol):
    """Protocol for LLM providers."""

    def predict(self, text: str) -> str:
        """Generate a prediction based on the input text."""
        ...


class EmbeddingProvider(Protocol):
    """Protocol for embedding providers."""

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Embed a list of documents."""
        ...

    def embed_query(self, text: str) -> List[float]:
        """Embed a single query."""
        ...


class VectorStoreProvider(Protocol):
    """Protocol for vector store providers."""

    def add_documents(self, documents: List[str]) -> None:
        """Add documents to the vector store."""
        ...

    def similarity_search_with_score(self, query: str, k: int) -> List[tuple]:
        """Perform similarity search with scores."""
        ...
