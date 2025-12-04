import pytest
import os
from unittest.mock import patch, MagicMock
from app import create_app

@pytest.fixture
def app():
    """Create application for testing"""
    # Mock the database initialization to prevent connection errors during testing
    with patch('app.init_database') as mock_init:
        mock_init.return_value = True
        # Also mock the logger to prevent file I/O issues
        with patch('app.logger'):
            app = create_app()
            app.config.update({
                "TESTING": True,
                # Use SQLite in-memory database for testing
                "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
            })
            yield app

@pytest.fixture
def client(app):
    """Test client for making requests"""
    return app.test_client()
