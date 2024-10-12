
def check_registration_rules(**kwargs):
    valids = []
    for username, password in kwargs.items():
        if (len(username) >= 4 and username != "quera" and username != "codecup") and len(password) >= 6:
            if not password.isdigit(): 
                valids.append(username)
    return (valids)

def main():
    print(check_registration_rules(saeed='1234567', ab='afj$L12'))

if __name__ == '__main__':
    main()
