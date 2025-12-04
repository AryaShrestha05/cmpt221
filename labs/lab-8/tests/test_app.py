# TODO: add five more unit test cases

def test_home_page(client):
    """Test that home page loads"""
    response = client.get('/')
    assert response.status_code == 200

def test_login_page(client):
    """Test that home page loads"""
    response = client.get('/login')
    assert response.status_code == 200

def test_users_page(client):
    """Test that users page loads"""
    response = client.get('/users')
    assert response.status_code == 200

def test_invalid_first_name(client):
    """Test signup validation for invalid first name"""
    response = client.post('/signup', data={
        'FirstName': '123',  # invalid - contains numbers
        'LastName': 'Doe',
        'Email': 'test@test.com',
        'PhoneNumber': '1234567890',
        'Password': 'password123'
    })
    assert b'First name can only contain letters' in response.data

def test_invalid_phone_number(client):
    """Test signup validation for invalid phone number"""
    response = client.post('/signup', data={
        'FirstName': 'John',
        'LastName': 'Doe',
        'Email': 'test@test.com',
        'PhoneNumber': '123',  # invalid - not 10 digits
        'Password': 'password123'
    })
    assert b'Phone number must be exactly 10 digits' in response.data

def test_signup_page_get(client):
    """Test that signup page loads on GET request"""
    response = client.get('/signup')
    assert response.status_code == 200

def test_invalid_last_name(client):
    """Test signup validation for invalid last name"""
    response = client.post('/signup', data={
        'FirstName': 'John',
        'LastName': 'Doe123',  # invalid - contains numbers
        'Email': 'test@test.com',
        'PhoneNumber': '1234567890',
        'Password': 'password123'
    })
    assert b'Last name can only contain letters' in response.data

def test_success_page(client):
    """Test that success page loads"""
    response = client.get('/success')
    assert response.status_code == 200

def test_error_page(client):
    """Test that error page loads"""
    response = client.get('/error')
    assert response.status_code == 200

def test_signup_with_valid_data_redirects(client):
    """Test that valid signup data redirects to home page"""
    response = client.post('/signup', data={
        'FirstName': 'Jane',
        'LastName': 'Smith',
        'Email': 'jane.smith@example.com',
        'PhoneNumber': '9876543210',
        'Password': 'securepass123'
    }, follow_redirects=False)
    # Should redirect to home page (status 302)
    assert response.status_code == 302
    # Check that it redirects to index
    assert '/index' in response.location or response.location == '/'