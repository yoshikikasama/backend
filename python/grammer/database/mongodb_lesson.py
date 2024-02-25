'''
JSON形式のデータを大量に投入する際に使用される
'''
from pymongo import MongoClient
import datetime


client = MongoClient('mongodb://localhost:27017/')
db = client['test_database']

stack1 = {
    'name': 'customer1',
    'pip':['python', 'java', 'go'],
    'info': {'os': 'mac'},
    'data': datetime.datetime.utcnow()
}
stack2 = {
    'name': 'customer2',
    'pip':['python', 'java'],
    'info': {'os': 'windows'},
    'data': datetime.datetime.utcnow()
}

db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack1).inserted_id
# print(stack_id, type(stack_id))
# print('######')
# print(db_stacks.find_one({'_id': stack_id}))
db_stacks = db.stacks
stack_id = db_stacks.insert_one(stack2).inserted_id

# now  = datetime.datetime.utcnow()
# for stack in db_stacks.find({'data': {'$gt': now}}):
#     print(stack)

db_stacks.find_one_and_update(
    {'name': 'custom1'}, {'$set': {'name': 'YYY'}}
)
print(db_stacks.find_one({'name': 'YYY'}))