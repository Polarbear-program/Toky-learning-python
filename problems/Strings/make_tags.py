def make_tags(tag, word):
  return f"<{tag}>" + word + f"</{tag}>" 

def make_tags_old(tag, word):
  return "<" + tag + ">" + word + "</" +tag +">" 

word = "Giam Dog"
tag = "i"
print(make_tags(tag, word))