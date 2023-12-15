import pandas

col = pandas.read_csv("data.txt")
txt = col.values.tolist()


## 1. Kurā gadā bija dibināts vecākais Omānas reģiona uzņēmums (informācija ir pieejama kolonnā Founded)?
# count = []
# for row in txt:
#     if row[4] == 'Oman':
#         count.append(row[6])
# print(min(count))

## 2.Kāds ir darbinieku skaits, kas strādā Latvijā?
# count = []
# for row in txt:
#     if row[4] == 'Latvia':
#         count.append(row[8])
# print(sum(count))

## 3.Kāds ir darbinieku skaits kas strādā telekomunikācijas jomā Latvijā.  (Industry = Telecommunications, Country = Latvia) ?
# employee = []
# for row in txt:
#     if row[4] == 'Latvia' and row[7] == 'Telecommunications':
#         employee.append(row[8])
# print(sum(employee))

## 4.Cik no datu bāze esošajiem Latvijas kompānijām ir SSL sertifikāts? (SSL sertifikāts ir kompānijām, kuram tīmekļa adrese sākas ar https://)
# website = []
# count = 0
# for row in txt:
#     if row[4] == 'Latvia':
#         website.append(row[3])
#
# for row in website:
#     if row[:5] == 'https':
#         count += 1
#
# print(count)

## 5.Cik reizes datu bāzē tiek minēts domēna vārds .org reģionam Latvia?
website = []
count = 0
for row in txt:
    if row[4] == 'Latvia':
        website.append(row[3])

for row in website:
    if row[-5:-1] == '.org':
        count += 1
print(count)


