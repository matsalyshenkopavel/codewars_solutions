"""Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)"""

def make_readable(seconds):
    answer = []
    answer.append(str(seconds // 3600))
    answer.append(str(seconds % 3600 // 60))
    answer.append(str((seconds % 3600) % 60))
    answer = ["0" + x  if len(x) == 1 else x for x in answer]
    return ':'.join(answer)

print(make_readable(33333))