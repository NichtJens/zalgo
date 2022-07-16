# ZALGO!

## Text conversion

```python
from zalgo import zalgo, escalate, random

print(zalgo("To invoke the hive-mind representing chaos."))
print(zalgo("Invoking the feeling of chaos.", n=1))
print(zalgo("Without order.", n=10))

print(escalate("The Nezperdian hive-mind of chaos. Zalgo."))
print(random("He Who Waits Behind the Wall. ZALGO!"))
```

```zalgo
Ṱͪ̂͛́͠ọ̓ͤ̂̌̇ i̵̡̹̝ͤ̀ň͖̥ͬ̍ͮv̞͕̜͌ͤͩő̹̠ͮͣ͢k̨͍͎̱͚ͪé̹͈̺͆͑ t̵͎̐ͩ̈͆ĥ̖̭̙ͨ͢è̬͏̦̓͢ h͍̭̍͒̓͜i̳̗ͪͣͥ̕v͈ͣͪ̏ͦ̌ḛ̤͕̒̍͜-m̠̈̿͂̏̕i̡͈̗̞̪̋ṋ̸̷́̀͡d̷͇̪͗͂̌ r̢̲͈̭ͬ̃ȩ̶͉͏͈͜p̱̘̒́ͣ͑r̻̖̈͆̇ͅe̞̤̲̺ͧ̈́s͙̲̼̱ͣͅe̟͔ͭͮ͒͞n̳ͧ̃̓͑̾t̟͙̩̾͂̒i̴͕̺ͤ̔͝n͚͙̪͉̍͟g̵̰̀͊ͮ͝ c͎̫̠͙͟ͅh̷̖ͭ̎͛͠ả͙͓̿̓͢o̤͑̊̿̀͟s̛̰͛̄̑̓.
I̝n̋v̏o̝k̎i̪nͥg̣ tͨh͖eͧ fͧe͡e̵l̲ín̨gͨ o̗f̏ c͒h̤a̟o̳s̤.
W̄ͭ̔̈́̂͆̅̓ͪ͢ȋ̷̧̫͖ͤͩͪ̎̚t̨̮̖ͩͤ͒̊ͬ͂́h̸̵̡̨͈̠͗̀ͫͅo͓̬͚͍͎ͦͤ͒ͤ͞ű̦͙͇̫̄̂̂ͦ͡t̶̙͖̥̼͒ͩ̐̐͢ ŏ̜̣͕̜̀͆͆̓̕r̞̖̼̭̃ͩ̈̋̃͟d̷̡̨̮̼̠͖͕̎ͮe̴͙͓͎̻̜̎̾͑̒r̸̺̿͏̫̻̇̌̓͟.
T͂ḥeͭ Ǹėz̭p̐e͇r̽d̔͛i̪ͧa͎ͭn̔ͤ h̼ͅȋ͖v͏̃ȇ͏-m͉͐̑i͔ͮͮn͌͒͞d̶̸̠ ọ̴̶f̞̃̑ c̳̲̈́h͉̘ͬa̱͊̌͑o̽̓͛̽s͎̙̻̦. Z̬̋̾ͬą͙͌ͤl̮͂͡͝g̯̍̅͠ö̦̱͓.
H̭͚ͧ͜e͈͚̱ͪ̔ͭ͢ W̡̬̳͔̩̰̹ͤ̀h̶̷̟́̿ͮͤͩ͐o̵̺͋̌ͮ̏̿̍ͣ W̸a̷̢̮̟ͦ̊̎ͭ̿ĭ̬̮͍͓̤ͤͧ͑̍ţ̥̝͓ͦ̂s̙̙̽͊̒̉̂͒͜ Ḇ̫̑ͥ͜e̤̍ḥ̵̞̣ͥi̴̻͌̑̇ṋ̢̬͓ͭd͑͗̓͜͠ tͨ̊̎h͇̿ͩ̚e̶̡͓̽̉̑͟͜ Ẇ̖̮͚͙ͮą̠̦̀ḷ̬̤͕̾́̏ĺ. Z̢̖̥̮̎̋A̡͍̳̝͍͒Ľ̒G̉ͨO̧̬͖̙̬̰̅͐̉͑!
```

## Exceptions

```bash
$ ipython
```

```python
In [1]: import zalgo

In [2]: zalgo.exceptions.invoke()

In [3]: raise RuntimeError("To invoke the hive-mind representing chaos.")
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
<ipython-input-3-e1158b16b3c4> in <module>()
----> 1 raise RuntimeError("To invoke the hive-mind representing chaos.")

RuntimeError: T̠͔̘̒̈́̈͘o̡̻͈ͭ̎̀͢ i̡̭̮ͦͦ̂̚n̵̢̧͉̖͂ͪv̸̤͔̥̾́̏o̵̡͙̫ͣ̓͞k̴͓͖̜ͬ̇͞ȩ̫͖͑ͬ̂ͫ t͍̃̎ͪ̈́͏̨h̷͙̗̪́͛̔ẽ͔͎̦ͥ̌ͮ h̯̬̣̖ͭͭͣį̤ͤ̀ͨ̃̃v̰̳̬̱͉̟ͅe̷̪͙̥͌͋͜-m̛̰̝̦̬̃ͩi̢̪ͨͮ͘͢ͅṇ̷̛̗̭̇̍dͮ̍ͣ̑̃̃ͅ r̼͖̅̏̇̅̕ę̱͙͆̌ͣ̽p̶̭̬͆̔̂͌r̷̵̻̻ͩ͠͝ê͎̓̾̈͋͝s̸̲̹͋̓ͧͮẹ͚ͪ͛͐͞͞n͕͓̋͊͘͞͡t̼ͧ̐̏̕͟͞ĭ̧̻̪̾ͪ̀n̡̼̰̹̚͜͞g̞̩̳̩̑̂̉ c̵̘̜̯̽͐͗h̙͕̟ͬͧ̿͡ȃ̴͉͍͖̈͡o̲͈̅̂͋͂͆ś̳͙̫ͤͨͨ.
```

