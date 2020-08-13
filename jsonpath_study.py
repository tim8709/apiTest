from jsonpath import jsonpath

book_dict = {
    "store": {
        "book": [
            {"category": "reference",
             "author": "Nigel Rees",
             "title": "Sayings of the Century",
             "price": 8.95
             },
            {"category": "fiction",
             "author": "Evelyn Waugh",
             "title": "Sword of Honour",
             "price": 12.99
             },
            {"category": "fiction",
             "author": "Herman Melville",
             "title": "Moby Dick",
             "isbn": "0-553-21311-3",
             "price": 8.99
             },
            {"category": "fiction",
             "author": "J. R. R. Tolkien",
             "title": "The Lord of the Rings",
             "isbn": "0-395-19395-8",
             "price": 22.99
             }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    }
}

#store.book下所有的author值
print(jsonpath(book_dict, '$.store.book[*].author'))

# 所有author的值
print(jsonpath(book_dict, '$..author'))

# store中所有的value
print(jsonpath(book_dict, '$.store.*'))

# store下所有price的值
print(jsonpath(book_dict, '$.store..price'))

# book中第3个元素
print(jsonpath(book_dict, '$..book[2]'))

# book中最后1个元素
print(jsonpath(book_dict, '$..book[(@.length-1)]'))
print(jsonpath(book_dict, '$..book[-1:]'))

# book中前两个元素
print(jsonpath(book_dict, '$..book[0,1]'))
print(jsonpath(book_dict, '$..book[:2]'))

# 所有含有isbn的元素
print(jsonpath(book_dict, '$..book[?(@.isbn)]'))

# 所有price小于10的元素
print(jsonpath(book_dict, '$..book[?(@.price<10)]'))

