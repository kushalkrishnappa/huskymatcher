"""
Implementation for matching professor data with queries.
"""

from abc import ABC, abstractmethod
from models import StudentProfile, MatchResult
from protocols import VectorStoreProvider
from typing import List


class MatchingStrategy(ABC):
    """Abstract base class for professor matching algorithms."""

    @abstractmethod
    def find_matches(
        self,
        student_profile: StudentProfile,
        vectorstore: VectorStoreProvider,
        top_k: int = 5,
    ) -> List[MatchResult]:
        """Find matching professors for a student."""
        pass


class SemanticMatchingStrategy(MatchingStrategy):
    """
    Implementation for semantic similarity-based matching.

    This implementation uses vector embeddings to find professors whose
    research interests and work align with the student's profile.
    """

    def find_matches(
        self,
        student_profile: StudentProfile,
        vectorstore: VectorStoreProvider,
        top_k: int = 5,
    ) -> List[MatchResult]:
        """Find matching professors for a student."""
        pass
