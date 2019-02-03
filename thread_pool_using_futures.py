from concurrent.futures import ThreadPoolExecutor as Executor

urls = """google twitter facebook youtube pinterest tumblr
instagram reddit flickr meetup classmates microsoft apple
linkedin xing renren disqus snapchat twoo whatsapp""".split()

def fetch(url):  1
    from urllib import request, error  2
    try:
        data = request.urlopen(url).read()
        return '{}: length {}'.format(url, len(data))
    except error.HTTPError as e:
        return '{}: {}'.format(url, e)

with Executor(max_workers=4) as exe:  3
    template = 'http://www.{}.com'
    jobs = [exe.submit(
        fetch, template.format(u)) for u in urls]  4
    results = [job.result() for job in jobs]  5

print('\n'.join(results))
