from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

templateEnvironment = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

create_account = templateEnvironment.get_template('create_account.html')
index = templateEnvironment.get_template('index.html')
balance = templateEnvironment.get_template('balance.html')