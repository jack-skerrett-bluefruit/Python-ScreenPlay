from behave import runner

def before_all(context : runner.Context):
    print('all')
    context.aaa = 'helen'
