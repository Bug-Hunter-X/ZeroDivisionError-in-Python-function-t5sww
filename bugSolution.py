def function(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 0 #or some other default value or error handling

result = function(10, 0)
print(result) # Output: 0