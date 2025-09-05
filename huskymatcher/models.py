"""
This module contains data classes and enums used in huskymatcher.
"""

from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class Professor:
    """Data class representing a professor's information."""

    name: str
    designation: str
    research_interests: List[str]
    education: List[str]
    biography: str
    projects: List[str]
    recent_publications: List[str]
    contact: Dict[str, str]
    areas_of_interest: List[Dict[str, Any]]
    website: Optional[str] = None
    google_scholar_link: Optional[str] = None


class DegreeLevel(Enum):
    """Enum for degree levels."""

    BACHELORS = "bachelors"
    MASTERS = "masters"
    PHD = "phd"
    POSTDOC = "postdoc"


@dataclass
class StudentProfile:
    """
    Data class representing a student's profile and preferences.

    This class encapsulates all relevant information about a student
    that will be used for professor matching.
    """

    name: str
    years_of_experience: int
    degree_level: DegreeLevel
    research_interests: List[str]
    skills: List[str]
    gpa: Optional[float] = None
    publications: Optional[List[str]] = field(default_factory=list)
    projects: Optional[List[str]] = field(default_factory=list)
    preferred_professors: Optional[List[str]] = field(default_factory=list)
    resume_text: Optional[str] = None

    def __post_init__(self) -> None:
        """Validate student profile data after initialization."""
        if self.years_of_experience < 0:
            raise ValueError("Years of experience cannot be negative")
        if self.gpa is not None and not (0.0 <= self.gpa <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0")
        if not self.research_interests:
            raise ValueError("At least one research interest must be specified")


@dataclass
class MatchResult:
    """Data class representing a professor match result."""

    professor: Professor
    similarity_score: float
    match_reasons: List[str]
    research_overlap: List[str]
