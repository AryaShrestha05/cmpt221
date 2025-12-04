#!/bin/bash
# Script to view users table data
docker exec lab10-postgres psql -U postgres -d marist -c 'SELECT * FROM "Users";'

