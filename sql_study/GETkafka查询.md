```python
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "account_status": {
              "value": "normal"
            }
          }
        },
        {
          "term": {
            "is_db": {
              "value": false
            }
          }
        }
      ], 
      "must_not": [
        {
          "term": {
            "follower_count": {
              "value": -1
            }
          }
        }
      ]
    }
  }
}

{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "account_status": {
              "value": "normal"
            }
          }
        },
        {
          "term": {
            "is_db": {
              "value": true
            }
          }
        }

      ],
            "filter": {
        "range": {
          "follower_count": {
            "gte": 10000
          }
        }
      }, 

      "must_not": [
        {
          "term": {
            "crawl_status": {
              "value": "done"
            }
          }
        },{
          "term": {
            "follower_count": {
              "value": "-1"
            }
          }
        }
      ]
    }
  }
}
```

