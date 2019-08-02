with open('requirements.txt') as input_file:
    reqs = [line.strip() for line in input_file.read().split() if not line.strip().startswith('#') and line.find(' req: ignore') == -1]
