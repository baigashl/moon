from peewee import *

db = PostgresqlDatabase(
    'earth',
    port = '5432',
    host = 'localhost',
    user = 'air',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Company(BaseModel):
    name = CharField(max_length=255, null=False, unique=True)
    emploee_quantity = IntegerField()
    capital = IntegerField()
    owner = CharField(max_length=255, null=False)


class Emploee(BaseModel):
    company = ForeignKeyField(Company, on_delete='CASCADE')
    email = CharField(max_length=255, null=False, unique=True)
    name = CharField(max_length=255, null=False)
    second_name = CharField(max_length=255, null=False)
    salary = IntegerField()

# db.create_tables([Company, Emploee])

# Company.create(
#     name = 'Tesla',
#     emploee_quantity = 35,
#     capital = 3000000,
#     owner = 'Elon Mask'
# )

# Company.create(
#     name = 'Apple',
#     emploee_quantity = 4000,
#     capital = 30000000,
#     owner = 'Steve Jobs'
# )

# Emploee.create(
#     company = 1,
#     email = 'qweqwe123@gmail.com',
#     name = 'John',
#     second_name = 'Johnson',
#     salary = 10000
# )

# Emploee.create(
#     company = 1,
#     email = 'qweqasdwe123@gmail.com',
#     name = 'asdasd',
#     second_name = 'qweasdqwe',
#     salary = 1000
# )

# Emploee.create(
#     company = 2,
#     email = 'asdasd@gmail.com',
#     name = 'Aibek',
#     second_name = 'Aibekov',
#     salary = 5000
# )

# Emploee.create(
#     company = 2,
#     email = 'Beka@gmail.com',
#     name = 'Beka',
#     second_name = 'Bekov',
#     salary = 3000
# )

db.close()


