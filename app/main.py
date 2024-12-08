from decorators import TaskDecorator

@TaskDecorator.cml_task(yaml_file='./decorators/testConfig.yaml')
def my_function(param1, param2):
    print(f"Processing {param1} and {param2}")
    return param1 + param2

# Вызов функции
result = my_function(1, 2)
print(result)
