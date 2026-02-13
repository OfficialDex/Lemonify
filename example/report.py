from lemonify import lemon

result = lemon("you are dumbass and i will kill you")

print("Analysis report:")
print("toxicity   :", result["toxicity"], "| toxic:", result["toxicity"] > 0.5)
print("insult     :", result["insult"], "| insult:", result["insult"] > 0.5)
print("sexuality  :", result["sexuality"], "| sexual:", result["sexuality"] > 0.5)
print("threat     :", result["threat"], "| threat:", result["threat"] > 0.5)
print("neutrality :", result["neutrality"], "| neutral:", result["neutrality"] > 0.5)
