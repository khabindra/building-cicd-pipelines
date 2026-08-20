import os

# os.environ.get looks for an environment variable.
# if it doesn't exist, it returns 'Not Found'
token = os.environ.get('MY_GITHUB_TOKEN', 'Not Fount')

if token == 'Not Found':
    print('ERROR: Token not found in environment!')
else:
    print('SUCCESS: Token loaded!')
    # DANGER: We are printing the token to prove a point about masking 
    print(f'The token is: {token}')
