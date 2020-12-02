def cleanData(data):
    data = data.replace(data[-1], '')
    moreThan = data.find('>')
    lessThan = data.find('</')
    data = data[moreThan+1:lessThan]
    return data

def addToDicc(dicc, data):
    if data in dicc:
        dicc[data] += 1
    else:
        dicc[data] = 1
    return dicc

def getMaxConcurrency(dicc):
    maxConc = max(dicc, key = dicc.get)
    return maxConc

def extractUserData():
    names = {}
    emails = {}
    passwords = {}
    concurrencies = {}
    genders = {}
    shirtSizes = {}
    try:
        file = open('dataset.xml', 'r')
    except:
        return
    line = 'algo'
    i = 0
    while line != '':
        if line == '  <record>':
            name = file.readline()
            email = file.readline()
            password = file.readline()
            concurrency = file.readline()
            gender = file.readline()
            shirtSize = file.readline()
            name = cleanData(name)
            names = addToDicc(names, name)
            email = cleanData(email)
            at = email.find('@')
            dot = email.find('.')
            email = email[at+1:dot]
            emails = addToDicc(emails, email)
            password = cleanData(password)
            passwords = addToDicc(passwords, password)
            concurrency = cleanData(concurrency)
            concurrencies = addToDicc(concurrencies, concurrency)
            gender = cleanData(gender)
            genders = addToDicc(genders, gender)
            shirtSize = cleanData(shirtSize)
            shirtSizes = addToDicc(shirtSizes, shirtSize)
        try:
            line = file.readline()
            line = line.replace(line[-1], '')
        except:
            break
    if file:
        file.close()
    moreFrequentlyName = getMaxConcurrency(names)
    moreFrequentlyEmail = getMaxConcurrency(emails)
    moreFrequentlyPassword = getMaxConcurrency(passwords)
    moreFrequentlyConcurrencies = getMaxConcurrency(concurrencies)
    moreFrequentlyGender = getMaxConcurrency(genders)
    moreFrequentlyShirtSize = getMaxConcurrency(shirtSizes)
    print(moreFrequentlyName, ':', names.get(moreFrequentlyName))
    print(moreFrequentlyEmail, ':', emails.get(moreFrequentlyEmail))
    print(moreFrequentlyPassword, ':', passwords.get(moreFrequentlyPassword))
    print(moreFrequentlyConcurrencies, ':', concurrencies.get(moreFrequentlyConcurrencies))
    print(moreFrequentlyGender, ':', genders.get(moreFrequentlyGender))
    print(moreFrequentlyShirtSize, ':', shirtSizes.get(moreFrequentlyShirtSize))

if __name__ == '__main__':
    extractUserData()

