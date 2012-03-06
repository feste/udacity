likelihood = 0.8 #p(pos|c)
prior = 0.001 #p(c)

likeNo = 0.1 #p(pos|notC)
priorNo = .999 #p(notC)

normalizingConstant = likeNo*priorNo + likelihood*prior

posterior = (likelihood * prior) / normalizingConstant

print posterior
