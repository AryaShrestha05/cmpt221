#!/bin/bash
# Script to display users table in a formatted way for screenshots
echo "=========================================="
echo "Users Table Data"
echo "=========================================="
echo ""
docker exec lab10-postgres psql -U postgres -d marist -c 'SELECT "UserID", "FirstName", "LastName", "Email", "PhoneNumber" FROM "Users" ORDER BY "UserID";'
echo ""
echo "=========================================="
echo "To see full details including passwords:"
echo "docker exec -it lab10-postgres psql -U postgres -d marist"
echo "Then run: SELECT * FROM \"Users\";"
echo "=========================================="

