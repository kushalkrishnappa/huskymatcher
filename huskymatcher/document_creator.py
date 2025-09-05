"""
Implementation for creating langchain documents from professor data.
"""

from abc import ABC, abstractmethod
from typing import Any, List
from models import Professor
from langchain.schema import Document


class DocumentCreator(ABC):
    """Abstract base class for creating documents from professor data."""

    @abstractmethod
    def create_documents(self, professors: Any) -> List[Document]:
        """Create documents from professor data."""
        pass


class ProfessorDocumentCreator(DocumentCreator):
    """
    Creates LangChain Document objects from Professor data.

    This class is responsible for converting Professor objects into
    searchable documents with appropriate metadata.
    """

    def create_documents(self, professors: List[Professor]) -> List[Document]:
        """Create LangChain Document objects from Professor data."""
        pass
