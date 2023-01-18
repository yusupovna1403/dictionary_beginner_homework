def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    sum = 0
    for dict in data:
      if dict['job'] == job:
        sum+=1

    return sum

job = 'Developer'
data=[
  {
    'name': 'John', 
    'job': 'Developer'
  }, 
  {
    'name': 'Mary', 
    'job': 'Developer'
  }
  ]
print(count_jobs(data,job))




    