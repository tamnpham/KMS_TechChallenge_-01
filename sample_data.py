import json 

sample_data = {
    'data' : [
          {
              'schema': 'table(name : text, score: number )',
              'question': 'who have score over 9',
              'sql': 'SELECT name FROM TABLE WHERE score > 9'
          }
    ]
}

with open('./data/sample_data.json' , 'w') as f:
  json.dump(sample_data, f)