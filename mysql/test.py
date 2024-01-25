#!/usr/bin/env python

import random

import mysql.connector             
from mysql.connector import Error  
from faker import Faker
from faker.config import AVAILABLE_LOCALES

Faker.seed(33422)
fake = Faker()

conn = mysql.connector.connect(host='localhost', database='khoa', user='root', password='123')
cursor = conn.cursor()
  
for i in range(100000):
	row = [fake.name(), fake.phone_number(), fake.email(), fake.address(), fake.country()]

	sql = "INSERT INTO `test` (name, phone, email, address, country) VALUES (%s, %s, %s, %s, %s)"
	val = (row[0], row[1], row[2], row[3], row[4])

	cursor.execute(sql, val)

#cursor.execute('INSERT INTO `person` (name, age, birth_day) VALUES (%s, %s, %s)' % (row[0], row[1], row[2])
conn.commit()

