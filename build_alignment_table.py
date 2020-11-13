import os
import textgrid
import json
# import pandas as pd
# from sklearn import preprocessing

cwd = os.getcwd()
phonemes = {}
# iterate over the files in the "output" directory
for filename in os.listdir(os.path.join(cwd, 'output')):
  if not filename.endswith('.TextGrid'):
    continue
  tg = textgrid.TextGrid.fromFile(os.path.join(cwd, 'output', filename))
  # phonemes
  for t in tg[1]:
    if t.mark not in phonemes:
      phonemes[t.mark] = []
    # start, end, duration
    phonemes[t.mark].append([t.minTime, t.maxTime, t.maxTime - t.minTime])
print(phonemes)
# max duration for each phoneme
# (the longest time it took for a given phoneme across all speakers)
phonemes_max_duration = {}
for phoneme, data in phonemes.items():
  phonemes_max_duration[phoneme] = max(data, key=lambda times: times[2])[2]

# print(phonemes_max_duration)
# save the results
with open('alignments.json', 'w', newline='') as file:
  json.dump(phonemes, file)
with open('phonemes_max_duration.json', 'w', newline='') as file:
  json.dump(phonemes_max_duration, file)