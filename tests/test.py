from jsonsearch import JSONSearchEngine

# Example JSON data
data_json = {
    "name": "John",
    "age": 30,
    "address": {
        "city": "New York",
        "zipcode": "10001"
    },
    "emails": ["john@example.com", "john.doe@gmail.com"]
}

# Initialize JSONSearchEngine with JSON data
search_engine = JSONSearchEngine(data_json)

# Search for a specific key
key_results = search_engine.search_key("age")
print("Key results:", key_results)

# Search for a specific value
value_results = search_engine.search_value("New York")
print("Value results:", value_results)

# Find all occurrences of a pattern
pattern_results = search_engine.find_all(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')
print("Pattern results:", pattern_results)