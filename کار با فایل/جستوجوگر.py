import os

def explore(ttype, address):
  ans = {}
  for ads, _, files in list(os.walk(address)):
    # abs_path = os.path.abspath(ads)
    for f in files:
        if "."+ttype.lower() in f.lower():
            ans[ads] = ans.get(ads, 0) + 1
  return(ans)
