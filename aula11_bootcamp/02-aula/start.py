from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random

app = FastAPI(debug=True)
fake = Faker()

file_name = "./data/products.csv"