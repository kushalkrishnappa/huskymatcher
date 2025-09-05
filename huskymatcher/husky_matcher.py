"""
A simple LangChain-based system that matches students with professors based on resume and preferences.
"""

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HuskyMatcher:
    """Main class for the HuskyMatcher system."""

    def __init__(self):
        """Initialize the HuskyMatcher."""
        pass


class HuskyMatcherFactory:
    """Factory class for creating HuskyMatcher instances."""

    @staticmethod
    def create_matcher() -> HuskyMatcher:
        """Create and return a new HuskyMatcher instance."""
        return HuskyMatcher()
