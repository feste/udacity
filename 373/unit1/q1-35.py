#nead p(fair | heads)

likeF = 0.5
priorF = 0.5

likeN = 0.1
priorN = 0.5

posterior = likeF * priorF / (likeF * priorF + likeN * priorN)

print posterior
