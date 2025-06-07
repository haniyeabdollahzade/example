def checl_registration_rules(**kwargs):
    valid_users = []
    for username, password in kwargs.items():
        if username in ['quera', 'codeup']:
            continue
        if len(username) < 4:
            continue
        if len(password) < 6 or password.isdigit():
            continue
        valid_users.append(username)
    return valid_users    

print(checl_registration_rules(username='password', sadegh='He3@lsa', quera='kLS45@l$'))