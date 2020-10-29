'''
do file
'''


def readme():
    content = ''
    files = ['01_intro.md', '02_why.md', '03_contributing.md', '04_legal.md']
    for file in files:
        with open(f'docs/getting_started/{file}') as f:
            content += f.read()
            content += '\n'
    with open('README.md', 'w') as f:
        f.write(content)
