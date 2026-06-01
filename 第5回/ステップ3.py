if txt == input_txt: # type: ignore
  print('正しく入力できています。')
else:
  print('誤りがあります。')
  print(f'正解の文字列:{txt}') # type: ignore
  print(f'ユーザーの文字列:{input_txt}') # type: ignore