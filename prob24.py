import sys

i = 0
digits = list(range(0,10))

for spot1 in digits:
	for spot2 in [i for i in digits if(i != spot1)]:
		for spot3 in [i for i in digits if(i not in [spot1,spot2])]:
			for spot4 in [i for i in digits if(i not in [spot1,spot2,spot3])]:
				for spot5 in [i for i in digits if(i not in [spot1,spot2,spot3,spot4])]:
					for spot6 in [i for i in digits if(i not in [spot1,spot2,spot3,spot4,spot5])]:
						for spot7 in [i for i in digits if(i not in [spot1,spot2,spot3,spot4,spot5,spot6])]:
							for spot8 in [i for i in digits if(i not in [spot1,spot2,spot3,spot4,spot5,spot6,spot7])]:
								for spot9 in [i for i in digits if(i not in [spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8])]:
									for spot10 in [i for i in digits if(i not in [spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9])]:
										i += 1
										if(i == 1000000):
											print("%d%d%d%d%d%d%d%d%d%d" % (spot1,spot2,spot3,spot4,spot5,spot6,spot7,spot8,spot9,spot10))
											sys.exit()

