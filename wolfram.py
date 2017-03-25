import wolframalpha

client = wolframalpha.Client('XAHJ8V-K4EQRW4K3U');
res = client.query('2+2')

"""for pod in res.pods:
    for sub in pod.subpods:
        print(sub.text)"""

print("line")

print(next(res.results).text)
