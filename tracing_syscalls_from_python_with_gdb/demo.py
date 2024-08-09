import urllib.request

def main():
    contents = urllib.request.urlopen("http://example.com").read()
    print(contents)

if __name__ == '__main__':
    main()
