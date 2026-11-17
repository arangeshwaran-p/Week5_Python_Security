
# SECURITY AUDIT REPORT

## 1. SQL Injection
Problem:
Attackers may manipulate SQL queries using malicious input.

Solution:
Used parameterized SQL queries with ? placeholders.

## 2. Password Security
Problem:
Plain-text passwords can be stolen from databases.

Solution:
Used PBKDF2-HMAC-SHA256 password hashing with random salt.

## 3. Input Validation
Problem:
Invalid usernames and weak passwords can affect security.

Solution:
Added username and password validation.

## 4. Information Leakage
Problem:
Different login errors may reveal registered usernames.

Solution:
Used a common invalid username or password message.

## 5. Password Visibility
Problem:
Passwords may be visible while typing in the terminal.

Solution:
Used Python getpass module.

## 6. Testing
Five automated tests were executed successfully.

Result: ALL 5 TESTS PASSED.

## Conclusion
The application was improved using secure coding
practices, password hashing, input validation,
and SQL injection prevention.
