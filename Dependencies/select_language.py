# What language will you be scripting in?
def select_language():
  print("\n=> Select language")
  languages = ["Python", "Ruby", "Javascript", "PHP"]
  for index, language in enumerate(languages, start = 1):
    print(f'{index}: {language}')
  user_input = int(input("What language will you be scripting in? Select index ").strip())
  if user_input <= len(languages):
    print(f"You selected {languages[user_input - 1]}")
    return languages[user_input - 1]
  else:
    print(f"Your list doesn\'t contain as many languages (max = {len(languages)})")
    return select_language()

def set_language_extension():
    language = select_language()
    return {
      'Python': '.py',
      'Javascript': '.js',
      'Ruby': '.rb',
      'HTML': '.html'
    }[language]