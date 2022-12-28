def year(year):
    def age(birth):
        return year - birth
    return age

def older_age(age):
    if age > 18:
        print('Of age')
    else:
        print('Under age')


current_year = year(2022)
older_or_under = older_age(current_year(2005))
print(older_or_under)
