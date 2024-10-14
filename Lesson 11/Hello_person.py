#parsing command line arguments

def hello(name, lang):
  greetings = {
    'English' : 'Hello',
    'Spanish' : 'Hola',
    'German' : 'Hallo',
  }

  msg = f'{greetings[lang]} {name}!'
  print(msg)


if __name__ == '__main__':
  import argparse

  parser =  argparse.ArgumentParser(
    description = 'Provides a personal greeting.'
  )

  parser.add_argument(
    '-n', '--name', metavar='name', required=True, help='Name of the person'
  )

  parser.add_argument(
    '-l', '--lang', metavar='Language', required=True, help='Language of the greeting.', choices=['English', 'German', 'Spanish']
  )

  args = parser.parse_args()

  hello(args.name,args.lang)