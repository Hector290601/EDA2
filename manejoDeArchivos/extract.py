def extractUserData():
    names = {}
    emails = {}
    passwords = {}
    file = open('dataset.xml', 'r')
    line = 'algo'
    while line != '':
        if line == '  <record>':
            name = file.readline()
            email = file.readline()
            password = file.readline()
            name = name.replace(name[-1], '')
            name = name.replace(' ', '')
            name = name.replace('<first_name>', '')
            name = name.replace('</first_name>', '')
            if name in names:
                names[name] += 1
            else:
                names[name] = 1
            email = email.replace(email[-1], '')
            email = email.replace(' ', '')
            email = email.replace('<email>', '')
            email = email.replace('</email>', '')
            at = email.find('@')
            dot = email.find('.')
            email = email[at+1:dot]
            if email in emails:
                emails[email] += 1
            else:
                emails[email] = 1
            password = password.replace(password[-1], '')
            password = password.replace(' ', '')
            password = password.replace('<password>', '')
            password = password.replace('</password>', '')
            if password in passwords:
                passwords[password] += 1
            else:
                passwords[password] = 1
        line = file.readline()
        line = line.replace(line[-1], '')
    if file:
        file.close()
    """
    mayorNombre = max(names.keys())
    mayorEmail = max(emails.keys())
    mayorPassword = max(passwords.keys())
    """
    mayorNombre =max(names, key = names.get)
    mayorEmail = max(emails, key = emails.get)
    mayorPassword = max(passwords, key = passwords.get)
    print(mayorNombre, ':', names.get(mayorNombre))
    print(mayorEmail, ':', emails.get(mayorEmail))
    print(mayorPassword, ':', passwords.get(mayorPassword))

if __name__ == '__main__':
    extractUserData()

