####				BASIC CLASSIFICATION WITH SKLEARN				####
#### Source: https://www.youtube.com/watch?v=cKxRvEZd3Mw

from sklearn.naive_bayes import GaussianNB

BUMPY = 0
SMOOTH = 1

ORANGE = 0
APPLE = 1

# features: mass, texture
train_features = [ [ 150, BUMPY ], [ 170, BUMPY ], [ 140, SMOOTH ], [ 130, SMOOTH ] ]
train_labels   = [ ORANGE, ORANGE, APPLE, APPLE ]

clf = GaussianNB()

clf.fit( train_features, train_labels )

test_features = [ [ 120, SMOOTH ] ]
test_predicts = clf.predict( test_features )

for i in range( len( test_features ) ):
	print "\n\tthe prediction for", test_features[ i ],"is", "apple" if test_predicts[ i ] else "orange", "\n"
