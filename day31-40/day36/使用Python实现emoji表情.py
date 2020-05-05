"""
使用Python实现emoji表情
"""
import emoji

# 默认表情可以直接通过表情的字符实现
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Token is :downcast_face_with_sweat:'))
print(emoji.emojize('Sleeping is :zzz:', use_aliases=True))
print(emoji.emojize('老班晚安 :growing_heart:'))
print(emoji.emojize('你是猪吗？ :rolling_on_the_floor_laughing:'))

# 也可以使用Unicode方式
print(emoji.emojize('\U0001F32D'), emoji.emojize('\U0001F354'),
      emoji.emojize('\U0001F35F'), emoji.emojize('\U0001F355'),
      emoji.emojize('\U0001F35F'), emoji.emojize('\U0001F355'))
      
print(emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'),
      emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'),
      emoji.emojize('\U0001F33A'), emoji.emojize('\U0001F33A'))

print(emoji.emojize('\U0001F497'), emoji.emojize('\U0001F496'),
      emoji.emojize('\U0001F495'), emoji.emojize('\U0001F497'),
      emoji.emojize('\U0001F496'), emoji.emojize('\U0001F495'))

